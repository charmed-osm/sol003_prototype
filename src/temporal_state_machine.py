from state_machine import StateMachine

import asyncio
from temporalio.client import Client

# Import the workflow from the external interface

from temporal.request_create_vnf import RequestCreateVnf
from temporal.request_instantiate_vnf import RequestInstantiateVnf
from CreateVnfRequest import CreateVnfRequest
from VnfInstance import VnfInstance
class TemporalStateMachine(StateMachine):

    def request_create_vnf(self, create_vnf_request: CreateVnfRequest) -> VnfInstance:
        """

        Args:
            create_vnf_request: VNF creation parameters (5.5.2.3).

        Returns:
            VnfInstance: VNF instance (5.5.2.2).
        """
        client = None

        async def connect():
            return await Client.connect("localhost:7233")

        loop = asyncio.get_event_loop()
        client = loop.run_until_complete(connect())

        # Execute a workflow
        async def execute_workflow():
            return await client.execute_workflow(
                RequestCreateVnf.run,
                create_vnf_request,
                id="RequestInstantiateVnf",
                task_queue="lcm-task-queue")

        vnf_instance = loop.run_until_complete(execute_workflow())
        loop.close()

        return vnf_instance

    def request_instantiate_vnf(
        self, vnf_id: str, instantiate_vnf_request: dict
    ) -> (str, str):
        """

        Args:
            vnf_id:
            instantiate_vnf_request: VNF instantiation parameters (5.5.2.4).

        Returns:
            str: Response code.
            str: VNF lifecycle operation occurrence ID (VnfLcmOpOcc ID).
        """
        return (None, None)

    def get_vnf_lcm_op_occs(self, vnf_lcm_op_occ_id: str) -> dict:
        """

        Args:
            vnf_lcm_op_occ_id: VNF lifecycle operation occurrence ID. (VnfLcmOpOcc ID).

        Returns:
            dict: VNF lifecycle operation occurrence status information (5.5.2.13).
        """
        return None

if __name__ == "__main__":
    sm = TemporalStateMachine()
    create_vnf_request = CreateVnfRequest(
        vnfdId="VNFD_UUID",
        vnfInstanceName="My new Instance",
        vnfInstanceDescription="A VNF that I am creating",
        metadata={}
    )

    vnf_instance = sm.request_create_vnf(create_vnf_request=create_vnf_request)
    print (f'{vnf_instance}')