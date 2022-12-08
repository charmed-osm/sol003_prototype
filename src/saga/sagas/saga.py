from collections.abc import Sequence
from .event_gather import do_gather
from .states import State, StepStates
from .step import Step
from typing import List
import logging



class Saga(StepStates):
    steps: List[Step] = []

    def __init__(self, steps: list = None):
        if steps is None:
            steps = []
        assert isinstance(steps, Sequence), "Steps must be a sequence"
        self.steps = steps
        super().__init__()

    def _failure(self):
        return any([step.failure for step in self.steps])

    async def run(self, *args, executor=None, exceptions=None, **kwargs):
        self._state = State.PROCESSING
        run_futures = [step.do_run(*args, **kwargs) for step in self.steps]
        await do_gather(*run_futures, allowed_exc=(exceptions))
        self._state = State.FAILED_TEMP if self._failure() else State.COMPLETED
        if self._failure():
            retry_futures = [step.handle_retry(*args, **kwargs) for step in self.steps]
            await do_gather(*retry_futures, allowed_exc=(exceptions))
            self._state = State.FAILED if self._failure() else State.COMPLETED
            if self._failure():
                rollback_futures = [step.do_rollback(*args, **kwargs) for step in self.steps if step.processed]
                await do_gather(*rollback_futures, allowed_exc=(exceptions))
        logging.debug(self._state)


class SagaBuilder(object):
    def __init__(self):
        self.steps = []

    @staticmethod
    def create():
        return SagaBuilder()

    def add_step(self, func, compensation, retry=0):
        step = Step(func, retry, compensation)
        self.steps.append(step)
        return self

    def build(self):
        return Saga(self.steps)
