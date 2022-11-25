from dataclasses import dataclass


class VnfLcmOpOccs:  # 5.5.2.13, page 131
    stateEnteredTime: float = None
    startTime: float = None
    vnfInstanceId: str = None
    grantId: str = None
    operation: str = None
    isAutomaticInvocation: bool = None
    operationParams: object = None
    isCancelPending: bool = None
    cancelMode: str = None
    error: str = None
    operationState: str = "SUCCESS"
    id: str = "lcm_opp_id"

    @property
    def operationState(self) -> str:
        return self._operationState

    @operationState.setter
    def operationState(self, value: str) -> None:
        self._operationState = value
#
