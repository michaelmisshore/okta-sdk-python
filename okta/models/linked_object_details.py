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

class LinkedObjectDetails(object):
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
        'description': 'str',
        'name': 'str',
        'title': 'str',
        'type': 'LinkedObjectDetailsType'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'title': 'title',
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

    def set_attributes(self, description=None, name=None, title=None, type=None):  # noqa: E501
        """LinkedObjectDetails - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._name = None
        self._title = None
        self._type = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this LinkedObjectDetails.  # noqa: E501


        :return: The description of this LinkedObjectDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LinkedObjectDetails.


        :param description: The description of this LinkedObjectDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this LinkedObjectDetails.  # noqa: E501


        :return: The name of this LinkedObjectDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LinkedObjectDetails.


        :param name: The name of this LinkedObjectDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this LinkedObjectDetails.  # noqa: E501


        :return: The title of this LinkedObjectDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LinkedObjectDetails.


        :param title: The title of this LinkedObjectDetails.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this LinkedObjectDetails.  # noqa: E501


        :return: The type of this LinkedObjectDetails.  # noqa: E501
        :rtype: LinkedObjectDetailsType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LinkedObjectDetails.


        :param type: The type of this LinkedObjectDetails.  # noqa: E501
        :type: LinkedObjectDetailsType
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
        if issubclass(LinkedObjectDetails, dict):
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
        if not isinstance(other, LinkedObjectDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
