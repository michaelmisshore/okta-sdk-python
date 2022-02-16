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

class ApplicationSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}
    swagger_types['app'] = 'ApplicationSettingsApplication'
    swagger_types['implicit_assignment'] = 'bool'
    swagger_types['inline_hook_id'] = 'str'
    swagger_types['notifications'] = 'ApplicationSettingsNotifications'
    swagger_types['notes'] = 'ApplicationSettingsNotes'

    attribute_map = {
        'app': 'app',
        'implicit_assignment': 'implicitAssignment',
        'inline_hook_id': 'inlineHookId',
        'notifications': 'notifications',
        'notes': 'notes'
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

    def set_attributes(self, app=None, implicit_assignment=None, inline_hook_id=None, notifications=None, notes=None, **kwargs):  # noqa: E501
        """ApplicationSettings - a model defined in Swagger"""  # noqa: E501
        self._app = None
        self._implicit_assignment = None
        self._inline_hook_id = None
        self._notifications = None
        self._notes = None
        self.discriminator = None
        if app is not None:
            if hasattr(models, self.swagger_types['app']):
                nested_class = getattr(models, self.swagger_types['app'])
                if isinstance(app, nested_class):
                    self.app = app
                elif isinstance(app, dict):
                    self.app = nested_class.from_kwargs(**app)
                else:
                    self.app = app
            else:
                self.app = app
        if implicit_assignment is not None:
            if hasattr(models, self.swagger_types['implicit_assignment']):
                nested_class = getattr(models, self.swagger_types['implicit_assignment'])
                if isinstance(implicit_assignment, nested_class):
                    self.implicit_assignment = implicit_assignment
                elif isinstance(implicit_assignment, dict):
                    self.implicit_assignment = nested_class.from_kwargs(**implicit_assignment)
                else:
                    self.implicit_assignment = implicit_assignment
            else:
                self.implicit_assignment = implicit_assignment
        if inline_hook_id is not None:
            if hasattr(models, self.swagger_types['inline_hook_id']):
                nested_class = getattr(models, self.swagger_types['inline_hook_id'])
                if isinstance(inline_hook_id, nested_class):
                    self.inline_hook_id = inline_hook_id
                elif isinstance(inline_hook_id, dict):
                    self.inline_hook_id = nested_class.from_kwargs(**inline_hook_id)
                else:
                    self.inline_hook_id = inline_hook_id
            else:
                self.inline_hook_id = inline_hook_id
        if notifications is not None:
            if hasattr(models, self.swagger_types['notifications']):
                nested_class = getattr(models, self.swagger_types['notifications'])
                if isinstance(notifications, nested_class):
                    self.notifications = notifications
                elif isinstance(notifications, dict):
                    self.notifications = nested_class.from_kwargs(**notifications)
                else:
                    self.notifications = notifications
            else:
                self.notifications = notifications
        if notes is not None:
            if hasattr(models, self.swagger_types['notes']):
                nested_class = getattr(models, self.swagger_types['notes'])
                if isinstance(notes, nested_class):
                    self.notes = notes
                elif isinstance(notes, dict):
                    self.notes = nested_class.from_kwargs(**notes)
                else:
                    self.notes = notes
            else:
                self.notes = notes

    @property
    def app(self):
        """Gets the app of this ApplicationSettings.  # noqa: E501


        :return: The app of this ApplicationSettings.  # noqa: E501
        :rtype: ApplicationSettingsApplication
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ApplicationSettings.


        :param app: The app of this ApplicationSettings.  # noqa: E501
        :type: ApplicationSettingsApplication
        """

        self._app = app

    @property
    def implicit_assignment(self):
        """Gets the implicit_assignment of this ApplicationSettings.  # noqa: E501


        :return: The implicit_assignment of this ApplicationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._implicit_assignment

    @implicit_assignment.setter
    def implicit_assignment(self, implicit_assignment):
        """Sets the implicit_assignment of this ApplicationSettings.


        :param implicit_assignment: The implicit_assignment of this ApplicationSettings.  # noqa: E501
        :type: bool
        """

        self._implicit_assignment = implicit_assignment

    @property
    def inline_hook_id(self):
        """Gets the inline_hook_id of this ApplicationSettings.  # noqa: E501


        :return: The inline_hook_id of this ApplicationSettings.  # noqa: E501
        :rtype: str
        """
        return self._inline_hook_id

    @inline_hook_id.setter
    def inline_hook_id(self, inline_hook_id):
        """Sets the inline_hook_id of this ApplicationSettings.


        :param inline_hook_id: The inline_hook_id of this ApplicationSettings.  # noqa: E501
        :type: str
        """

        self._inline_hook_id = inline_hook_id

    @property
    def notifications(self):
        """Gets the notifications of this ApplicationSettings.  # noqa: E501


        :return: The notifications of this ApplicationSettings.  # noqa: E501
        :rtype: ApplicationSettingsNotifications
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this ApplicationSettings.


        :param notifications: The notifications of this ApplicationSettings.  # noqa: E501
        :type: ApplicationSettingsNotifications
        """

        self._notifications = notifications

    @property
    def notes(self):
        """Gets the notes of this ApplicationSettings.  # noqa: E501


        :return: The notes of this ApplicationSettings.  # noqa: E501
        :rtype: ApplicationSettingsNotes
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ApplicationSettings.


        :param notes: The notes of this ApplicationSettings.  # noqa: E501
        :type: ApplicationSettingsNotes
        """

        self._notes = notes

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
        if issubclass(ApplicationSettings, dict):
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
        if not isinstance(other, ApplicationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
