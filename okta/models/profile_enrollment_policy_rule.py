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
from okta.models.policy_rule import PolicyRule  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class ProfileEnrollmentPolicyRule(PolicyRule):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(PolicyRule, "swagger_types"):
        swagger_types.update(PolicyRule.swagger_types)
    swagger_types['actions'] = 'ProfileEnrollmentPolicyRuleActions'
    swagger_types['name'] = 'str'

    attribute_map = {
        'actions': 'actions',
        'name': 'name'
    }
    if hasattr(PolicyRule, "attribute_map"):
        attribute_map.update(PolicyRule.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, actions=None, name=None, **kwargs):  # noqa: E501
        """ProfileEnrollmentPolicyRule - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._actions = None
        self._name = None
        self.discriminator = None
        if actions is not None:
            if hasattr(models, self.swagger_types['actions']):
                nested_class = getattr(models, self.swagger_types['actions'])
                if isinstance(actions, nested_class):
                    self.actions = actions
                elif isinstance(actions, dict):
                    self.actions = nested_class.from_kwargs(**actions)
                else:
                    self.actions = actions
            else:
                self.actions = actions
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
    def actions(self):
        """Gets the actions of this ProfileEnrollmentPolicyRule.  # noqa: E501


        :return: The actions of this ProfileEnrollmentPolicyRule.  # noqa: E501
        :rtype: ProfileEnrollmentPolicyRuleActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ProfileEnrollmentPolicyRule.


        :param actions: The actions of this ProfileEnrollmentPolicyRule.  # noqa: E501
        :type: ProfileEnrollmentPolicyRuleActions
        """

        self._actions = actions

    @property
    def name(self):
        """Gets the name of this ProfileEnrollmentPolicyRule.  # noqa: E501


        :return: The name of this ProfileEnrollmentPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileEnrollmentPolicyRule.


        :param name: The name of this ProfileEnrollmentPolicyRule.  # noqa: E501
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
        if issubclass(ProfileEnrollmentPolicyRule, dict):
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
        if not isinstance(other, ProfileEnrollmentPolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
