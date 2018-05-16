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

from .resource_py3 import Resource


class GalleryImage(Resource):
    """Specifies information about the gallery image that you want to create or
    update.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param description: The description of this gallery image resource.
    :type description: str
    :param eula: The Eula agreement for the gallery image.
    :type eula: str
    :param privacy_statement_uri: The privacy statement uri.
    :type privacy_statement_uri: str
    :param release_note_uri: The release note uri.
    :type release_note_uri: str
    :param os_type: This property allows you to specify the type of the OS
     that is included in the disk if creating a VM from user-image or a
     specialized VHD. <br><br> Possible values are: <br><br> **Windows**
     <br><br> **Linux**. Possible values include: 'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_06_01.models.OperatingSystemTypes
    :param os_state: The OS State. Possible values include: 'Generalized',
     'Specialized'
    :type os_state: str or
     ~azure.mgmt.compute.v2018_06_01.models.OperatingSystemStateTypes
    :param end_of_life_date: The end of life of this gallery image.
    :type end_of_life_date: date
    :param identifier:
    :type identifier:
     ~azure.mgmt.compute.v2018_06_01.models.GalleryImageIdentifier
    :param recommended:
    :type recommended:
     ~azure.mgmt.compute.v2018_06_01.models.RecommendedMachineConfiguration
    :param disallowed:
    :type disallowed: ~azure.mgmt.compute.v2018_06_01.models.Disallowed
    :param purchase_plan:
    :type purchase_plan:
     ~azure.mgmt.compute.v2018_06_01.models.ImagePurchasePlan
    :ivar provisioning_state: The provisioning state, which only appears in
     the response.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'eula': {'key': 'properties.eula', 'type': 'str'},
        'privacy_statement_uri': {'key': 'properties.privacyStatementUri', 'type': 'str'},
        'release_note_uri': {'key': 'properties.releaseNoteUri', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'os_state': {'key': 'properties.osState', 'type': 'OperatingSystemStateTypes'},
        'end_of_life_date': {'key': 'properties.endOfLifeDate', 'type': 'date'},
        'identifier': {'key': 'properties.identifier', 'type': 'GalleryImageIdentifier'},
        'recommended': {'key': 'properties.recommended', 'type': 'RecommendedMachineConfiguration'},
        'disallowed': {'key': 'properties.disallowed', 'type': 'Disallowed'},
        'purchase_plan': {'key': 'properties.purchasePlan', 'type': 'ImagePurchasePlan'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, description: str=None, eula: str=None, privacy_statement_uri: str=None, release_note_uri: str=None, os_type=None, os_state=None, end_of_life_date=None, identifier=None, recommended=None, disallowed=None, purchase_plan=None, **kwargs) -> None:
        super(GalleryImage, self).__init__(location=location, tags=tags, **kwargs)
        self.description = description
        self.eula = eula
        self.privacy_statement_uri = privacy_statement_uri
        self.release_note_uri = release_note_uri
        self.os_type = os_type
        self.os_state = os_state
        self.end_of_life_date = end_of_life_date
        self.identifier = identifier
        self.recommended = recommended
        self.disallowed = disallowed
        self.purchase_plan = purchase_plan
        self.provisioning_state = None
