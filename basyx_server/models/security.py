# coding: utf-8

"""
    BaSyx Asset Administration Shell Repository HTTP REST-API

    The full description of the generic BaSyx Asset Administration Shell Repository HTTP REST-API  # noqa: E501

    OpenAPI spec version: v1
    Contact: constantin.ziesche@bosch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Security(object):
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
        'access_control_policy_points': 'AccessControlPolicyPoints',
        'certificate': 'list[OneOfSecurityCertificateItems]',
        'required_certificate_extension': 'list[Reference]'
    }

    attribute_map = {
        'access_control_policy_points': 'accessControlPolicyPoints',
        'certificate': 'certificate',
        'required_certificate_extension': 'requiredCertificateExtension'
    }

    def __init__(self, access_control_policy_points=None, certificate=None, required_certificate_extension=None):  # noqa: E501
        """Security - a model defined in Swagger"""  # noqa: E501
        self._access_control_policy_points = None
        self._certificate = None
        self._required_certificate_extension = None
        self.discriminator = None
        self.access_control_policy_points = access_control_policy_points
        if certificate is not None:
            self.certificate = certificate
        if required_certificate_extension is not None:
            self.required_certificate_extension = required_certificate_extension

    @property
    def access_control_policy_points(self):
        """Gets the access_control_policy_points of this Security.  # noqa: E501


        :return: The access_control_policy_points of this Security.  # noqa: E501
        :rtype: AccessControlPolicyPoints
        """
        return self._access_control_policy_points

    @access_control_policy_points.setter
    def access_control_policy_points(self, access_control_policy_points):
        """Sets the access_control_policy_points of this Security.


        :param access_control_policy_points: The access_control_policy_points of this Security.  # noqa: E501
        :type: AccessControlPolicyPoints
        """
        if access_control_policy_points is None:
            raise ValueError("Invalid value for `access_control_policy_points`, must not be `None`")  # noqa: E501

        self._access_control_policy_points = access_control_policy_points

    @property
    def certificate(self):
        """Gets the certificate of this Security.  # noqa: E501


        :return: The certificate of this Security.  # noqa: E501
        :rtype: list[OneOfSecurityCertificateItems]
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this Security.


        :param certificate: The certificate of this Security.  # noqa: E501
        :type: list[OneOfSecurityCertificateItems]
        """

        self._certificate = certificate

    @property
    def required_certificate_extension(self):
        """Gets the required_certificate_extension of this Security.  # noqa: E501


        :return: The required_certificate_extension of this Security.  # noqa: E501
        :rtype: list[Reference]
        """
        return self._required_certificate_extension

    @required_certificate_extension.setter
    def required_certificate_extension(self, required_certificate_extension):
        """Sets the required_certificate_extension of this Security.


        :param required_certificate_extension: The required_certificate_extension of this Security.  # noqa: E501
        :type: list[Reference]
        """

        self._required_certificate_extension = required_certificate_extension

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
        if issubclass(Security, dict):
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
        if not isinstance(other, Security):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
