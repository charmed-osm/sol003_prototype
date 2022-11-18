from datetime import datetime, timedelta
from temporalio import workflow, activity

@activity.defn
async def request_create_vnf(name: str) -> list:
    print("I'm running the activity request_create_vnf")
    return [1,2,3]

@workflow.defn
class RequestCreateVnf:
    @workflow.run
    async def run(self, name: str) -> list:
        print(f"I'm starting the workflow RequestCreateVnf")
        return await workflow.execute_activity(
            request_create_vnf,
            name,
            schedule_to_close_timeout=timedelta(seconds=5)
        )
