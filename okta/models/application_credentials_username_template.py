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

class ApplicationCredentialsUsernameTemplate(object):
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
        'push_status': 'str',
        'suffix': 'str',
        'template': 'str',
        'type': 'str'
    }

    attribute_map = {
        'push_status': 'pushStatus',
        'suffix': 'suffix',
        'template': 'template',
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

    def set_attributes(self, push_status=None, suffix=None, template=None, type=None):  # noqa: E501
        """ApplicationCredentialsUsernameTemplate - a model defined in Swagger"""  # noqa: E501
        self._push_status = None
        self._suffix = None
        self._template = None
        self._type = None
        self.discriminator = None
        if push_status is not None:
            self.push_status = push_status
        if suffix is not None:
            self.suffix = suffix
        if template is not None:
            self.template = template
        if type is not None:
            self.type = type

    @property
    def push_status(self):
        """Gets the push_status of this ApplicationCredentialsUsernameTemplate.  # noqa: E501


        :return: The push_status of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :rtype: str
        """
        return self._push_status

    @push_status.setter
    def push_status(self, push_status):
        """Sets the push_status of this ApplicationCredentialsUsernameTemplate.


        :param push_status: The push_status of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :type: str
        """

        self._push_status = push_status

    @property
    def suffix(self):
        """Gets the suffix of this ApplicationCredentialsUsernameTemplate.  # noqa: E501


        :return: The suffix of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this ApplicationCredentialsUsernameTemplate.


        :param suffix: The suffix of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

    @property
    def template(self):
        """Gets the template of this ApplicationCredentialsUsernameTemplate.  # noqa: E501


        :return: The template of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ApplicationCredentialsUsernameTemplate.


        :param template: The template of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def type(self):
        """Gets the type of this ApplicationCredentialsUsernameTemplate.  # noqa: E501


        :return: The type of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApplicationCredentialsUsernameTemplate.


        :param type: The type of this ApplicationCredentialsUsernameTemplate.  # noqa: E501
        :type: str
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
        if issubclass(ApplicationCredentialsUsernameTemplate, dict):
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
        if not isinstance(other, ApplicationCredentialsUsernameTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
