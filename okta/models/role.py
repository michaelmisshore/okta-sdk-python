# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class Role(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['embedded'] = 'dict(str, object)'
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['assignment_type'] = 'RoleAssignmentType'
    swagger_types['created'] = 'datetime'
    swagger_types['description'] = 'str'
    swagger_types['id'] = 'str'
    swagger_types['label'] = 'str'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['status'] = 'LifecycleStatus'
    swagger_types['type'] = 'RoleType'

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'assignment_type': 'assignmentType',
        'created': 'created',
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'last_updated': 'lastUpdated',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, embedded=None, links=None, assignment_type=None, created=None, description=None, id=None, label=None, last_updated=None, status=None, type=None, **kwargs):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._assignment_type = None
        self._created = None
        self._description = None
        self._id = None
        self._label = None
        self._last_updated = None
        self._status = None
        self._type = None
        self.discriminator = None
        if embedded is not None:
            if hasattr(models, self.swagger_types['embedded']):
                nested_class = getattr(models, self.swagger_types['embedded'])
                if isinstance(embedded, nested_class):
                    self.embedded = embedded
                elif isinstance(embedded, dict):
                    self.embedded = nested_class.from_kwargs(**embedded)
                else:
                    self.embedded = embedded
            else:
                self.embedded = embedded
        if links is not None:
            if hasattr(models, self.swagger_types['links']):
                nested_class = getattr(models, self.swagger_types['links'])
                if isinstance(links, nested_class):
                    self.links = links
                elif isinstance(links, dict):
                    self.links = nested_class.from_kwargs(**links)
                else:
                    self.links = links
            else:
                self.links = links
        if assignment_type is not None:
            if hasattr(models, self.swagger_types['assignment_type']):
                nested_class = getattr(models, self.swagger_types['assignment_type'])
                if isinstance(assignment_type, nested_class):
                    self.assignment_type = assignment_type
                elif isinstance(assignment_type, dict):
                    self.assignment_type = nested_class.from_kwargs(**assignment_type)
                else:
                    self.assignment_type = assignment_type
            else:
                self.assignment_type = assignment_type
        if created is not None:
            if hasattr(models, self.swagger_types['created']):
                nested_class = getattr(models, self.swagger_types['created'])
                if isinstance(created, nested_class):
                    self.created = created
                elif isinstance(created, dict):
                    self.created = nested_class.from_kwargs(**created)
                else:
                    self.created = created
            else:
                self.created = created
        if description is not None:
            if hasattr(models, self.swagger_types['description']):
                nested_class = getattr(models, self.swagger_types['description'])
                if isinstance(description, nested_class):
                    self.description = description
                elif isinstance(description, dict):
                    self.description = nested_class.from_kwargs(**description)
                else:
                    self.description = description
            else:
                self.description = description
        if id is not None:
            if hasattr(models, self.swagger_types['id']):
                nested_class = getattr(models, self.swagger_types['id'])
                if isinstance(id, nested_class):
                    self.id = id
                elif isinstance(id, dict):
                    self.id = nested_class.from_kwargs(**id)
                else:
                    self.id = id
            else:
                self.id = id
        if label is not None:
            if hasattr(models, self.swagger_types['label']):
                nested_class = getattr(models, self.swagger_types['label'])
                if isinstance(label, nested_class):
                    self.label = label
                elif isinstance(label, dict):
                    self.label = nested_class.from_kwargs(**label)
                else:
                    self.label = label
            else:
                self.label = label
        if last_updated is not None:
            if hasattr(models, self.swagger_types['last_updated']):
                nested_class = getattr(models, self.swagger_types['last_updated'])
                if isinstance(last_updated, nested_class):
                    self.last_updated = last_updated
                elif isinstance(last_updated, dict):
                    self.last_updated = nested_class.from_kwargs(**last_updated)
                else:
                    self.last_updated = last_updated
            else:
                self.last_updated = last_updated
        if status is not None:
            if hasattr(models, self.swagger_types['status']):
                nested_class = getattr(models, self.swagger_types['status'])
                if isinstance(status, nested_class):
                    self.status = status
                elif isinstance(status, dict):
                    self.status = nested_class.from_kwargs(**status)
                else:
                    self.status = status
            else:
                self.status = status
        if type is not None:
            if hasattr(models, self.swagger_types['type']):
                nested_class = getattr(models, self.swagger_types['type'])
                if isinstance(type, nested_class):
                    self.type = type
                elif isinstance(type, dict):
                    self.type = nested_class.from_kwargs(**type)
                else:
                    self.type = type
            else:
                self.type = type

    @property
    def embedded(self):
        """Gets the embedded of this Role.  # noqa: E501


        :return: The embedded of this Role.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Role.


        :param embedded: The embedded of this Role.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this Role.  # noqa: E501


        :return: The links of this Role.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Role.


        :param links: The links of this Role.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def assignment_type(self):
        """Gets the assignment_type of this Role.  # noqa: E501


        :return: The assignment_type of this Role.  # noqa: E501
        :rtype: RoleAssignmentType
        """
        return self._assignment_type

    @assignment_type.setter
    def assignment_type(self, assignment_type):
        """Sets the assignment_type of this Role.


        :param assignment_type: The assignment_type of this Role.  # noqa: E501
        :type: RoleAssignmentType
        """

        self._assignment_type = assignment_type

    @property
    def created(self):
        """Gets the created of this Role.  # noqa: E501


        :return: The created of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Role.


        :param created: The created of this Role.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this Role.  # noqa: E501


        :return: The description of this Role.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.


        :param description: The description of this Role.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501


        :return: The id of this Role.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.


        :param id: The id of this Role.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Role.  # noqa: E501


        :return: The label of this Role.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Role.


        :param label: The label of this Role.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def last_updated(self):
        """Gets the last_updated of this Role.  # noqa: E501


        :return: The last_updated of this Role.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Role.


        :param last_updated: The last_updated of this Role.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def status(self):
        """Gets the status of this Role.  # noqa: E501


        :return: The status of this Role.  # noqa: E501
        :rtype: LifecycleStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Role.


        :param status: The status of this Role.  # noqa: E501
        :type: LifecycleStatus
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this Role.  # noqa: E501


        :return: The type of this Role.  # noqa: E501
        :rtype: RoleType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Role.


        :param type: The type of this Role.  # noqa: E501
        :type: RoleType
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Role, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other