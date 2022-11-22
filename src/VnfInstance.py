class InstantiatedVnfInfo:
    flavourId: str       # SOL002SOL003_def.yaml#/definitions/IdentifierInVnfd
    vnfState: str        # SOL002SOL003VNFLifecycleManagement_def.yaml#/definitions/VnfOperationalStateType
    scaleStatus: list    # SOL002SOL003VNFLifecycleManagement_def.yaml#/definitions/ScaleInfo
    maxScaleLevels: list # SOL002SOL003VNFLifecycleManagement_def.yaml#/definitions/ScaleInfo
    extCpInfo: list      # SOL002SOL003VNFLifecycleManagement_def.yaml#/definitions/VnfExtCpInfo
    vipCpInfo: list      # SOL002SOL003VNFLifecycleManagement_def.yaml#/definitions/VipCpInfo
    extVirtualLinkInfo: list         # SOL002SOL003VNFLifecycleManagement_def.yaml#/definitions/ExtVirtualLinkInfo
    extManagedVirtualLinkInfo: list  # definitions/ExtManagedVirtualLinkInfo
    monitoringParameters: list       # SOL002SOL003VNFLifecycleManagement_def.yaml#/definitions/MonitoringParameter
    localizationLanguage: str
    vnfcResourceInfo: list           # definitions/VnfcResourceInfo
    vnfVirtualLinkResourceInfo: list # definitions/VnfVirtualLinkResourceInfo
    virtualStorageResourceInfo: list # definitions/VirtualStorageResourceInfo


'''
      This type represents a VNF instance. It shall comply with the provisions defined in table 5.5.2.2-1.

      NOTE:	Clause B.3.2 provides examples illustrating the relationship among the different run-time
            information elements (CP, VL and link ports) used to represent the connectivity of a VNF.

      NOTE 1:	Modifying the value of this attribute shall not be performed when conflicts exist between
              the previous and the newly referred VNF package, i.e. when the new VNFD is changed with
              respect to the previous VNFD in other aspects than merely referencing to other VNF software
              images. In order to avoid misalignment of the VnfInstance with the current VNF's on-boarded
              VNF Package, the values of attributes in the VnfInstance that have corresponding attributes
              in the VNFD shall be kept in sync with the values in the VNFD.
      NOTE 2:	ETSI GS NFV-SOL 001 specifies the structure and format of the VNFD based on TOSCA specifications.
      NOTE 3:	VNF configurable properties are sometimes also referred to as configuration parameters applicable
              to a VNF. Some of these are set prior to instantiation and cannot be modified if the VNF is instantiated,
              some are set prior to instantiation (are part of initial configuration) and can be modified later,
              and others can be set only after instantiation. The applicability of certain configuration may
              depend on the VNF and the required operation of the VNF at a certain point in time.
      NOTE 4:	Upon creation of the VnfInstance structure, the VNFM shall create and initialize all child attributes
              of "vnfConfigurableProperties", "metadata" and "extensions" that were declared in the VNFD with a defined
              initial value. The defined initial values can be declared in the VNFD, and/or, in case of "metadata",
              obtained from the "CreateVnfRequest" structure. Child attributes of "vnfConfigurableProperties",
              "metadata" and "extensions" that have no defined initial value shall not be created, in order to be
              consistent with the semantics of the JSON Merge Patch method (see IETF RFC 7396) that interprets null
              values as deletion request.
      NOTE 5:	It is possible to have several ExtManagedVirtualLinkInfo for the same VNF internal VL in case of a
              multi-site VNF spanning several VIMs. The set of ExtManagedVirtualLinkInfo corresponding to the same
              VNF internal VL shall indicate so by referencing to the same VnfVirtualLinkDesc and externally-managed
              multi-site VL instance (refer to clause 5.5.3.3).
      NOTE 6:	Even though externally-managed internal VLs are also used for VNF-internal connectivity, they shall
              not be listed in the "vnfVirtualLinkResourceInfo" attribute as this would be redundant.
    type: object
    required:
      - id
      - vnfdId
      - vnfProvider
      - vnfProductName
      - vnfSoftwareVersion
      - vnfdVersion
      - instantiationState
'''

class VnfInstance:
    id: str
    vnfInstanceName: str
    vnfInstanceDescription: str
    vnfdId: str
    vnfProvider: str
    vnfProductName: str
    vnfSoftwareVersion: str
    vnfdVersion: str
    vnfConfigurableProperties: dict
    vimConnectionInfo: str #?
    instantiationState: str # Should be an Enum
    instantiatedVnfInfo: InstantiatedVnfInfo
    metadata: dict
    # extensions: dict #? Need to look into this

