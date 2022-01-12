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

class UserPolicyRuleCondition(object):
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
    swagger_types['exclude'] = 'list[str]'
    swagger_types['inactivity'] = 'InactivityPolicyRuleCondition'
    swagger_types['include'] = 'list[str]'
    swagger_types['lifecycle_expiration'] = 'LifecycleExpirationPolicyRuleCondition'
    swagger_types['password_expiration'] = 'PasswordExpirationPolicyRuleCondition'
    swagger_types['user_lifecycle_attribute'] = 'UserLifecycleAttributePolicyRuleCondition'

    attribute_map = {
        'exclude': 'exclude',
        'inactivity': 'inactivity',
        'include': 'include',
        'lifecycle_expiration': 'lifecycleExpiration',
        'password_expiration': 'passwordExpiration',
        'user_lifecycle_attribute': 'userLifecycleAttribute'
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

    def set_attributes(self, exclude=None, inactivity=None, include=None, lifecycle_expiration=None, password_expiration=None, user_lifecycle_attribute=None, **kwargs):  # noqa: E501
        """UserPolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._exclude = None
        self._inactivity = None
        self._include = None
        self._lifecycle_expiration = None
        self._password_expiration = None
        self._user_lifecycle_attribute = None
        self.discriminator = None
        if exclude is not None:
            if hasattr(models, self.swagger_types['exclude']):
                nested_class = getattr(models, self.swagger_types['exclude'])
                if isinstance(exclude, nested_class):
                    self.exclude = exclude
                elif isinstance(exclude, dict):
                    self.exclude = nested_class.from_kwargs(**exclude)
                else:
                    self.exclude = exclude
            else:
                self.exclude = exclude
        if inactivity is not None:
            if hasattr(models, self.swagger_types['inactivity']):
                nested_class = getattr(models, self.swagger_types['inactivity'])
                if isinstance(inactivity, nested_class):
                    self.inactivity = inactivity
                elif isinstance(inactivity, dict):
                    self.inactivity = nested_class.from_kwargs(**inactivity)
                else:
                    self.inactivity = inactivity
            else:
                self.inactivity = inactivity
        if include is not None:
            if hasattr(models, self.swagger_types['include']):
                nested_class = getattr(models, self.swagger_types['include'])
                if isinstance(include, nested_class):
                    self.include = include
                elif isinstance(include, dict):
                    self.include = nested_class.from_kwargs(**include)
                else:
                    self.include = include
            else:
                self.include = include
        if lifecycle_expiration is not None:
            if hasattr(models, self.swagger_types['lifecycle_expiration']):
                nested_class = getattr(models, self.swagger_types['lifecycle_expiration'])
                if isinstance(lifecycle_expiration, nested_class):
                    self.lifecycle_expiration = lifecycle_expiration
                elif isinstance(lifecycle_expiration, dict):
                    self.lifecycle_expiration = nested_class.from_kwargs(**lifecycle_expiration)
                else:
                    self.lifecycle_expiration = lifecycle_expiration
            else:
                self.lifecycle_expiration = lifecycle_expiration
        if password_expiration is not None:
            if hasattr(models, self.swagger_types['password_expiration']):
                nested_class = getattr(models, self.swagger_types['password_expiration'])
                if isinstance(password_expiration, nested_class):
                    self.password_expiration = password_expiration
                elif isinstance(password_expiration, dict):
                    self.password_expiration = nested_class.from_kwargs(**password_expiration)
                else:
                    self.password_expiration = password_expiration
            else:
                self.password_expiration = password_expiration
        if user_lifecycle_attribute is not None:
            if hasattr(models, self.swagger_types['user_lifecycle_attribute']):
                nested_class = getattr(models, self.swagger_types['user_lifecycle_attribute'])
                if isinstance(user_lifecycle_attribute, nested_class):
                    self.user_lifecycle_attribute = user_lifecycle_attribute
                elif isinstance(user_lifecycle_attribute, dict):
                    self.user_lifecycle_attribute = nested_class.from_kwargs(**user_lifecycle_attribute)
                else:
                    self.user_lifecycle_attribute = user_lifecycle_attribute
            else:
                self.user_lifecycle_attribute = user_lifecycle_attribute

    @property
    def exclude(self):
        """Gets the exclude of this UserPolicyRuleCondition.  # noqa: E501


        :return: The exclude of this UserPolicyRuleCondition.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this UserPolicyRuleCondition.


        :param exclude: The exclude of this UserPolicyRuleCondition.  # noqa: E501
        :type: list[str]
        """

        self._exclude = exclude

    @property
    def inactivity(self):
        """Gets the inactivity of this UserPolicyRuleCondition.  # noqa: E501


        :return: The inactivity of this UserPolicyRuleCondition.  # noqa: E501
        :rtype: InactivityPolicyRuleCondition
        """
        return self._inactivity

    @inactivity.setter
    def inactivity(self, inactivity):
        """Sets the inactivity of this UserPolicyRuleCondition.


        :param inactivity: The inactivity of this UserPolicyRuleCondition.  # noqa: E501
        :type: InactivityPolicyRuleCondition
        """

        self._inactivity = inactivity

    @property
    def include(self):
        """Gets the include of this UserPolicyRuleCondition.  # noqa: E501


        :return: The include of this UserPolicyRuleCondition.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this UserPolicyRuleCondition.


        :param include: The include of this UserPolicyRuleCondition.  # noqa: E501
        :type: list[str]
        """

        self._include = include

    @property
    def lifecycle_expiration(self):
        """Gets the lifecycle_expiration of this UserPolicyRuleCondition.  # noqa: E501


        :return: The lifecycle_expiration of this UserPolicyRuleCondition.  # noqa: E501
        :rtype: LifecycleExpirationPolicyRuleCondition
        """
        return self._lifecycle_expiration

    @lifecycle_expiration.setter
    def lifecycle_expiration(self, lifecycle_expiration):
        """Sets the lifecycle_expiration of this UserPolicyRuleCondition.


        :param lifecycle_expiration: The lifecycle_expiration of this UserPolicyRuleCondition.  # noqa: E501
        :type: LifecycleExpirationPolicyRuleCondition
        """

        self._lifecycle_expiration = lifecycle_expiration

    @property
    def password_expiration(self):
        """Gets the password_expiration of this UserPolicyRuleCondition.  # noqa: E501


        :return: The password_expiration of this UserPolicyRuleCondition.  # noqa: E501
        :rtype: PasswordExpirationPolicyRuleCondition
        """
        return self._password_expiration

    @password_expiration.setter
    def password_expiration(self, password_expiration):
        """Sets the password_expiration of this UserPolicyRuleCondition.


        :param password_expiration: The password_expiration of this UserPolicyRuleCondition.  # noqa: E501
        :type: PasswordExpirationPolicyRuleCondition
        """

        self._password_expiration = password_expiration

    @property
    def user_lifecycle_attribute(self):
        """Gets the user_lifecycle_attribute of this UserPolicyRuleCondition.  # noqa: E501


        :return: The user_lifecycle_attribute of this UserPolicyRuleCondition.  # noqa: E501
        :rtype: UserLifecycleAttributePolicyRuleCondition
        """
        return self._user_lifecycle_attribute

    @user_lifecycle_attribute.setter
    def user_lifecycle_attribute(self, user_lifecycle_attribute):
        """Sets the user_lifecycle_attribute of this UserPolicyRuleCondition.


        :param user_lifecycle_attribute: The user_lifecycle_attribute of this UserPolicyRuleCondition.  # noqa: E501
        :type: UserLifecycleAttributePolicyRuleCondition
        """

        self._user_lifecycle_attribute = user_lifecycle_attribute

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
        if issubclass(UserPolicyRuleCondition, dict):
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
        if not isinstance(other, UserPolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other