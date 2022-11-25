from dataclasses import dataclass


@dataclass
class VnfLcmOpOccs:  # 5.5.2.13, page 131
    stateEnteredTime: str = None
    startTime: str = None
    vnfInstanceId: str = None
    grantId: str = None
    operation: str = None
    isAutomaticInvocation: bool = None
    operationParams: object = None
    isCancelPending: bool = None
    cancelMode: str = None
    error: str = None
    operationState: str = None
    id: str = None
