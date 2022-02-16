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

class DevicePolicyRuleCondition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['migrated'] = 'bool'
    swagger_types['platform'] = 'DevicePolicyRuleConditionPlatform'
    swagger_types['rooted'] = 'bool'
    swagger_types['trust_level'] = 'DevicePolicyTrustLevel'

    attribute_map = {
        'migrated': 'migrated',
        'platform': 'platform',
        'rooted': 'rooted',
        'trust_level': 'trustLevel'
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

    def set_attributes(self, migrated=None, platform=None, rooted=None, trust_level=None, **kwargs):  # noqa: E501
        """DevicePolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._migrated = None
        self._platform = None
        self._rooted = None
        self._trust_level = None
        self.discriminator = None
        if migrated is not None:
            if hasattr(models, self.swagger_types['migrated']):
                nested_class = getattr(models, self.swagger_types['migrated'])
                if isinstance(migrated, nested_class):
                    self.migrated = migrated
                elif isinstance(migrated, dict):
                    self.migrated = nested_class.from_kwargs(**migrated)
                else:
                    self.migrated = migrated
            else:
                self.migrated = migrated
        if platform is not None:
            if hasattr(models, self.swagger_types['platform']):
                nested_class = getattr(models, self.swagger_types['platform'])
                if isinstance(platform, nested_class):
                    self.platform = platform
                elif isinstance(platform, dict):
                    self.platform = nested_class.from_kwargs(**platform)
                else:
                    self.platform = platform
            else:
                self.platform = platform
        if rooted is not None:
            if hasattr(models, self.swagger_types['rooted']):
                nested_class = getattr(models, self.swagger_types['rooted'])
                if isinstance(rooted, nested_class):
                    self.rooted = rooted
                elif isinstance(rooted, dict):
                    self.rooted = nested_class.from_kwargs(**rooted)
                else:
                    self.rooted = rooted
            else:
                self.rooted = rooted
        if trust_level is not None:
            if hasattr(models, self.swagger_types['trust_level']):
                nested_class = getattr(models, self.swagger_types['trust_level'])
                if isinstance(trust_level, nested_class):
                    self.trust_level = trust_level
                elif isinstance(trust_level, dict):
                    self.trust_level = nested_class.from_kwargs(**trust_level)
                else:
                    self.trust_level = trust_level
            else:
                self.trust_level = trust_level

    @property
    def migrated(self):
        """Gets the migrated of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The migrated of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: bool
        """
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        """Sets the migrated of this DevicePolicyRuleCondition.


        :param migrated: The migrated of this DevicePolicyRuleCondition.  # noqa: E501
        :type: bool
        """

        self._migrated = migrated

    @property
    def platform(self):
        """Gets the platform of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The platform of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: DevicePolicyRuleConditionPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DevicePolicyRuleCondition.


        :param platform: The platform of this DevicePolicyRuleCondition.  # noqa: E501
        :type: DevicePolicyRuleConditionPlatform
        """

        self._platform = platform

    @property
    def rooted(self):
        """Gets the rooted of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The rooted of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: bool
        """
        return self._rooted

    @rooted.setter
    def rooted(self, rooted):
        """Sets the rooted of this DevicePolicyRuleCondition.


        :param rooted: The rooted of this DevicePolicyRuleCondition.  # noqa: E501
        :type: bool
        """

        self._rooted = rooted

    @property
    def trust_level(self):
        """Gets the trust_level of this DevicePolicyRuleCondition.  # noqa: E501


        :return: The trust_level of this DevicePolicyRuleCondition.  # noqa: E501
        :rtype: DevicePolicyTrustLevel
        """
        return self._trust_level

    @trust_level.setter
    def trust_level(self, trust_level):
        """Sets the trust_level of this DevicePolicyRuleCondition.


        :param trust_level: The trust_level of this DevicePolicyRuleCondition.  # noqa: E501
        :type: DevicePolicyTrustLevel
        """

        self._trust_level = trust_level

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
        if issubclass(DevicePolicyRuleCondition, dict):
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
        if not isinstance(other, DevicePolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
