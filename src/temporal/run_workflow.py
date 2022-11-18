import asyncio
from temporalio.client import Client

# Import the workflow from the external interface

from request_create_vnf import RequestCreateVnf
from request_instantiate_vnf import RequestInstantiateVnf

async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        RequestCreateVnf.run,
        "my name",
        id="RequestInstantiateVnf",
        task_queue="lcm-task-queue")

    print(f"Result: {result}")

    # Execute another workflow
    result = await client.execute_workflow(
        RequestInstantiateVnf.run,
        "my name",
        id="RequestInstantiateVnf",
        task_queue="lcm-task-queue")

    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())