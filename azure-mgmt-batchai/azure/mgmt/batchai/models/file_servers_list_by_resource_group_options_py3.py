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

from msrest.serialization import Model


class FileServersListByResourceGroupOptions(Model):
    """Additional parameters for list_by_resource_group operation.

    :param max_results: The maximum number of items to return in the response.
     A maximum of 1000 files can be returned. Default value: 1000 .
    :type max_results: int
    """

    _attribute_map = {
        'max_results': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, max_results: int=1000, **kwargs) -> None:
        super(FileServersListByResourceGroupOptions, self).__init__(**kwargs)
        self.max_results = max_results
