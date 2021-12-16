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

from okta.helpers import to_snake_case

class EventHookChannel(object):
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
    swagger_types = {
        'config': 'EventHookChannelConfig',
        'type': 'EventHookChannelType',
        'version': 'str'
    }

    attribute_map = {
        'config': 'config',
        'type': 'type',
        'version': 'version'
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

    def set_attributes(self, config=None, type=None, version=None):  # noqa: E501
        """EventHookChannel - a model defined in Swagger"""  # noqa: E501
        self._config = None
        self._type = None
        self._version = None
        self.discriminator = None
        if config is not None:
            self.config = config
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def config(self):
        """Gets the config of this EventHookChannel.  # noqa: E501


        :return: The config of this EventHookChannel.  # noqa: E501
        :rtype: EventHookChannelConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this EventHookChannel.


        :param config: The config of this EventHookChannel.  # noqa: E501
        :type: EventHookChannelConfig
        """

        self._config = config

    @property
    def type(self):
        """Gets the type of this EventHookChannel.  # noqa: E501


        :return: The type of this EventHookChannel.  # noqa: E501
        :rtype: EventHookChannelType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventHookChannel.


        :param type: The type of this EventHookChannel.  # noqa: E501
        :type: EventHookChannelType
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this EventHookChannel.  # noqa: E501


        :return: The version of this EventHookChannel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EventHookChannel.


        :param version: The version of this EventHookChannel.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(EventHookChannel, dict):
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
        if not isinstance(other, EventHookChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
