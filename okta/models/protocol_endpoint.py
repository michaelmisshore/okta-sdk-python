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

class ProtocolEndpoint(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['binding'] = 'ProtocolEndpointBinding'
    swagger_types['destination'] = 'str'
    swagger_types['type'] = 'ProtocolEndpointType'
    swagger_types['url'] = 'str'

    attribute_map = {
        'binding': 'binding',
        'destination': 'destination',
        'type': 'type',
        'url': 'url'
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

    def set_attributes(self, binding=None, destination=None, type=None, url=None, **kwargs):  # noqa: E501
        """ProtocolEndpoint - a model defined in Swagger"""  # noqa: E501
        self._binding = None
        self._destination = None
        self._type = None
        self._url = None
        self.discriminator = None
        if binding is not None:
            if hasattr(models, self.swagger_types['binding']):
                nested_class = getattr(models, self.swagger_types['binding'])
                if isinstance(binding, nested_class):
                    self.binding = binding
                elif isinstance(binding, dict):
                    self.binding = nested_class.from_kwargs(**binding)
                else:
                    self.binding = binding
            else:
                self.binding = binding
        if destination is not None:
            if hasattr(models, self.swagger_types['destination']):
                nested_class = getattr(models, self.swagger_types['destination'])
                if isinstance(destination, nested_class):
                    self.destination = destination
                elif isinstance(destination, dict):
                    self.destination = nested_class.from_kwargs(**destination)
                else:
                    self.destination = destination
            else:
                self.destination = destination
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
        if url is not None:
            if hasattr(models, self.swagger_types['url']):
                nested_class = getattr(models, self.swagger_types['url'])
                if isinstance(url, nested_class):
                    self.url = url
                elif isinstance(url, dict):
                    self.url = nested_class.from_kwargs(**url)
                else:
                    self.url = url
            else:
                self.url = url

    @property
    def binding(self):
        """Gets the binding of this ProtocolEndpoint.  # noqa: E501


        :return: The binding of this ProtocolEndpoint.  # noqa: E501
        :rtype: ProtocolEndpointBinding
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this ProtocolEndpoint.


        :param binding: The binding of this ProtocolEndpoint.  # noqa: E501
        :type: ProtocolEndpointBinding
        """

        self._binding = binding

    @property
    def destination(self):
        """Gets the destination of this ProtocolEndpoint.  # noqa: E501


        :return: The destination of this ProtocolEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ProtocolEndpoint.


        :param destination: The destination of this ProtocolEndpoint.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def type(self):
        """Gets the type of this ProtocolEndpoint.  # noqa: E501


        :return: The type of this ProtocolEndpoint.  # noqa: E501
        :rtype: ProtocolEndpointType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProtocolEndpoint.


        :param type: The type of this ProtocolEndpoint.  # noqa: E501
        :type: ProtocolEndpointType
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this ProtocolEndpoint.  # noqa: E501


        :return: The url of this ProtocolEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ProtocolEndpoint.


        :param url: The url of this ProtocolEndpoint.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ProtocolEndpoint, dict):
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
        if not isinstance(other, ProtocolEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
