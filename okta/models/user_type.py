# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.10.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class UserType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['created'] = 'datetime'
    swagger_types['created_by'] = 'str'
    swagger_types['default'] = 'bool'
    swagger_types['description'] = 'str'
    swagger_types['display_name'] = 'str'
    swagger_types['id'] = 'str'
    swagger_types['last_updated'] = 'datetime'
    swagger_types['last_updated_by'] = 'str'
    swagger_types['name'] = 'str'

    attribute_map = {
        'links': '_links',
        'created': 'created',
        'created_by': 'createdBy',
        'default': 'default',
        'description': 'description',
        'display_name': 'displayName',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'last_updated_by': 'lastUpdatedBy',
        'name': 'name'
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

    def set_attributes(self, links=None, created=None, created_by=None, default=None, description=None, display_name=None, id=None, last_updated=None, last_updated_by=None, name=None, **kwargs):  # noqa: E501
        """UserType - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._created = None
        self._created_by = None
        self._default = None
        self._description = None
        self._display_name = None
        self._id = None
        self._last_updated = None
        self._last_updated_by = None
        self._name = None
        self.discriminator = None
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
        if created_by is not None:
            if hasattr(models, self.swagger_types['created_by']):
                nested_class = getattr(models, self.swagger_types['created_by'])
                if isinstance(created_by, nested_class):
                    self.created_by = created_by
                elif isinstance(created_by, dict):
                    self.created_by = nested_class.from_kwargs(**created_by)
                else:
                    self.created_by = created_by
            else:
                self.created_by = created_by
        if default is not None:
            if hasattr(models, self.swagger_types['default']):
                nested_class = getattr(models, self.swagger_types['default'])
                if isinstance(default, nested_class):
                    self.default = default
                elif isinstance(default, dict):
                    self.default = nested_class.from_kwargs(**default)
                else:
                    self.default = default
            else:
                self.default = default
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
        if display_name is not None:
            if hasattr(models, self.swagger_types['display_name']):
                nested_class = getattr(models, self.swagger_types['display_name'])
                if isinstance(display_name, nested_class):
                    self.display_name = display_name
                elif isinstance(display_name, dict):
                    self.display_name = nested_class.from_kwargs(**display_name)
                else:
                    self.display_name = display_name
            else:
                self.display_name = display_name
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
        if last_updated_by is not None:
            if hasattr(models, self.swagger_types['last_updated_by']):
                nested_class = getattr(models, self.swagger_types['last_updated_by'])
                if isinstance(last_updated_by, nested_class):
                    self.last_updated_by = last_updated_by
                elif isinstance(last_updated_by, dict):
                    self.last_updated_by = nested_class.from_kwargs(**last_updated_by)
                else:
                    self.last_updated_by = last_updated_by
            else:
                self.last_updated_by = last_updated_by
        if name is not None:
            if hasattr(models, self.swagger_types['name']):
                nested_class = getattr(models, self.swagger_types['name'])
                if isinstance(name, nested_class):
                    self.name = name
                elif isinstance(name, dict):
                    self.name = nested_class.from_kwargs(**name)
                else:
                    self.name = name
            else:
                self.name = name

    @property
    def links(self):
        """Gets the links of this UserType.  # noqa: E501


        :return: The links of this UserType.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserType.


        :param links: The links of this UserType.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this UserType.  # noqa: E501


        :return: The created of this UserType.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserType.


        :param created: The created of this UserType.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this UserType.  # noqa: E501


        :return: The created_by of this UserType.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UserType.


        :param created_by: The created_by of this UserType.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def default(self):
        """Gets the default of this UserType.  # noqa: E501


        :return: The default of this UserType.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this UserType.


        :param default: The default of this UserType.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this UserType.  # noqa: E501


        :return: The description of this UserType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserType.


        :param description: The description of this UserType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this UserType.  # noqa: E501


        :return: The display_name of this UserType.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserType.


        :param display_name: The display_name of this UserType.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this UserType.  # noqa: E501


        :return: The id of this UserType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserType.


        :param id: The id of this UserType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this UserType.  # noqa: E501


        :return: The last_updated of this UserType.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this UserType.


        :param last_updated: The last_updated of this UserType.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this UserType.  # noqa: E501


        :return: The last_updated_by of this UserType.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this UserType.


        :param last_updated_by: The last_updated_by of this UserType.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def name(self):
        """Gets the name of this UserType.  # noqa: E501


        :return: The name of this UserType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserType.


        :param name: The name of this UserType.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(UserType, dict):
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
        if not isinstance(other, UserType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
