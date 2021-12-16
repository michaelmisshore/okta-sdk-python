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
from okta.models.application_credentials import ApplicationCredentials  # noqa: F401,E501

from okta.helpers import to_snake_case

class SchemeApplicationCredentials(ApplicationCredentials):
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
        'password': 'PasswordCredential',
        'reveal_password': 'bool',
        'scheme': 'ApplicationCredentialsScheme',
        'signing': 'ApplicationCredentialsSigning',
        'user_name': 'str'
    }
    if hasattr(ApplicationCredentials, "swagger_types"):
        swagger_types.update(ApplicationCredentials.swagger_types)

    attribute_map = {
        'password': 'password',
        'reveal_password': 'revealPassword',
        'scheme': 'scheme',
        'signing': 'signing',
        'user_name': 'userName'
    }
    if hasattr(ApplicationCredentials, "attribute_map"):
        attribute_map.update(ApplicationCredentials.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, password=None, reveal_password=None, scheme=None, signing=None, user_name=None, *args, **kwargs):  # noqa: E501
        """SchemeApplicationCredentials - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._reveal_password = None
        self._scheme = None
        self._signing = None
        self._user_name = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if reveal_password is not None:
            self.reveal_password = reveal_password
        if scheme is not None:
            self.scheme = scheme
        if signing is not None:
            self.signing = signing
        if user_name is not None:
            self.user_name = user_name
        super().set_attributes(*args, **kwargs)

    @property
    def password(self):
        """Gets the password of this SchemeApplicationCredentials.  # noqa: E501


        :return: The password of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: PasswordCredential
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SchemeApplicationCredentials.


        :param password: The password of this SchemeApplicationCredentials.  # noqa: E501
        :type: PasswordCredential
        """

        self._password = password

    @property
    def reveal_password(self):
        """Gets the reveal_password of this SchemeApplicationCredentials.  # noqa: E501


        :return: The reveal_password of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: bool
        """
        return self._reveal_password

    @reveal_password.setter
    def reveal_password(self, reveal_password):
        """Sets the reveal_password of this SchemeApplicationCredentials.


        :param reveal_password: The reveal_password of this SchemeApplicationCredentials.  # noqa: E501
        :type: bool
        """

        self._reveal_password = reveal_password

    @property
    def scheme(self):
        """Gets the scheme of this SchemeApplicationCredentials.  # noqa: E501


        :return: The scheme of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: ApplicationCredentialsScheme
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this SchemeApplicationCredentials.


        :param scheme: The scheme of this SchemeApplicationCredentials.  # noqa: E501
        :type: ApplicationCredentialsScheme
        """

        self._scheme = scheme

    @property
    def signing(self):
        """Gets the signing of this SchemeApplicationCredentials.  # noqa: E501


        :return: The signing of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: ApplicationCredentialsSigning
        """
        return self._signing

    @signing.setter
    def signing(self, signing):
        """Sets the signing of this SchemeApplicationCredentials.


        :param signing: The signing of this SchemeApplicationCredentials.  # noqa: E501
        :type: ApplicationCredentialsSigning
        """

        self._signing = signing

    @property
    def user_name(self):
        """Gets the user_name of this SchemeApplicationCredentials.  # noqa: E501


        :return: The user_name of this SchemeApplicationCredentials.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SchemeApplicationCredentials.


        :param user_name: The user_name of this SchemeApplicationCredentials.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(SchemeApplicationCredentials, dict):
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
        if not isinstance(other, SchemeApplicationCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
