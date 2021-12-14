# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from okta.helpers import to_snake_case

class ApplicationGroupAssignment(object):
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
        'embedded': 'dict(str, object)',
        'links': 'dict(str, object)',
        'id': 'str',
        'last_updated': 'datetime',
        'priority': 'int',
        'profile': 'dict(str, object)'
    }

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'priority': 'priority',
        'profile': 'profile'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, embedded=None, links=None, id=None, last_updated=None, priority=None, profile=None):  # noqa: E501
        """ApplicationGroupAssignment - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._id = None
        self._last_updated = None
        self._priority = None
        self._profile = None
        self.discriminator = None
        if embedded is not None:
            self.embedded = embedded
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if priority is not None:
            self.priority = priority
        if profile is not None:
            self.profile = profile

    @property
    def embedded(self):
        """Gets the embedded of this ApplicationGroupAssignment.  # noqa: E501


        :return: The embedded of this ApplicationGroupAssignment.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this ApplicationGroupAssignment.


        :param embedded: The embedded of this ApplicationGroupAssignment.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this ApplicationGroupAssignment.  # noqa: E501


        :return: The links of this ApplicationGroupAssignment.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApplicationGroupAssignment.


        :param links: The links of this ApplicationGroupAssignment.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this ApplicationGroupAssignment.  # noqa: E501


        :return: The id of this ApplicationGroupAssignment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationGroupAssignment.


        :param id: The id of this ApplicationGroupAssignment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this ApplicationGroupAssignment.  # noqa: E501


        :return: The last_updated of this ApplicationGroupAssignment.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ApplicationGroupAssignment.


        :param last_updated: The last_updated of this ApplicationGroupAssignment.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def priority(self):
        """Gets the priority of this ApplicationGroupAssignment.  # noqa: E501


        :return: The priority of this ApplicationGroupAssignment.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ApplicationGroupAssignment.


        :param priority: The priority of this ApplicationGroupAssignment.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def profile(self):
        """Gets the profile of this ApplicationGroupAssignment.  # noqa: E501


        :return: The profile of this ApplicationGroupAssignment.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this ApplicationGroupAssignment.


        :param profile: The profile of this ApplicationGroupAssignment.  # noqa: E501
        :type: dict(str, object)
        """

        self._profile = profile

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
        if issubclass(ApplicationGroupAssignment, dict):
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
        if not isinstance(other, ApplicationGroupAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other