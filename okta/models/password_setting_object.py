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

class PasswordSettingObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['change'] = 'ChangeEnum'
    swagger_types['seed'] = 'SeedEnum'
    swagger_types['status'] = 'EnabledStatus'

    attribute_map = {
        'change': 'change',
        'seed': 'seed',
        'status': 'status'
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

    def set_attributes(self, change=None, seed=None, status=None, **kwargs):  # noqa: E501
        """PasswordSettingObject - a model defined in Swagger"""  # noqa: E501
        self._change = None
        self._seed = None
        self._status = None
        self.discriminator = None
        if change is not None:
            if hasattr(models, self.swagger_types['change']):
                nested_class = getattr(models, self.swagger_types['change'])
                if isinstance(change, nested_class):
                    self.change = change
                elif isinstance(change, dict):
                    self.change = nested_class.from_kwargs(**change)
                else:
                    self.change = change
            else:
                self.change = change
        if seed is not None:
            if hasattr(models, self.swagger_types['seed']):
                nested_class = getattr(models, self.swagger_types['seed'])
                if isinstance(seed, nested_class):
                    self.seed = seed
                elif isinstance(seed, dict):
                    self.seed = nested_class.from_kwargs(**seed)
                else:
                    self.seed = seed
            else:
                self.seed = seed
        if status is not None:
            if hasattr(models, self.swagger_types['status']):
                nested_class = getattr(models, self.swagger_types['status'])
                if isinstance(status, nested_class):
                    self.status = status
                elif isinstance(status, dict):
                    self.status = nested_class.from_kwargs(**status)
                else:
                    self.status = status
            else:
                self.status = status

    @property
    def change(self):
        """Gets the change of this PasswordSettingObject.  # noqa: E501


        :return: The change of this PasswordSettingObject.  # noqa: E501
        :rtype: ChangeEnum
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this PasswordSettingObject.


        :param change: The change of this PasswordSettingObject.  # noqa: E501
        :type: ChangeEnum
        """

        self._change = change

    @property
    def seed(self):
        """Gets the seed of this PasswordSettingObject.  # noqa: E501


        :return: The seed of this PasswordSettingObject.  # noqa: E501
        :rtype: SeedEnum
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this PasswordSettingObject.


        :param seed: The seed of this PasswordSettingObject.  # noqa: E501
        :type: SeedEnum
        """

        self._seed = seed

    @property
    def status(self):
        """Gets the status of this PasswordSettingObject.  # noqa: E501


        :return: The status of this PasswordSettingObject.  # noqa: E501
        :rtype: EnabledStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PasswordSettingObject.


        :param status: The status of this PasswordSettingObject.  # noqa: E501
        :type: EnabledStatus
        """

        self._status = status

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
        if issubclass(PasswordSettingObject, dict):
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
        if not isinstance(other, PasswordSettingObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
