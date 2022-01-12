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

class VerificationMethod(object):
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
    swagger_types['constraints'] = 'list[AccessPolicyConstraints]'
    swagger_types['factor_mode'] = 'str'
    swagger_types['reauthenticate_in'] = 'str'
    swagger_types['type'] = 'str'

    attribute_map = {
        'constraints': 'constraints',
        'factor_mode': 'factorMode',
        'reauthenticate_in': 'reauthenticateIn',
        'type': 'type'
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

    def set_attributes(self, constraints=None, factor_mode=None, reauthenticate_in=None, type=None, **kwargs):  # noqa: E501
        """VerificationMethod - a model defined in Swagger"""  # noqa: E501
        self._constraints = None
        self._factor_mode = None
        self._reauthenticate_in = None
        self._type = None
        self.discriminator = None
        if constraints is not None:
            if hasattr(models, self.swagger_types['constraints']):
                nested_class = getattr(models, self.swagger_types['constraints'])
                if isinstance(constraints, nested_class):
                    self.constraints = constraints
                elif isinstance(constraints, dict):
                    self.constraints = nested_class.from_kwargs(**constraints)
                else:
                    self.constraints = constraints
            else:
                self.constraints = constraints
        if factor_mode is not None:
            if hasattr(models, self.swagger_types['factor_mode']):
                nested_class = getattr(models, self.swagger_types['factor_mode'])
                if isinstance(factor_mode, nested_class):
                    self.factor_mode = factor_mode
                elif isinstance(factor_mode, dict):
                    self.factor_mode = nested_class.from_kwargs(**factor_mode)
                else:
                    self.factor_mode = factor_mode
            else:
                self.factor_mode = factor_mode
        if reauthenticate_in is not None:
            if hasattr(models, self.swagger_types['reauthenticate_in']):
                nested_class = getattr(models, self.swagger_types['reauthenticate_in'])
                if isinstance(reauthenticate_in, nested_class):
                    self.reauthenticate_in = reauthenticate_in
                elif isinstance(reauthenticate_in, dict):
                    self.reauthenticate_in = nested_class.from_kwargs(**reauthenticate_in)
                else:
                    self.reauthenticate_in = reauthenticate_in
            else:
                self.reauthenticate_in = reauthenticate_in
        if type is not None:
            if hasattr(models, self.swagger_types['type']):
                nested_class = getattr(models, self.swagger_types['type'])
                if isinstance(type, nested_class):
                    self.type = type
                elif isinstance(type, dict):
                    self.type = nested_class.from_kwargs(**type)
                else:
                    self.type = type
            else:
                self.type = type

    @property
    def constraints(self):
        """Gets the constraints of this VerificationMethod.  # noqa: E501


        :return: The constraints of this VerificationMethod.  # noqa: E501
        :rtype: list[AccessPolicyConstraints]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this VerificationMethod.


        :param constraints: The constraints of this VerificationMethod.  # noqa: E501
        :type: list[AccessPolicyConstraints]
        """

        self._constraints = constraints

    @property
    def factor_mode(self):
        """Gets the factor_mode of this VerificationMethod.  # noqa: E501


        :return: The factor_mode of this VerificationMethod.  # noqa: E501
        :rtype: str
        """
        return self._factor_mode

    @factor_mode.setter
    def factor_mode(self, factor_mode):
        """Sets the factor_mode of this VerificationMethod.


        :param factor_mode: The factor_mode of this VerificationMethod.  # noqa: E501
        :type: str
        """

        self._factor_mode = factor_mode

    @property
    def reauthenticate_in(self):
        """Gets the reauthenticate_in of this VerificationMethod.  # noqa: E501


        :return: The reauthenticate_in of this VerificationMethod.  # noqa: E501
        :rtype: str
        """
        return self._reauthenticate_in

    @reauthenticate_in.setter
    def reauthenticate_in(self, reauthenticate_in):
        """Sets the reauthenticate_in of this VerificationMethod.


        :param reauthenticate_in: The reauthenticate_in of this VerificationMethod.  # noqa: E501
        :type: str
        """

        self._reauthenticate_in = reauthenticate_in

    @property
    def type(self):
        """Gets the type of this VerificationMethod.  # noqa: E501


        :return: The type of this VerificationMethod.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VerificationMethod.


        :param type: The type of this VerificationMethod.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(VerificationMethod, dict):
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
        if not isinstance(other, VerificationMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other