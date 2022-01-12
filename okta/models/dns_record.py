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

class DNSRecord(object):
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
    swagger_types['expiration'] = 'str'
    swagger_types['fqdn'] = 'str'
    swagger_types['record_type'] = 'DNSRecordType'
    swagger_types['values'] = 'list[str]'

    attribute_map = {
        'expiration': 'expiration',
        'fqdn': 'fqdn',
        'record_type': 'recordType',
        'values': 'values'
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

    def set_attributes(self, expiration=None, fqdn=None, record_type=None, values=None, **kwargs):  # noqa: E501
        """DNSRecord - a model defined in Swagger"""  # noqa: E501
        self._expiration = None
        self._fqdn = None
        self._record_type = None
        self._values = None
        self.discriminator = None
        if expiration is not None:
            if hasattr(models, self.swagger_types['expiration']):
                nested_class = getattr(models, self.swagger_types['expiration'])
                if isinstance(expiration, nested_class):
                    self.expiration = expiration
                elif isinstance(expiration, dict):
                    self.expiration = nested_class.from_kwargs(**expiration)
                else:
                    self.expiration = expiration
            else:
                self.expiration = expiration
        if fqdn is not None:
            if hasattr(models, self.swagger_types['fqdn']):
                nested_class = getattr(models, self.swagger_types['fqdn'])
                if isinstance(fqdn, nested_class):
                    self.fqdn = fqdn
                elif isinstance(fqdn, dict):
                    self.fqdn = nested_class.from_kwargs(**fqdn)
                else:
                    self.fqdn = fqdn
            else:
                self.fqdn = fqdn
        if record_type is not None:
            if hasattr(models, self.swagger_types['record_type']):
                nested_class = getattr(models, self.swagger_types['record_type'])
                if isinstance(record_type, nested_class):
                    self.record_type = record_type
                elif isinstance(record_type, dict):
                    self.record_type = nested_class.from_kwargs(**record_type)
                else:
                    self.record_type = record_type
            else:
                self.record_type = record_type
        if values is not None:
            if hasattr(models, self.swagger_types['values']):
                nested_class = getattr(models, self.swagger_types['values'])
                if isinstance(values, nested_class):
                    self.values = values
                elif isinstance(values, dict):
                    self.values = nested_class.from_kwargs(**values)
                else:
                    self.values = values
            else:
                self.values = values

    @property
    def expiration(self):
        """Gets the expiration of this DNSRecord.  # noqa: E501


        :return: The expiration of this DNSRecord.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this DNSRecord.


        :param expiration: The expiration of this DNSRecord.  # noqa: E501
        :type: str
        """

        self._expiration = expiration

    @property
    def fqdn(self):
        """Gets the fqdn of this DNSRecord.  # noqa: E501


        :return: The fqdn of this DNSRecord.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this DNSRecord.


        :param fqdn: The fqdn of this DNSRecord.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def record_type(self):
        """Gets the record_type of this DNSRecord.  # noqa: E501


        :return: The record_type of this DNSRecord.  # noqa: E501
        :rtype: DNSRecordType
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this DNSRecord.


        :param record_type: The record_type of this DNSRecord.  # noqa: E501
        :type: DNSRecordType
        """

        self._record_type = record_type

    @property
    def values(self):
        """Gets the values of this DNSRecord.  # noqa: E501


        :return: The values of this DNSRecord.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this DNSRecord.


        :param values: The values of this DNSRecord.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(DNSRecord, dict):
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
        if not isinstance(other, DNSRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other