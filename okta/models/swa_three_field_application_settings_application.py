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
from okta.models.application_settings_application import ApplicationSettingsApplication  # noqa: F401,E501

from okta.helpers import to_snake_case

class SwaThreeFieldApplicationSettingsApplication(ApplicationSettingsApplication):
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
        'button_selector': 'str',
        'extra_field_selector': 'str',
        'extra_field_value': 'str',
        'login_url_regex': 'str',
        'password_selector': 'str',
        'target_url': 'str',
        'user_name_selector': 'str'
    }
    if hasattr(ApplicationSettingsApplication, "swagger_types"):
        swagger_types.update(ApplicationSettingsApplication.swagger_types)

    attribute_map = {
        'button_selector': 'buttonSelector',
        'extra_field_selector': 'extraFieldSelector',
        'extra_field_value': 'extraFieldValue',
        'login_url_regex': 'loginUrlRegex',
        'password_selector': 'passwordSelector',
        'target_url': 'targetURL',
        'user_name_selector': 'userNameSelector'
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

    def set_attributes(self, button_selector=None, extra_field_selector=None, extra_field_value=None, login_url_regex=None, password_selector=None, target_url=None, user_name_selector=None, *args, **kwargs):  # noqa: E501
        """SwaThreeFieldApplicationSettingsApplication - a model defined in Swagger"""  # noqa: E501
        self._button_selector = None
        self._extra_field_selector = None
        self._extra_field_value = None
        self._login_url_regex = None
        self._password_selector = None
        self._target_url = None
        self._user_name_selector = None
        self.discriminator = None
        if button_selector is not None:
            self.button_selector = button_selector
        if extra_field_selector is not None:
            self.extra_field_selector = extra_field_selector
        if extra_field_value is not None:
            self.extra_field_value = extra_field_value
        if login_url_regex is not None:
            self.login_url_regex = login_url_regex
        if password_selector is not None:
            self.password_selector = password_selector
        if target_url is not None:
            self.target_url = target_url
        if user_name_selector is not None:
            self.user_name_selector = user_name_selector
        super().set_attributes(*args, **kwargs)

    @property
    def button_selector(self):
        """Gets the button_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501


        :return: The button_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._button_selector

    @button_selector.setter
    def button_selector(self, button_selector):
        """Sets the button_selector of this SwaThreeFieldApplicationSettingsApplication.


        :param button_selector: The button_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._button_selector = button_selector

    @property
    def extra_field_selector(self):
        """Gets the extra_field_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501


        :return: The extra_field_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._extra_field_selector

    @extra_field_selector.setter
    def extra_field_selector(self, extra_field_selector):
        """Sets the extra_field_selector of this SwaThreeFieldApplicationSettingsApplication.


        :param extra_field_selector: The extra_field_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._extra_field_selector = extra_field_selector

    @property
    def extra_field_value(self):
        """Gets the extra_field_value of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501


        :return: The extra_field_value of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._extra_field_value

    @extra_field_value.setter
    def extra_field_value(self, extra_field_value):
        """Sets the extra_field_value of this SwaThreeFieldApplicationSettingsApplication.


        :param extra_field_value: The extra_field_value of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._extra_field_value = extra_field_value

    @property
    def login_url_regex(self):
        """Gets the login_url_regex of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501


        :return: The login_url_regex of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._login_url_regex

    @login_url_regex.setter
    def login_url_regex(self, login_url_regex):
        """Sets the login_url_regex of this SwaThreeFieldApplicationSettingsApplication.


        :param login_url_regex: The login_url_regex of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._login_url_regex = login_url_regex

    @property
    def password_selector(self):
        """Gets the password_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501


        :return: The password_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._password_selector

    @password_selector.setter
    def password_selector(self, password_selector):
        """Sets the password_selector of this SwaThreeFieldApplicationSettingsApplication.


        :param password_selector: The password_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._password_selector = password_selector

    @property
    def target_url(self):
        """Gets the target_url of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501


        :return: The target_url of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this SwaThreeFieldApplicationSettingsApplication.


        :param target_url: The target_url of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._target_url = target_url

    @property
    def user_name_selector(self):
        """Gets the user_name_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501


        :return: The user_name_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._user_name_selector

    @user_name_selector.setter
    def user_name_selector(self, user_name_selector):
        """Sets the user_name_selector of this SwaThreeFieldApplicationSettingsApplication.


        :param user_name_selector: The user_name_selector of this SwaThreeFieldApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._user_name_selector = user_name_selector

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
        if issubclass(SwaThreeFieldApplicationSettingsApplication, dict):
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
        if not isinstance(other, SwaThreeFieldApplicationSettingsApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
