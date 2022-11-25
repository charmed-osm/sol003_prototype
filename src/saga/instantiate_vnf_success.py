import asyncio
from src.saga.sagas.sagas import SagaBuilder
from saga_state_machine import SagaStateMachine
from src.CreateVnfRequest import CreateVnfRequest
from src.VnfInstance import VnfInstance
from src.VnfLcmOpOcc import VnfLcmOpOccs
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


vnf_request_instantiation = {}


class SagaWorkflowSuccess(SagaStateMachine):

    def request_create_vnf(self, create_vnf_request: object) -> (str, object):
        """

        Args:
            create_vnf_request: VNF creation parameters (5.5.2.3).

        Returns:
            str: Response code.
            object: VNF instance (5.5.2.2).
        """
        raise TypeError

    def rollback_create_vnf(self, vnf_instance: object) -> None:
        """

        Args:
            vnf_instance: (5.5.2.2).
        """
        print("rollback_create_vnf_called")
        del(vnf_instance)

    def request_instantiate_vnf(self, vnf_id: str, instantiate_vnf_request: dict) -> (str, str):
        """

        Args:
            vnf_id:
            instantiate_vnf_request: VNF instantiation parameters (5.5.2.4).

        Returns:
            str: Response code.
            str: VNF lifecycle operation occurrence ID (VnfLcmOpOcc ID).
        """
        return 200, VnfLcmOpOccs.id

    def rollback_instantiate_vnf(self, vnf_lcm_opp_occs: object) -> None:
        """
        Args:
            vnf_lcm_opp_occs (object): VNF lifecycle operation occurrence
        """
        print("rollback_instantiate_vnf_called")
        self._set_status_cancel_of_vnf_lcm_op_occs(vnf_lcm_opp_occs)

    def get_vnf_lcm_op_occs(self, vnf_lcm_op_occ_id: str) -> dict:
        """

        Args:
            vnf_lcm_op_occ_id: VNF lifecycle operation occurrence ID. (VnfLcmOpOcc ID).

        Returns:
            dict: VNF lifecycle operation occurrence status information (5.5.2.13).
        """
        vnf_lcm_op_occs = self._find_opp_occs_by_id(vnf_lcm_op_occ_id)

        return dict((item, getattr(vnf_lcm_op_occs, item)) for item in dir(vnf_lcm_op_occs) if not item.startswith('__'))

    def _set_status_cancel_of_vnf_lcm_op_occs(self, vnf_lcm_opp_occs: object) -> None:
        """

        Args:
            vnf_lcm_opp_occ_id: VNF lifecycle operation occurrence ID. (VnfLcmOpOcc ID).

        Returns:
            dict: VNF lifecycle operation occurrence status information (5.5.2.13).
        """
        vnf_lcm_opp_occs._operationState = "Cancel"

    def _find_opp_occs_by_id(self, vnf_lcm_opp_occ_id: str) -> object:
        """

        Args:
            vnf_lcm_op_occ_id: VNF lifecycle operation occurrence ID. (VnfLcmOpOcc ID).

        Returns:
            vnf_lcm_opp_occ (object): VNF lifecycle operation occurrence
        """
        return VnfLcmOpOccs



saga_builder = SagaBuilder.create()
instance = SagaWorkflowSuccess()
vnfinstance = VnfInstance()
vnflcmopps = VnfLcmOpOccs()
create_request = CreateVnfRequest()

saga = (
    saga_builder.add_step(lambda: instance.request_create_vnf(create_request), lambda: instance.rollback_create_vnf(vnfinstance))
    .add_step(lambda: instance.request_instantiate_vnf(vnfinstance.id, vnf_request_instantiation), lambda: instance.rollback_instantiate_vnf(vnflcmopps))
    .build()
)

if __name__ == "__main__":
    asyncio.run(saga.run(exceptions=(AssertionError, TypeError)))
    logging.debug(vnfinstance.id)
    logging.debug(vnflcmopps.id)

