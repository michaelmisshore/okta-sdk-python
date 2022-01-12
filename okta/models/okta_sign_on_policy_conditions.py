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
from okta.models.policy_rule_conditions import PolicyRuleConditions  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class OktaSignOnPolicyConditions(PolicyRuleConditions):
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
    if hasattr(PolicyRuleConditions, "swagger_types"):
        swagger_types.update(PolicyRuleConditions.swagger_types)
    swagger_types['people'] = 'PolicyPeopleCondition'

    attribute_map = {
        'people': 'people'
    }
    if hasattr(PolicyRuleConditions, "attribute_map"):
        attribute_map.update(PolicyRuleConditions.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, people=None, **kwargs):  # noqa: E501
        """OktaSignOnPolicyConditions - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._people = None
        self.discriminator = None
        if people is not None:
            if hasattr(models, self.swagger_types['people']):
                nested_class = getattr(models, self.swagger_types['people'])
                if isinstance(people, nested_class):
                    self.people = people
                elif isinstance(people, dict):
                    self.people = nested_class.from_kwargs(**people)
                else:
                    self.people = people
            else:
                self.people = people

    @property
    def people(self):
        """Gets the people of this OktaSignOnPolicyConditions.  # noqa: E501


        :return: The people of this OktaSignOnPolicyConditions.  # noqa: E501
        :rtype: PolicyPeopleCondition
        """
        return self._people

    @people.setter
    def people(self, people):
        """Sets the people of this OktaSignOnPolicyConditions.


        :param people: The people of this OktaSignOnPolicyConditions.  # noqa: E501
        :type: PolicyPeopleCondition
        """

        self._people = people

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
        if issubclass(OktaSignOnPolicyConditions, dict):
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
        if not isinstance(other, OktaSignOnPolicyConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other