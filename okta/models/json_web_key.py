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

class JsonWebKey(object):
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
        'links': 'dict(str, object)',
        'alg': 'str',
        'created': 'datetime',
        'e': 'str',
        'expires_at': 'datetime',
        'key_ops': 'list[str]',
        'kid': 'str',
        'kty': 'str',
        'last_updated': 'datetime',
        'n': 'str',
        'status': 'str',
        'use': 'str',
        'x5c': 'list[str]',
        'x5t': 'str',
        'x5t_s256': 'str',
        'x5u': 'str'
    }

    attribute_map = {
        'links': '_links',
        'alg': 'alg',
        'created': 'created',
        'e': 'e',
        'expires_at': 'expiresAt',
        'key_ops': 'key_ops',
        'kid': 'kid',
        'kty': 'kty',
        'last_updated': 'lastUpdated',
        'n': 'n',
        'status': 'status',
        'use': 'use',
        'x5c': 'x5c',
        'x5t': 'x5t',
        'x5t_s256': 'x5t#S256',
        'x5u': 'x5u'
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

    def set_attributes(self, links=None, alg=None, created=None, e=None, expires_at=None, key_ops=None, kid=None, kty=None, last_updated=None, n=None, status=None, use=None, x5c=None, x5t=None, x5t_s256=None, x5u=None):  # noqa: E501
        """JsonWebKey - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._alg = None
        self._created = None
        self._e = None
        self._expires_at = None
        self._key_ops = None
        self._kid = None
        self._kty = None
        self._last_updated = None
        self._n = None
        self._status = None
        self._use = None
        self._x5c = None
        self._x5t = None
        self._x5t_s256 = None
        self._x5u = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if alg is not None:
            self.alg = alg
        if created is not None:
            self.created = created
        if e is not None:
            self.e = e
        if expires_at is not None:
            self.expires_at = expires_at
        if key_ops is not None:
            self.key_ops = key_ops
        if kid is not None:
            self.kid = kid
        if kty is not None:
            self.kty = kty
        if last_updated is not None:
            self.last_updated = last_updated
        if n is not None:
            self.n = n
        if status is not None:
            self.status = status
        if use is not None:
            self.use = use
        if x5c is not None:
            self.x5c = x5c
        if x5t is not None:
            self.x5t = x5t
        if x5t_s256 is not None:
            self.x5t_s256 = x5t_s256
        if x5u is not None:
            self.x5u = x5u

    @property
    def links(self):
        """Gets the links of this JsonWebKey.  # noqa: E501


        :return: The links of this JsonWebKey.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this JsonWebKey.


        :param links: The links of this JsonWebKey.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def alg(self):
        """Gets the alg of this JsonWebKey.  # noqa: E501


        :return: The alg of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this JsonWebKey.


        :param alg: The alg of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._alg = alg

    @property
    def created(self):
        """Gets the created of this JsonWebKey.  # noqa: E501


        :return: The created of this JsonWebKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this JsonWebKey.


        :param created: The created of this JsonWebKey.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def e(self):
        """Gets the e of this JsonWebKey.  # noqa: E501


        :return: The e of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """Sets the e of this JsonWebKey.


        :param e: The e of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._e = e

    @property
    def expires_at(self):
        """Gets the expires_at of this JsonWebKey.  # noqa: E501


        :return: The expires_at of this JsonWebKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this JsonWebKey.


        :param expires_at: The expires_at of this JsonWebKey.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def key_ops(self):
        """Gets the key_ops of this JsonWebKey.  # noqa: E501


        :return: The key_ops of this JsonWebKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._key_ops

    @key_ops.setter
    def key_ops(self, key_ops):
        """Sets the key_ops of this JsonWebKey.


        :param key_ops: The key_ops of this JsonWebKey.  # noqa: E501
        :type: list[str]
        """

        self._key_ops = key_ops

    @property
    def kid(self):
        """Gets the kid of this JsonWebKey.  # noqa: E501


        :return: The kid of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this JsonWebKey.


        :param kid: The kid of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._kid = kid

    @property
    def kty(self):
        """Gets the kty of this JsonWebKey.  # noqa: E501


        :return: The kty of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """Sets the kty of this JsonWebKey.


        :param kty: The kty of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._kty = kty

    @property
    def last_updated(self):
        """Gets the last_updated of this JsonWebKey.  # noqa: E501


        :return: The last_updated of this JsonWebKey.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this JsonWebKey.


        :param last_updated: The last_updated of this JsonWebKey.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def n(self):
        """Gets the n of this JsonWebKey.  # noqa: E501


        :return: The n of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this JsonWebKey.


        :param n: The n of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._n = n

    @property
    def status(self):
        """Gets the status of this JsonWebKey.  # noqa: E501


        :return: The status of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JsonWebKey.


        :param status: The status of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def use(self):
        """Gets the use of this JsonWebKey.  # noqa: E501


        :return: The use of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this JsonWebKey.


        :param use: The use of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._use = use

    @property
    def x5c(self):
        """Gets the x5c of this JsonWebKey.  # noqa: E501


        :return: The x5c of this JsonWebKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._x5c

    @x5c.setter
    def x5c(self, x5c):
        """Sets the x5c of this JsonWebKey.


        :param x5c: The x5c of this JsonWebKey.  # noqa: E501
        :type: list[str]
        """

        self._x5c = x5c

    @property
    def x5t(self):
        """Gets the x5t of this JsonWebKey.  # noqa: E501


        :return: The x5t of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x5t

    @x5t.setter
    def x5t(self, x5t):
        """Sets the x5t of this JsonWebKey.


        :param x5t: The x5t of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x5t = x5t

    @property
    def x5t_s256(self):
        """Gets the x5t_s256 of this JsonWebKey.  # noqa: E501


        :return: The x5t_s256 of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x5t_s256

    @x5t_s256.setter
    def x5t_s256(self, x5t_s256):
        """Sets the x5t_s256 of this JsonWebKey.


        :param x5t_s256: The x5t_s256 of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x5t_s256 = x5t_s256

    @property
    def x5u(self):
        """Gets the x5u of this JsonWebKey.  # noqa: E501


        :return: The x5u of this JsonWebKey.  # noqa: E501
        :rtype: str
        """
        return self._x5u

    @x5u.setter
    def x5u(self, x5u):
        """Sets the x5u of this JsonWebKey.


        :param x5u: The x5u of this JsonWebKey.  # noqa: E501
        :type: str
        """

        self._x5u = x5u

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
        if issubclass(JsonWebKey, dict):
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
        if not isinstance(other, JsonWebKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
