from datetime import datetime, timedelta
from temporalio import workflow, activity
from src.CreateVnfRequest import CreateVnfRequest
from src.VnfInstance import VnfInstance, InstantiatedVnfInfo

@activity.defn
async def request_create_vnf(vnfRequest: CreateVnfRequest) -> VnfInstance:
    print("I'm running the activity request_create_vnf")
    instantiatedVnfInfo = InstantiatedVnfInfo(
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
        vipCpInfo=[]
    )
    vnfInstance = VnfInstance(
        id="New ID Goes Here",
        instantiationState="NOT_INSTANTIATED",
        instantiatedVnfInfo=instantiatedVnfInfo,
        vnfConfigurableProperties={},
        metadata={}
    )
    return vnfInstance

@workflow.defn
class RequestCreateVnf:
    @workflow.run
    async def run(self, vnfRequest: CreateVnfRequest) -> VnfInstance:
        print(f"I'm starting the workflow RequestCreateVnf")
        return await workflow.execute_activity(
            request_create_vnf,
            vnfRequest,
            schedule_to_close_timeout=timedelta(seconds=5)
        )
