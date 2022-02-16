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

class SpCertificate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['x_5_c'] = 'list[str]'

    attribute_map = {
        'x_5_c': 'x5c'
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

    def set_attributes(self, x_5_c=None, **kwargs):  # noqa: E501
        """SpCertificate - a model defined in Swagger"""  # noqa: E501
        self._x_5_c = None
        self.discriminator = None
        if x_5_c is not None:
            if hasattr(models, self.swagger_types['x_5_c']):
                nested_class = getattr(models, self.swagger_types['x_5_c'])
                if isinstance(x_5_c, nested_class):
                    self.x_5_c = x_5_c
                elif isinstance(x_5_c, dict):
                    self.x_5_c = nested_class.from_kwargs(**x_5_c)
                else:
                    self.x_5_c = x_5_c
            else:
                self.x_5_c = x_5_c

    @property
    def x_5_c(self):
        """Gets the x_5_c of this SpCertificate.  # noqa: E501


        :return: The x_5_c of this SpCertificate.  # noqa: E501
        :rtype: list[str]
        """
        return self._x_5_c

    @x_5_c.setter
    def x_5_c(self, x_5_c):
        """Sets the x_5_c of this SpCertificate.


        :param x_5_c: The x_5_c of this SpCertificate.  # noqa: E501
        :type: list[str]
        """

        self._x_5_c = x_5_c

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
        if issubclass(SpCertificate, dict):
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
        if not isinstance(other, SpCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
