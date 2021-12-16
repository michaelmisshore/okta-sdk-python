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

class ProfileEnrollmentPolicyRuleAction(object):
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
        'access': 'str',
        'activation_requirements': 'ProfileEnrollmentPolicyRuleActivationRequirement',
        'pre_registration_inline_hooks': 'list[PreRegistrationInlineHook]',
        'profile_attributes': 'list[ProfileEnrollmentPolicyRuleProfileAttribute]',
        'target_group_ids': 'list[str]',
        'unknown_user_action': 'str'
    }

    attribute_map = {
        'access': 'access',
        'activation_requirements': 'activationRequirements',
        'pre_registration_inline_hooks': 'preRegistrationInlineHooks',
        'profile_attributes': 'profileAttributes',
        'target_group_ids': 'targetGroupIds',
        'unknown_user_action': 'unknownUserAction'
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

    def set_attributes(self, access=None, activation_requirements=None, pre_registration_inline_hooks=None, profile_attributes=None, target_group_ids=None, unknown_user_action=None):  # noqa: E501
        """ProfileEnrollmentPolicyRuleAction - a model defined in Swagger"""  # noqa: E501
        self._access = None
        self._activation_requirements = None
        self._pre_registration_inline_hooks = None
        self._profile_attributes = None
        self._target_group_ids = None
        self._unknown_user_action = None
        self.discriminator = None
        if access is not None:
            self.access = access
        if activation_requirements is not None:
            self.activation_requirements = activation_requirements
        if pre_registration_inline_hooks is not None:
            self.pre_registration_inline_hooks = pre_registration_inline_hooks
        if profile_attributes is not None:
            self.profile_attributes = profile_attributes
        if target_group_ids is not None:
            self.target_group_ids = target_group_ids
        if unknown_user_action is not None:
            self.unknown_user_action = unknown_user_action

    @property
    def access(self):
        """Gets the access of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501


        :return: The access of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this ProfileEnrollmentPolicyRuleAction.


        :param access: The access of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :type: str
        """

        self._access = access

    @property
    def activation_requirements(self):
        """Gets the activation_requirements of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501


        :return: The activation_requirements of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :rtype: ProfileEnrollmentPolicyRuleActivationRequirement
        """
        return self._activation_requirements

    @activation_requirements.setter
    def activation_requirements(self, activation_requirements):
        """Sets the activation_requirements of this ProfileEnrollmentPolicyRuleAction.


        :param activation_requirements: The activation_requirements of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :type: ProfileEnrollmentPolicyRuleActivationRequirement
        """

        self._activation_requirements = activation_requirements

    @property
    def pre_registration_inline_hooks(self):
        """Gets the pre_registration_inline_hooks of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501


        :return: The pre_registration_inline_hooks of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :rtype: list[PreRegistrationInlineHook]
        """
        return self._pre_registration_inline_hooks

    @pre_registration_inline_hooks.setter
    def pre_registration_inline_hooks(self, pre_registration_inline_hooks):
        """Sets the pre_registration_inline_hooks of this ProfileEnrollmentPolicyRuleAction.


        :param pre_registration_inline_hooks: The pre_registration_inline_hooks of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :type: list[PreRegistrationInlineHook]
        """

        self._pre_registration_inline_hooks = pre_registration_inline_hooks

    @property
    def profile_attributes(self):
        """Gets the profile_attributes of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501


        :return: The profile_attributes of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :rtype: list[ProfileEnrollmentPolicyRuleProfileAttribute]
        """
        return self._profile_attributes

    @profile_attributes.setter
    def profile_attributes(self, profile_attributes):
        """Sets the profile_attributes of this ProfileEnrollmentPolicyRuleAction.


        :param profile_attributes: The profile_attributes of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :type: list[ProfileEnrollmentPolicyRuleProfileAttribute]
        """

        self._profile_attributes = profile_attributes

    @property
    def target_group_ids(self):
        """Gets the target_group_ids of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501


        :return: The target_group_ids of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_group_ids

    @target_group_ids.setter
    def target_group_ids(self, target_group_ids):
        """Sets the target_group_ids of this ProfileEnrollmentPolicyRuleAction.


        :param target_group_ids: The target_group_ids of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :type: list[str]
        """

        self._target_group_ids = target_group_ids

    @property
    def unknown_user_action(self):
        """Gets the unknown_user_action of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501


        :return: The unknown_user_action of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :rtype: str
        """
        return self._unknown_user_action

    @unknown_user_action.setter
    def unknown_user_action(self, unknown_user_action):
        """Sets the unknown_user_action of this ProfileEnrollmentPolicyRuleAction.


        :param unknown_user_action: The unknown_user_action of this ProfileEnrollmentPolicyRuleAction.  # noqa: E501
        :type: str
        """

        self._unknown_user_action = unknown_user_action

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
        if issubclass(ProfileEnrollmentPolicyRuleAction, dict):
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
        if not isinstance(other, ProfileEnrollmentPolicyRuleAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
