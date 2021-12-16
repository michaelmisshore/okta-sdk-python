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
from okta.models.email_content import EmailContent  # noqa: F401,E501

from okta.helpers import to_snake_case

class EmailCustomization(EmailContent):
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
        'id': 'str',
        'language': 'str',
        'is_default': 'bool',
        'created': 'datetime',
        'last_updated': 'datetime',
        'links': 'EmailDefaultContentLinks'
    }
    if hasattr(EmailContent, "swagger_types"):
        swagger_types.update(EmailContent.swagger_types)

    attribute_map = {
        'id': 'id',
        'language': 'language',
        'is_default': 'isDefault',
        'created': 'created',
        'last_updated': 'lastUpdated',
        'links': '_links'
    }
    if hasattr(EmailContent, "attribute_map"):
        attribute_map.update(EmailContent.attribute_map)

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
        else:
            config = {}
        self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, id=None, language=None, is_default=None, created=None, last_updated=None, links=None, *args, **kwargs):  # noqa: E501
        """EmailCustomization - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._language = None
        self._is_default = None
        self._created = None
        self._last_updated = None
        self._links = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.language = language
        if is_default is not None:
            self.is_default = is_default
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated
        if links is not None:
            self.links = links
        super().set_attributes(*args, **kwargs)

    @property
    def id(self):
        """Gets the id of this EmailCustomization.  # noqa: E501


        :return: The id of this EmailCustomization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmailCustomization.


        :param id: The id of this EmailCustomization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def language(self):
        """Gets the language of this EmailCustomization.  # noqa: E501

        unique under each email templage  # noqa: E501

        :return: The language of this EmailCustomization.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this EmailCustomization.

        unique under each email templage  # noqa: E501

        :param language: The language of this EmailCustomization.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def is_default(self):
        """Gets the is_default of this EmailCustomization.  # noqa: E501


        :return: The is_default of this EmailCustomization.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this EmailCustomization.


        :param is_default: The is_default of this EmailCustomization.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def created(self):
        """Gets the created of this EmailCustomization.  # noqa: E501


        :return: The created of this EmailCustomization.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EmailCustomization.


        :param created: The created of this EmailCustomization.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this EmailCustomization.  # noqa: E501


        :return: The last_updated of this EmailCustomization.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this EmailCustomization.


        :param last_updated: The last_updated of this EmailCustomization.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def links(self):
        """Gets the links of this EmailCustomization.  # noqa: E501


        :return: The links of this EmailCustomization.  # noqa: E501
        :rtype: EmailDefaultContentLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EmailCustomization.


        :param links: The links of this EmailCustomization.  # noqa: E501
        :type: EmailDefaultContentLinks
        """

        self._links = links

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
        if issubclass(EmailCustomization, dict):
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
        if not isinstance(other, EmailCustomization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
