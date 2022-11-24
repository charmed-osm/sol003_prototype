#######################################################################################################
# This is the effective main of a new LCM.  We

import asyncio
from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker

from temporal.request_create_vnf import RequestCreateVnf, request_create_vnf
from temporal.request_instantiate_vnf import RequestInstantiateVnf, request_instantiate_vnf

async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Run the worker
    worker = Worker(client,
        task_queue="lcm-task-queue",
        workflows=[
            RequestCreateVnf,
            RequestInstantiateVnf],
        activities=[
            request_create_vnf,
            request_instantiate_vnf])
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())