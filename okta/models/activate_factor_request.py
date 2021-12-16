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

class ActivateFactorRequest(object):
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
        'attestation': 'str',
        'client_data': 'str',
        'pass_code': 'str',
        'registration_data': 'str',
        'state_token': 'str'
    }

    attribute_map = {
        'attestation': 'attestation',
        'client_data': 'clientData',
        'pass_code': 'passCode',
        'registration_data': 'registrationData',
        'state_token': 'stateToken'
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

    def set_attributes(self, attestation=None, client_data=None, pass_code=None, registration_data=None, state_token=None):  # noqa: E501
        """ActivateFactorRequest - a model defined in Swagger"""  # noqa: E501
        self._attestation = None
        self._client_data = None
        self._pass_code = None
        self._registration_data = None
        self._state_token = None
        self.discriminator = None
        if attestation is not None:
            self.attestation = attestation
        if client_data is not None:
            self.client_data = client_data
        if pass_code is not None:
            self.pass_code = pass_code
        if registration_data is not None:
            self.registration_data = registration_data
        if state_token is not None:
            self.state_token = state_token

    @property
    def attestation(self):
        """Gets the attestation of this ActivateFactorRequest.  # noqa: E501


        :return: The attestation of this ActivateFactorRequest.  # noqa: E501
        :rtype: str
        """
        return self._attestation

    @attestation.setter
    def attestation(self, attestation):
        """Sets the attestation of this ActivateFactorRequest.


        :param attestation: The attestation of this ActivateFactorRequest.  # noqa: E501
        :type: str
        """

        self._attestation = attestation

    @property
    def client_data(self):
        """Gets the client_data of this ActivateFactorRequest.  # noqa: E501


        :return: The client_data of this ActivateFactorRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_data

    @client_data.setter
    def client_data(self, client_data):
        """Sets the client_data of this ActivateFactorRequest.


        :param client_data: The client_data of this ActivateFactorRequest.  # noqa: E501
        :type: str
        """

        self._client_data = client_data

    @property
    def pass_code(self):
        """Gets the pass_code of this ActivateFactorRequest.  # noqa: E501


        :return: The pass_code of this ActivateFactorRequest.  # noqa: E501
        :rtype: str
        """
        return self._pass_code

    @pass_code.setter
    def pass_code(self, pass_code):
        """Sets the pass_code of this ActivateFactorRequest.


        :param pass_code: The pass_code of this ActivateFactorRequest.  # noqa: E501
        :type: str
        """

        self._pass_code = pass_code

    @property
    def registration_data(self):
        """Gets the registration_data of this ActivateFactorRequest.  # noqa: E501


        :return: The registration_data of this ActivateFactorRequest.  # noqa: E501
        :rtype: str
        """
        return self._registration_data

    @registration_data.setter
    def registration_data(self, registration_data):
        """Sets the registration_data of this ActivateFactorRequest.


        :param registration_data: The registration_data of this ActivateFactorRequest.  # noqa: E501
        :type: str
        """

        self._registration_data = registration_data

    @property
    def state_token(self):
        """Gets the state_token of this ActivateFactorRequest.  # noqa: E501


        :return: The state_token of this ActivateFactorRequest.  # noqa: E501
        :rtype: str
        """
        return self._state_token

    @state_token.setter
    def state_token(self, state_token):
        """Sets the state_token of this ActivateFactorRequest.


        :param state_token: The state_token of this ActivateFactorRequest.  # noqa: E501
        :type: str
        """

        self._state_token = state_token

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
        if issubclass(ActivateFactorRequest, dict):
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
        if not isinstance(other, ActivateFactorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
