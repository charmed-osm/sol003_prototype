import unittest
from src import (
    StateMachineFactory,
    SagaStateMachine,
    StatePatternStateMachine,
    TemporalStateMachine,
)


class TestStateMachineFactory(unittest.TestCase):
    def setUp(self):
        self.factory = StateMachineFactory()

    def test_temporal_state_machine_is_created(self):
        temporal = self.factory.get_state_machine("temporal")
        self.assertIsInstance(temporal, TemporalStateMachine)

    def test_saga_state_machine_is_created(self):
        saga = self.factory.get_state_machine("saga")
        self.assertIsInstance(saga, SagaStateMachine)

    def test_state_pattern_state_machine_is_created(self):
        state = self.factory.get_state_machine("state")
        self.assertIsInstance(state, StatePatternStateMachine)

    def test_invalid_state_machine_raises_exception(self):
        with self.assertRaises(ValueError):
            self.factory.get_state_machine("invalid")
