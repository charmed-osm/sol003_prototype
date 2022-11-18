from saga_state_machine import SagaStateMachine
from state_pattern_state_machine import StatePatternStateMachine
from temporal_state_machine import TemporalStateMachine


class StateMachineFactory:
    def __init__(self):
        self._state_machines = {
            "temporal": TemporalStateMachine,
            "saga": SagaStateMachine,
            "state": StatePatternStateMachine,
        }

    def get_state_machine(self, pattern):
        state_machine = self._state_machines.get(pattern)
        if not state_machine:
            raise ValueError(pattern)
        return state_machine()
