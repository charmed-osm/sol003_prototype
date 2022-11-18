from state_machine import StateMachine


class TemporalStateMachine(StateMachine):
    def request_create_vnf(self, create_vnf_request: dict) -> (str, dict):
        """

        Args:
            create_vnf_request: VNF creation parameters (5.5.2.3).

        Returns:
            str: Response code.
            dict: VNF instance (5.5.2.2).
        """
        return (None, None)

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
