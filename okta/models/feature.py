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

class Feature(object):
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
    swagger_types['links'] = 'dict(str, object)'
    swagger_types['description'] = 'str'
    swagger_types['id'] = 'str'
    swagger_types['name'] = 'str'
    swagger_types['stage'] = 'FeatureStage'
    swagger_types['status'] = 'EnabledStatus'
    swagger_types['type'] = 'FeatureType'

    attribute_map = {
        'links': '_links',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'stage': 'stage',
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

    def set_attributes(self, links=None, description=None, id=None, name=None, stage=None, status=None, type=None, **kwargs):  # noqa: E501
        """Feature - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._description = None
        self._id = None
        self._name = None
        self._stage = None
        self._status = None
        self._type = None
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
        if stage is not None:
            if hasattr(models, self.swagger_types['stage']):
                nested_class = getattr(models, self.swagger_types['stage'])
                if isinstance(stage, nested_class):
                    self.stage = stage
                elif isinstance(stage, dict):
                    self.stage = nested_class.from_kwargs(**stage)
                else:
                    self.stage = stage
            else:
                self.stage = stage
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
    def links(self):
        """Gets the links of this Feature.  # noqa: E501


        :return: The links of this Feature.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Feature.


        :param links: The links of this Feature.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def description(self):
        """Gets the description of this Feature.  # noqa: E501


        :return: The description of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Feature.


        :param description: The description of this Feature.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Feature.  # noqa: E501


        :return: The id of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Feature.


        :param id: The id of this Feature.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Feature.  # noqa: E501


        :return: The name of this Feature.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Feature.


        :param name: The name of this Feature.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def stage(self):
        """Gets the stage of this Feature.  # noqa: E501


        :return: The stage of this Feature.  # noqa: E501
        :rtype: FeatureStage
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this Feature.


        :param stage: The stage of this Feature.  # noqa: E501
        :type: FeatureStage
        """

        self._stage = stage

    @property
    def status(self):
        """Gets the status of this Feature.  # noqa: E501


        :return: The status of this Feature.  # noqa: E501
        :rtype: EnabledStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Feature.


        :param status: The status of this Feature.  # noqa: E501
        :type: EnabledStatus
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this Feature.  # noqa: E501


        :return: The type of this Feature.  # noqa: E501
        :rtype: FeatureType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Feature.


        :param type: The type of this Feature.  # noqa: E501
        :type: FeatureType
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
        if issubclass(Feature, dict):
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
        if not isinstance(other, Feature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other