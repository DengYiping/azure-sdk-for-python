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


class GalleryList(Model):
    """The List Galleries operation response.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. A list of galleries.
    :type value: list[~azure.mgmt.compute.v2018_06_01.models.Gallery]
    :param next_link: The uri to fetch the next page of galleries. Call
     ListNext() with this to fetch the next page of galleries.
    :type next_link: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Gallery]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value, next_link: str=None, **kwargs) -> None:
        super(GalleryList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
