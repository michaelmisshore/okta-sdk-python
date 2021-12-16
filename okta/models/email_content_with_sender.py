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
from okta.models.email_content import EmailContent  # noqa: F401,E501

from okta.helpers import to_snake_case

class EmailContentWithSender(EmailContent):
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
        'from_address': 'str',
        'from_name': 'str'
    }
    if hasattr(EmailContent, "swagger_types"):
        swagger_types.update(EmailContent.swagger_types)

    attribute_map = {
        'from_address': 'fromAddress',
        'from_name': 'fromName'
    }
    if hasattr(EmailContent, "attribute_map"):
        attribute_map.update(EmailContent.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, from_address=None, from_name=None, *args, **kwargs):  # noqa: E501
        """EmailContentWithSender - a model defined in Swagger"""  # noqa: E501
        self._from_address = None
        self._from_name = None
        self.discriminator = None
        self.from_address = from_address
        self.from_name = from_name
        super().set_attributes(*args, **kwargs)

    @property
    def from_address(self):
        """Gets the from_address of this EmailContentWithSender.  # noqa: E501


        :return: The from_address of this EmailContentWithSender.  # noqa: E501
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this EmailContentWithSender.


        :param from_address: The from_address of this EmailContentWithSender.  # noqa: E501
        :type: str
        """
        if from_address is None:
            raise ValueError("Invalid value for `from_address`, must not be `None`")  # noqa: E501

        self._from_address = from_address

    @property
    def from_name(self):
        """Gets the from_name of this EmailContentWithSender.  # noqa: E501


        :return: The from_name of this EmailContentWithSender.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this EmailContentWithSender.


        :param from_name: The from_name of this EmailContentWithSender.  # noqa: E501
        :type: str
        """
        if from_name is None:
            raise ValueError("Invalid value for `from_name`, must not be `None`")  # noqa: E501

        self._from_name = from_name

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
        if issubclass(EmailContentWithSender, dict):
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
        if not isinstance(other, EmailContentWithSender):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
