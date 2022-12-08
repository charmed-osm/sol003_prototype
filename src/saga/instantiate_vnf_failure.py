import asyncio
from pprint import pprint
from src.saga.sagas import SagaBuilder
from src.VnfInstance import VnfInstance
import logging
from request_objects import create_vnf_request, vnf_instance, vnf_lcm_op_occs


class RequestVnfCreateException(Exception):
    pass


class RequestInstantiateVnfException(Exception):
    pass


class SagaStateMachine:
    def request_create_vnf(self, create_vnf_request: object) -> VnfInstance:
        """

        Args:
            create_vnf_request: VNF creation parameters (5.5.2.3).

        Returns:

            object: VNF instance (5.5.2.2).
        """
        logging.debug("request_create_vnf method called")
        vnf_instance.id = "VNF_ID_1"
        raise RequestVnfCreateException

    def rollback_create_vnf(self, instance: object) -> None:
        """

        Args:
            instance: (5.5.2.2).
        """
        logging.debug("rollback_create_vnf called")
        del instance

    def request_instantiate_vnf(self, vnf_id: str, instantiate_vnf_request: dict) -> (str, str):
        """

        Args:
            vnf_id:
            instantiate_vnf_request: VNF instantiation parameters (5.5.2.4).

        Returns:
            str: Response code.
            str: VNF lifecycle operation occurrence ID (VnfLcmOpOcc ID).
        """
        logging.debug("request_instantiate_vnf method called")
        vnf_lcm_op_occs.vnfInstanceId = (vnf_id,)
        vnf_lcm_op_occs.id = "OPP_ID_1"
        vnf_lcm_op_occs.operationState = "COMPLETED"

        return 200, vnf_lcm_op_occs.id

    def rollback_instantiate_vnf(self, vnf_lcm_opp_occs: object) -> None:
        """
        Args:
            vnf_lcm_opp_occs (object): VNF lifecycle operation occurrence
        """
        logging.debug("rollback_instantiate_vnf method called")

        self._set_status_rollback_lcm_op_occs(vnf_lcm_opp_occs)

    def get_vnf_lcm_op_occs(self, vnf_lcm_op_occ_id: str) -> dict:
        """

        Args:
            vnf_lcm_op_occ_id: VNF lifecycle operation occurrence ID. (VnfLcmOpOcc ID).

        Returns:
            dict: VNF lifecycle operation occurrence status information (5.5.2.13).
        """
        logging.debug("get_vnf_lcm_op_occs method called")
        return dict(
            (item, getattr(vnf_lcm_op_occs, item))
            for item in dir(vnf_lcm_op_occs)
            if not item.startswith("__")
        )

    def _set_status_rollback_lcm_op_occs(self, vnf_lcm_op_occs: object) -> None:
        """

        Args:
            vnf_lcm_opp_occ_id: VNF lifecycle operation occurrence ID. (VnfLcmOpOcc ID).

        Returns:
            dict: VNF lifecycle operation occurrence status information (5.5.2.13).
        """
        vnf_lcm_op_occs.operationState = "ROLLED_BACK"


if __name__ == "__main__":
    saga_builder = SagaBuilder.create()
    sg_vnf_instantiate = SagaStateMachine()
    saga = (
        saga_builder.add_step(
            lambda: sg_vnf_instantiate.request_create_vnf(create_vnf_request),
            lambda: sg_vnf_instantiate.rollback_create_vnf(vnf_instance),
        )
        .add_step(
            lambda: sg_vnf_instantiate.request_instantiate_vnf(vnf_instance.id, {}),
            lambda: sg_vnf_instantiate.rollback_instantiate_vnf(vnf_lcm_op_occs),
            retry=2,
        )
        .build()
    )
    asyncio.run(saga.run(exceptions=(RequestInstantiateVnfException, RequestVnfCreateException)))
    logging.debug(pprint(sg_vnf_instantiate.get_vnf_lcm_op_occs(vnf_lcm_op_occs.id)))
