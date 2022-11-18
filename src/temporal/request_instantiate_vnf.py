from datetime import datetime, timedelta
from temporalio import workflow, activity

@activity.defn
async def request_instantiate_vnf(vnf_id: str) -> list:
    print(f"I'm running the activity request_instantiate_vnf for {vnf_id}")
    return ('a','b',1)

@workflow.defn
class RequestInstantiateVnf:
    @workflow.run
    async def run(self, vnf_id: str) -> list:
        print(f"I'm starting the workflow for request_instantiate_vnf")
        return await workflow.execute_activity(
            request_instantiate_vnf,
            vnf_id,
            schedule_to_close_timeout=timedelta(seconds=5)
        )