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
from okta.models.policy_rule_actions import PolicyRuleActions  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class PasswordPolicyRuleActions(PolicyRuleActions):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(PolicyRuleActions, "swagger_types"):
        swagger_types.update(PolicyRuleActions.swagger_types)
    swagger_types['password_change'] = 'PasswordPolicyRuleAction'
    swagger_types['self_service_password_reset'] = 'PasswordPolicyRuleAction'
    swagger_types['self_service_unlock'] = 'PasswordPolicyRuleAction'

    attribute_map = {
        'password_change': 'passwordChange',
        'self_service_password_reset': 'selfServicePasswordReset',
        'self_service_unlock': 'selfServiceUnlock'
    }
    if hasattr(PolicyRuleActions, "attribute_map"):
        attribute_map.update(PolicyRuleActions.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, password_change=None, self_service_password_reset=None, self_service_unlock=None, **kwargs):  # noqa: E501
        """PasswordPolicyRuleActions - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._password_change = None
        self._self_service_password_reset = None
        self._self_service_unlock = None
        self.discriminator = None
        if password_change is not None:
            if hasattr(models, self.swagger_types['password_change']):
                nested_class = getattr(models, self.swagger_types['password_change'])
                if isinstance(password_change, nested_class):
                    self.password_change = password_change
                elif isinstance(password_change, dict):
                    self.password_change = nested_class.from_kwargs(**password_change)
                else:
                    self.password_change = password_change
            else:
                self.password_change = password_change
        if self_service_password_reset is not None:
            if hasattr(models, self.swagger_types['self_service_password_reset']):
                nested_class = getattr(models, self.swagger_types['self_service_password_reset'])
                if isinstance(self_service_password_reset, nested_class):
                    self.self_service_password_reset = self_service_password_reset
                elif isinstance(self_service_password_reset, dict):
                    self.self_service_password_reset = nested_class.from_kwargs(**self_service_password_reset)
                else:
                    self.self_service_password_reset = self_service_password_reset
            else:
                self.self_service_password_reset = self_service_password_reset
        if self_service_unlock is not None:
            if hasattr(models, self.swagger_types['self_service_unlock']):
                nested_class = getattr(models, self.swagger_types['self_service_unlock'])
                if isinstance(self_service_unlock, nested_class):
                    self.self_service_unlock = self_service_unlock
                elif isinstance(self_service_unlock, dict):
                    self.self_service_unlock = nested_class.from_kwargs(**self_service_unlock)
                else:
                    self.self_service_unlock = self_service_unlock
            else:
                self.self_service_unlock = self_service_unlock

    @property
    def password_change(self):
        """Gets the password_change of this PasswordPolicyRuleActions.  # noqa: E501


        :return: The password_change of this PasswordPolicyRuleActions.  # noqa: E501
        :rtype: PasswordPolicyRuleAction
        """
        return self._password_change

    @password_change.setter
    def password_change(self, password_change):
        """Sets the password_change of this PasswordPolicyRuleActions.


        :param password_change: The password_change of this PasswordPolicyRuleActions.  # noqa: E501
        :type: PasswordPolicyRuleAction
        """

        self._password_change = password_change

    @property
    def self_service_password_reset(self):
        """Gets the self_service_password_reset of this PasswordPolicyRuleActions.  # noqa: E501


        :return: The self_service_password_reset of this PasswordPolicyRuleActions.  # noqa: E501
        :rtype: PasswordPolicyRuleAction
        """
        return self._self_service_password_reset

    @self_service_password_reset.setter
    def self_service_password_reset(self, self_service_password_reset):
        """Sets the self_service_password_reset of this PasswordPolicyRuleActions.


        :param self_service_password_reset: The self_service_password_reset of this PasswordPolicyRuleActions.  # noqa: E501
        :type: PasswordPolicyRuleAction
        """

        self._self_service_password_reset = self_service_password_reset

    @property
    def self_service_unlock(self):
        """Gets the self_service_unlock of this PasswordPolicyRuleActions.  # noqa: E501


        :return: The self_service_unlock of this PasswordPolicyRuleActions.  # noqa: E501
        :rtype: PasswordPolicyRuleAction
        """
        return self._self_service_unlock

    @self_service_unlock.setter
    def self_service_unlock(self, self_service_unlock):
        """Sets the self_service_unlock of this PasswordPolicyRuleActions.


        :param self_service_unlock: The self_service_unlock of this PasswordPolicyRuleActions.  # noqa: E501
        :type: PasswordPolicyRuleAction
        """

        self._self_service_unlock = self_service_unlock

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
        if issubclass(PasswordPolicyRuleActions, dict):
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
        if not isinstance(other, PasswordPolicyRuleActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
