# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class Cluster(Resource):
    """Contains information about a Cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource
    :vartype type: str
    :ivar location: The location of the resource
    :vartype location: str
    :ivar tags: The tags of the resource
    :vartype tags: dict[str, str]
    :param vm_size: The size of the virtual machines in the cluster. All
     virtual machines in a cluster are the same size. For information about
     available VM sizes for clusters using images from the Virtual Machines
     Marketplace (see Sizes for Virtual Machines (Linux) or Sizes for Virtual
     Machines (Windows). Batch AI service supports all Azure VM sizes except
     STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and
     STANDARD_DSV2 series).
    :type vm_size: str
    :param vm_priority: dedicated or lowpriority. The default value is
     dedicated. The node can get preempted while the task is running if
     lowpriority is choosen. This is best suited if the workload is
     checkpointing and can be restarted. Possible values include: 'dedicated',
     'lowpriority'. Default value: "dedicated" .
    :type vm_priority: str or ~azure.mgmt.batchai.models.VmPriority
    :param scale_settings: Desired scale for the Cluster.
    :type scale_settings: ~azure.mgmt.batchai.models.ScaleSettings
    :param virtual_machine_configuration: Settings for OS image and mounted
     data volumes.
    :type virtual_machine_configuration:
     ~azure.mgmt.batchai.models.VirtualMachineConfiguration
    :param node_setup: Setup to be done on all compute nodes in the Cluster.
    :type node_setup: ~azure.mgmt.batchai.models.NodeSetup
    :param user_account_settings: Settings for user account of compute nodes.
    :type user_account_settings:
     ~azure.mgmt.batchai.models.UserAccountSettings
    :param subnet: Specifies the identifier of the subnet.
    :type subnet: ~azure.mgmt.batchai.models.ResourceId
    :ivar creation_time: The creation time of the cluster.
    :vartype creation_time: datetime
    :ivar provisioning_state: Specifies the provisioning state of the cluster.
     Possible value are: creating - Specifies that the cluster is being
     created. succeeded - Specifies that the cluster has been created
     successfully. failed - Specifies that the cluster creation has failed.
     deleting - Specifies that the cluster is being deleted. Possible values
     include: 'creating', 'succeeded', 'failed', 'deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.batchai.models.ProvisioningState
    :ivar provisioning_state_transition_time: The provisioning state
     transition time of the cluster.
    :vartype provisioning_state_transition_time: datetime
    :ivar allocation_state: Indicates whether the cluster is resizing.
     Possible values are: steady and resizing. steady state indicates that the
     cluster is not resizing. There are no changes to the number of compute
     nodes in the cluster in progress. A cluster enters this state when it is
     created and when no operations are being performed on the cluster to
     change the number of compute nodes. resizing state indicates that the
     cluster is resizing; that is, compute nodes are being added to or removed
     from the cluster. Possible values include: 'steady', 'resizing'
    :vartype allocation_state: str or
     ~azure.mgmt.batchai.models.AllocationState
    :ivar allocation_state_transition_time: The time at which the cluster
     entered its current allocation state.
    :vartype allocation_state_transition_time: datetime
    :ivar errors: Contains details of various errors on the cluster including
     resize and node setup task. This element contains all the errors
     encountered by various compute nodes during node setup.
    :vartype errors: list[~azure.mgmt.batchai.models.BatchAIError]
    :ivar current_node_count: The number of compute nodes currently assigned
     to the cluster.
    :vartype current_node_count: int
    :ivar node_state_counts: Counts of various node states on the cluster.
    :vartype node_state_counts: ~azure.mgmt.batchai.models.NodeStateCounts
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'tags': {'readonly': True},
        'creation_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'provisioning_state_transition_time': {'readonly': True},
        'allocation_state': {'readonly': True},
        'allocation_state_transition_time': {'readonly': True},
        'errors': {'readonly': True},
        'current_node_count': {'readonly': True},
        'node_state_counts': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'vm_size': {'key': 'properties.vmSize', 'type': 'str'},
        'vm_priority': {'key': 'properties.vmPriority', 'type': 'VmPriority'},
        'scale_settings': {'key': 'properties.scaleSettings', 'type': 'ScaleSettings'},
        'virtual_machine_configuration': {'key': 'properties.virtualMachineConfiguration', 'type': 'VirtualMachineConfiguration'},
        'node_setup': {'key': 'properties.nodeSetup', 'type': 'NodeSetup'},
        'user_account_settings': {'key': 'properties.userAccountSettings', 'type': 'UserAccountSettings'},
        'subnet': {'key': 'properties.subnet', 'type': 'ResourceId'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'provisioning_state_transition_time': {'key': 'properties.provisioningStateTransitionTime', 'type': 'iso-8601'},
        'allocation_state': {'key': 'properties.allocationState', 'type': 'str'},
        'allocation_state_transition_time': {'key': 'properties.allocationStateTransitionTime', 'type': 'iso-8601'},
        'errors': {'key': 'properties.errors', 'type': '[BatchAIError]'},
        'current_node_count': {'key': 'properties.currentNodeCount', 'type': 'int'},
        'node_state_counts': {'key': 'properties.nodeStateCounts', 'type': 'NodeStateCounts'},
    }

    def __init__(self, **kwargs):
        super(Cluster, self).__init__(**kwargs)
        self.vm_size = kwargs.get('vm_size', None)
        self.vm_priority = kwargs.get('vm_priority', "dedicated")
        self.scale_settings = kwargs.get('scale_settings', None)
        self.virtual_machine_configuration = kwargs.get('virtual_machine_configuration', None)
        self.node_setup = kwargs.get('node_setup', None)
        self.user_account_settings = kwargs.get('user_account_settings', None)
        self.subnet = kwargs.get('subnet', None)
        self.creation_time = None
        self.provisioning_state = None
        self.provisioning_state_transition_time = None
        self.allocation_state = None
        self.allocation_state_transition_time = None
        self.errors = None
        self.current_node_count = None
        self.node_state_counts = None
