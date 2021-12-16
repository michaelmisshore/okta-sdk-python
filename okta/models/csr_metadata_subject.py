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

class CsrMetadataSubject(object):
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
        'common_name': 'str',
        'country_name': 'str',
        'locality_name': 'str',
        'organization_name': 'str',
        'organizational_unit_name': 'str',
        'state_or_province_name': 'str'
    }

    attribute_map = {
        'common_name': 'commonName',
        'country_name': 'countryName',
        'locality_name': 'localityName',
        'organization_name': 'organizationName',
        'organizational_unit_name': 'organizationalUnitName',
        'state_or_province_name': 'stateOrProvinceName'
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

    def set_attributes(self, common_name=None, country_name=None, locality_name=None, organization_name=None, organizational_unit_name=None, state_or_province_name=None):  # noqa: E501
        """CsrMetadataSubject - a model defined in Swagger"""  # noqa: E501
        self._common_name = None
        self._country_name = None
        self._locality_name = None
        self._organization_name = None
        self._organizational_unit_name = None
        self._state_or_province_name = None
        self.discriminator = None
        if common_name is not None:
            self.common_name = common_name
        if country_name is not None:
            self.country_name = country_name
        if locality_name is not None:
            self.locality_name = locality_name
        if organization_name is not None:
            self.organization_name = organization_name
        if organizational_unit_name is not None:
            self.organizational_unit_name = organizational_unit_name
        if state_or_province_name is not None:
            self.state_or_province_name = state_or_province_name

    @property
    def common_name(self):
        """Gets the common_name of this CsrMetadataSubject.  # noqa: E501


        :return: The common_name of this CsrMetadataSubject.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this CsrMetadataSubject.


        :param common_name: The common_name of this CsrMetadataSubject.  # noqa: E501
        :type: str
        """

        self._common_name = common_name

    @property
    def country_name(self):
        """Gets the country_name of this CsrMetadataSubject.  # noqa: E501


        :return: The country_name of this CsrMetadataSubject.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this CsrMetadataSubject.


        :param country_name: The country_name of this CsrMetadataSubject.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def locality_name(self):
        """Gets the locality_name of this CsrMetadataSubject.  # noqa: E501


        :return: The locality_name of this CsrMetadataSubject.  # noqa: E501
        :rtype: str
        """
        return self._locality_name

    @locality_name.setter
    def locality_name(self, locality_name):
        """Sets the locality_name of this CsrMetadataSubject.


        :param locality_name: The locality_name of this CsrMetadataSubject.  # noqa: E501
        :type: str
        """

        self._locality_name = locality_name

    @property
    def organization_name(self):
        """Gets the organization_name of this CsrMetadataSubject.  # noqa: E501


        :return: The organization_name of this CsrMetadataSubject.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this CsrMetadataSubject.


        :param organization_name: The organization_name of this CsrMetadataSubject.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def organizational_unit_name(self):
        """Gets the organizational_unit_name of this CsrMetadataSubject.  # noqa: E501


        :return: The organizational_unit_name of this CsrMetadataSubject.  # noqa: E501
        :rtype: str
        """
        return self._organizational_unit_name

    @organizational_unit_name.setter
    def organizational_unit_name(self, organizational_unit_name):
        """Sets the organizational_unit_name of this CsrMetadataSubject.


        :param organizational_unit_name: The organizational_unit_name of this CsrMetadataSubject.  # noqa: E501
        :type: str
        """

        self._organizational_unit_name = organizational_unit_name

    @property
    def state_or_province_name(self):
        """Gets the state_or_province_name of this CsrMetadataSubject.  # noqa: E501


        :return: The state_or_province_name of this CsrMetadataSubject.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province_name

    @state_or_province_name.setter
    def state_or_province_name(self, state_or_province_name):
        """Sets the state_or_province_name of this CsrMetadataSubject.


        :param state_or_province_name: The state_or_province_name of this CsrMetadataSubject.  # noqa: E501
        :type: str
        """

        self._state_or_province_name = state_or_province_name

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
        if issubclass(CsrMetadataSubject, dict):
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
        if not isinstance(other, CsrMetadataSubject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
