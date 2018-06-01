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

from .device_life_cycle_event_properties import DeviceLifeCycleEventProperties


class IotHubDeviceCreatedEventData(DeviceLifeCycleEventProperties):
    """Event data for Microsoft.Devices.DeviceCreated event.

    :param device_id: The unique identifier of the device. This case-sensitive
     string can be up to 128 characters long, and supports ASCII 7-bit
     alphanumeric characters plus the following special characters: - : . + % _
     &#35; * ? ! ( ) , = @ ; $ '.
    :type device_id: str
    :param hub_name: Name of the IoT Hub where the device was created or
     deleted.
    :type hub_name: str
    :param op_type: The event type specified for this operation by the IoT
     Hub.
    :type op_type: str
    :param operation_timestamp: The ISO8601 timestamp of the operation.
    :type operation_timestamp: str
    :param twin: Information about the device twin, which is the cloud
     represenation of application device metadata.
    :type twin: ~azure.eventgrid.models.DeviceTwinInfo
    """

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'hub_name': {'key': 'hubName', 'type': 'str'},
        'op_type': {'key': 'opType', 'type': 'str'},
        'operation_timestamp': {'key': 'operationTimestamp', 'type': 'str'},
        'twin': {'key': 'twin', 'type': 'DeviceTwinInfo'},
    }

    def __init__(self, **kwargs):
        super(IotHubDeviceCreatedEventData, self).__init__(**kwargs)
