from enum import Enum


class State(Enum):
    NOT_STARTED = 0
    PROCESSING = 1
    COMPLETED = 2
    FAILED_TEMP = 3
    FAILED = 4
    ROLLING_BACK = 5
    ROLLED_BACK = 6


class StepStates:
    def __init__(self):
        self._state = State.NOT_STARTED

    @property
    def state(self):
        return self._state

    @property
    def complete(self):
        return self._state in [State.ROLLED_BACK, State.COMPLETED, State.FAILED]

    @property
    def success(self):
        return self._state == State.COMPLETED

    @property
    def processing(self):
        return self._state in [State.PROCESSING, State.ROLLING_BACK]

    @property
    def processed(self):
        return self._state in [State.COMPLETED, State.FAILED]

    @property
    def failure(self):
        return self._state == State.FAILED
