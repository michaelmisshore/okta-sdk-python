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
from okta.models.policy_rule_actions import PolicyRuleActions  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class AccessPolicyRuleActions(PolicyRuleActions):
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
    if hasattr(PolicyRuleActions, "swagger_types"):
        swagger_types.update(PolicyRuleActions.swagger_types)
    swagger_types['app_sign_on'] = 'AccessPolicyRuleApplicationSignOn'

    attribute_map = {
        'app_sign_on': 'appSignOn'
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

    def set_attributes(self, app_sign_on=None, **kwargs):  # noqa: E501
        """AccessPolicyRuleActions - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._app_sign_on = None
        self.discriminator = None
        if app_sign_on is not None:
            if hasattr(models, self.swagger_types['app_sign_on']):
                nested_class = getattr(models, self.swagger_types['app_sign_on'])
                if isinstance(app_sign_on, nested_class):
                    self.app_sign_on = app_sign_on
                elif isinstance(app_sign_on, dict):
                    self.app_sign_on = nested_class.from_kwargs(**app_sign_on)
                else:
                    self.app_sign_on = app_sign_on
            else:
                self.app_sign_on = app_sign_on

    @property
    def app_sign_on(self):
        """Gets the app_sign_on of this AccessPolicyRuleActions.  # noqa: E501


        :return: The app_sign_on of this AccessPolicyRuleActions.  # noqa: E501
        :rtype: AccessPolicyRuleApplicationSignOn
        """
        return self._app_sign_on

    @app_sign_on.setter
    def app_sign_on(self, app_sign_on):
        """Sets the app_sign_on of this AccessPolicyRuleActions.


        :param app_sign_on: The app_sign_on of this AccessPolicyRuleActions.  # noqa: E501
        :type: AccessPolicyRuleApplicationSignOn
        """

        self._app_sign_on = app_sign_on

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
        if issubclass(AccessPolicyRuleActions, dict):
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
        if not isinstance(other, AccessPolicyRuleActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other