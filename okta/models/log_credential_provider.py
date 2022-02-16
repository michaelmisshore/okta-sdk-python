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

from aenum import MultiValueEnum


class LogCredentialProvider(str, MultiValueEnum):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    OKTA_AUTHENTICATION_PROVIDER = "OKTA_AUTHENTICATION_PROVIDER"
    OKTA_CREDENTIAL_PROVIDER = "OKTA_CREDENTIAL_PROVIDER"
    RSA = "RSA"
    SYMANTEC = "SYMANTEC"
    GOOGLE = "GOOGLE"
    DUO = "DUO"
    YUBIKEY = "YUBIKEY"