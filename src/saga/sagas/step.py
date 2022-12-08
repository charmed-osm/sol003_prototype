import asyncio
from abc import abstractmethod
from inspect import iscoroutinefunction as is_coroutine
from .states import State, StepStates


class BaseStep(StepStates):
    @abstractmethod
    async def run(self, *args, **kwargs):
        pass

    @abstractmethod
    async def rollback(self, *args, **kwargs):
        pass


class Step(BaseStep):
    """
    Creates an saga step with a function to call with its compensation
    """

    def __init__(self, func, retry: int = 0, compensation=None):
        assert callable(func) is True, "'func' argument must be callable"
        self.func = func
        self.retry = retry
        if compensation:
            assert callable(compensation) is True, "'func' argument must be callable"
            self.compensation = compensation
        super().__init__()

    async def handle_retry(self, *args, **kwargs):
        try:
            while self.retry > 0:
                try:
                    res = await self.run(*args, **kwargs)
                    self._state = State.COMPLETED
                    return res

                except Exception:
                    self.retry -= 1

            else:
                self._state = State.FAILED

        except Exception as retry_eror:
            self._state = State.FAILED
            raise retry_eror

    async def do_run(self, *args, **kwargs):
        self._state = State.PROCESSING
        try:
            res = await self.run(*args, **kwargs)
            self._state = State.COMPLETED
            return res

        except Exception as error:
            if self.retry:
                self._state = State.FAILED_TEMP
            else:
                self._state = State.FAILED
                raise error



    async def do_rollback(self, *args, **kwargs):
        self._state = State.ROLLING_BACK
        res = await self.rollback(*args, **kwargs)
        self._state = State.ROLLED_BACK
        return res

    async def _call_func(self, func, *args, executor=None, **kwargs):
        if is_coroutine(func):
            return await func(*args, **kwargs)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(executor, func, *args, **kwargs)

    async def run(self, *args, **kwargs):
        return await self._call_func(self.func, *args, **kwargs)

    async def rollback(self, *args, **kwargs):
        return (
            await self._call_func(self.compensation, *args, **kwargs)
            if self.compensation
            else None
        )
