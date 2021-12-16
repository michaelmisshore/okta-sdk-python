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

class LifecycleExpirationPolicyRuleCondition(object):
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
        'lifecycle_status': 'str',
        'number': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'lifecycle_status': 'lifecycleStatus',
        'number': 'number',
        'unit': 'unit'
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

    def set_attributes(self, lifecycle_status=None, number=None, unit=None):  # noqa: E501
        """LifecycleExpirationPolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._lifecycle_status = None
        self._number = None
        self._unit = None
        self.discriminator = None
        if lifecycle_status is not None:
            self.lifecycle_status = lifecycle_status
        if number is not None:
            self.number = number
        if unit is not None:
            self.unit = unit

    @property
    def lifecycle_status(self):
        """Gets the lifecycle_status of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501


        :return: The lifecycle_status of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_status

    @lifecycle_status.setter
    def lifecycle_status(self, lifecycle_status):
        """Sets the lifecycle_status of this LifecycleExpirationPolicyRuleCondition.


        :param lifecycle_status: The lifecycle_status of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501
        :type: str
        """

        self._lifecycle_status = lifecycle_status

    @property
    def number(self):
        """Gets the number of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501


        :return: The number of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this LifecycleExpirationPolicyRuleCondition.


        :param number: The number of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def unit(self):
        """Gets the unit of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501


        :return: The unit of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this LifecycleExpirationPolicyRuleCondition.


        :param unit: The unit of this LifecycleExpirationPolicyRuleCondition.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if issubclass(LifecycleExpirationPolicyRuleCondition, dict):
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
        if not isinstance(other, LifecycleExpirationPolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
