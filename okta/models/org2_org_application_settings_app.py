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
from okta.models.application_settings_application import ApplicationSettingsApplication  # noqa: F401,E501

import okta.models as models  # noqa
from okta.helpers import to_snake_case

class Org2OrgApplicationSettingsApp(ApplicationSettingsApplication):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    if hasattr(ApplicationSettingsApplication, "swagger_types"):
        swagger_types.update(ApplicationSettingsApplication.swagger_types)
    swagger_types['acs_url'] = 'str'
    swagger_types['aud_restriction'] = 'str'
    swagger_types['base_url'] = 'str'

    attribute_map = {
        'acs_url': 'acsUrl',
        'aud_restriction': 'audRestriction',
        'base_url': 'baseUrl'
    }
    if hasattr(ApplicationSettingsApplication, "attribute_map"):
        attribute_map.update(ApplicationSettingsApplication.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, acs_url=None, aud_restriction=None, base_url=None, **kwargs):  # noqa: E501
        """Org2OrgApplicationSettingsApp - a model defined in Swagger"""  # noqa: E501
        config = {}
        if kwargs is not None:
            config = {to_snake_case(key): value for key, value in kwargs.items()}
        super().set_attributes(**config)
        self._acs_url = None
        self._aud_restriction = None
        self._base_url = None
        self.discriminator = None
        if acs_url is not None:
            if hasattr(models, self.swagger_types['acs_url']):
                nested_class = getattr(models, self.swagger_types['acs_url'])
                if isinstance(acs_url, nested_class):
                    self.acs_url = acs_url
                elif isinstance(acs_url, dict):
                    self.acs_url = nested_class.from_kwargs(**acs_url)
                else:
                    self.acs_url = acs_url
            else:
                self.acs_url = acs_url
        if aud_restriction is not None:
            if hasattr(models, self.swagger_types['aud_restriction']):
                nested_class = getattr(models, self.swagger_types['aud_restriction'])
                if isinstance(aud_restriction, nested_class):
                    self.aud_restriction = aud_restriction
                elif isinstance(aud_restriction, dict):
                    self.aud_restriction = nested_class.from_kwargs(**aud_restriction)
                else:
                    self.aud_restriction = aud_restriction
            else:
                self.aud_restriction = aud_restriction
        if base_url is not None:
            if hasattr(models, self.swagger_types['base_url']):
                nested_class = getattr(models, self.swagger_types['base_url'])
                if isinstance(base_url, nested_class):
                    self.base_url = base_url
                elif isinstance(base_url, dict):
                    self.base_url = nested_class.from_kwargs(**base_url)
                else:
                    self.base_url = base_url
            else:
                self.base_url = base_url

    @property
    def acs_url(self):
        """Gets the acs_url of this Org2OrgApplicationSettingsApp.  # noqa: E501


        :return: The acs_url of this Org2OrgApplicationSettingsApp.  # noqa: E501
        :rtype: str
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        """Sets the acs_url of this Org2OrgApplicationSettingsApp.


        :param acs_url: The acs_url of this Org2OrgApplicationSettingsApp.  # noqa: E501
        :type: str
        """

        self._acs_url = acs_url

    @property
    def aud_restriction(self):
        """Gets the aud_restriction of this Org2OrgApplicationSettingsApp.  # noqa: E501


        :return: The aud_restriction of this Org2OrgApplicationSettingsApp.  # noqa: E501
        :rtype: str
        """
        return self._aud_restriction

    @aud_restriction.setter
    def aud_restriction(self, aud_restriction):
        """Sets the aud_restriction of this Org2OrgApplicationSettingsApp.


        :param aud_restriction: The aud_restriction of this Org2OrgApplicationSettingsApp.  # noqa: E501
        :type: str
        """

        self._aud_restriction = aud_restriction

    @property
    def base_url(self):
        """Gets the base_url of this Org2OrgApplicationSettingsApp.  # noqa: E501


        :return: The base_url of this Org2OrgApplicationSettingsApp.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this Org2OrgApplicationSettingsApp.


        :param base_url: The base_url of this Org2OrgApplicationSettingsApp.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

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
        if issubclass(Org2OrgApplicationSettingsApp, dict):
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
        if not isinstance(other, Org2OrgApplicationSettingsApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
