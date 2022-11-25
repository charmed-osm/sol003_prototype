from src.CreateVnfRequest import CreateVnfRequest
from src.VnfInstance import InstantiatedVnfInfo, VnfInstance
from src.VnfLcmOpOcc import VnfLcmOpOccs

instantiated_vnf_info = InstantiatedVnfInfo(
    flavourId="flavor-id",
    vnfState="NOT_INSTANTIATED",
    extCpInfo=[],
    extManagedVirtualLinkInfo=[],
    extVirtualLinkInfo=[],
    scaleStatus=[],
    maxScaleLevels=[],
    monitoringParameters=[],
    vnfcResourceInfo=[],
    vnfVirtualLinkResourceInfo=[],
    virtualStorageResourceInfo=[],
    vipCpInfo=[],
)
vnf_instance = VnfInstance(
    id="New ID Goes Here",
    instantiationState="NOT_INSTANTIATED",
    instantiatedVnfInfo=instantiated_vnf_info,
    vnfConfigurableProperties={},
    metadata={},
)


create_vnf_request = CreateVnfRequest(
    vnfdId="VNFD_UUID",
    vnfInstanceName="My new Instance",
    vnfInstanceDescription="A VNF that I am creating",
    metadata={},
)

vnf_lcm_op_occs = VnfLcmOpOccs(
    stateEnteredTime="STATE ENTER DATE",
    startTime="STATE ENTER DATE",
    vnfInstanceId="VNF_INS_UUID",
    grantId="",
    operation="INSTANTIATE",
    isAutomaticInvocation="False",
    operationParams=object,
    isCancelPending=False,
    cancelMode="",
    error="",
    operationState="",
    id="New LcmOpOcc ID",
)
