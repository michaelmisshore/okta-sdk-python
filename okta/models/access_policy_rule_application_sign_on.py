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

class AccessPolicyRuleApplicationSignOn(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['access'] = 'str'
    swagger_types['verification_method'] = 'VerificationMethod'

    attribute_map = {
        'access': 'access',
        'verification_method': 'verificationMethod'
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

    def set_attributes(self, access=None, verification_method=None, **kwargs):  # noqa: E501
        """AccessPolicyRuleApplicationSignOn - a model defined in Swagger"""  # noqa: E501
        self._access = None
        self._verification_method = None
        self.discriminator = None
        if access is not None:
            if hasattr(models, self.swagger_types['access']):
                nested_class = getattr(models, self.swagger_types['access'])
                if isinstance(access, nested_class):
                    self.access = access
                elif isinstance(access, dict):
                    self.access = nested_class.from_kwargs(**access)
                else:
                    self.access = access
            else:
                self.access = access
        if verification_method is not None:
            if hasattr(models, self.swagger_types['verification_method']):
                nested_class = getattr(models, self.swagger_types['verification_method'])
                if isinstance(verification_method, nested_class):
                    self.verification_method = verification_method
                elif isinstance(verification_method, dict):
                    self.verification_method = nested_class.from_kwargs(**verification_method)
                else:
                    self.verification_method = verification_method
            else:
                self.verification_method = verification_method

    @property
    def access(self):
        """Gets the access of this AccessPolicyRuleApplicationSignOn.  # noqa: E501


        :return: The access of this AccessPolicyRuleApplicationSignOn.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this AccessPolicyRuleApplicationSignOn.


        :param access: The access of this AccessPolicyRuleApplicationSignOn.  # noqa: E501
        :type: str
        """

        self._access = access

    @property
    def verification_method(self):
        """Gets the verification_method of this AccessPolicyRuleApplicationSignOn.  # noqa: E501


        :return: The verification_method of this AccessPolicyRuleApplicationSignOn.  # noqa: E501
        :rtype: VerificationMethod
        """
        return self._verification_method

    @verification_method.setter
    def verification_method(self, verification_method):
        """Sets the verification_method of this AccessPolicyRuleApplicationSignOn.


        :param verification_method: The verification_method of this AccessPolicyRuleApplicationSignOn.  # noqa: E501
        :type: VerificationMethod
        """

        self._verification_method = verification_method

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
        if issubclass(AccessPolicyRuleApplicationSignOn, dict):
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
        if not isinstance(other, AccessPolicyRuleApplicationSignOn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
