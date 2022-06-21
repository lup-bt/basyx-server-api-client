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

class PolicyAdministrationPoint(object):
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
        'local_access_control': 'AccessControl',
        'external_access_control': 'bool'
    }

    attribute_map = {
        'local_access_control': 'localAccessControl',
        'external_access_control': 'externalAccessControl'
    }

    def __init__(self, local_access_control=None, external_access_control=None):  # noqa: E501
        """PolicyAdministrationPoint - a model defined in Swagger"""  # noqa: E501
        self._local_access_control = None
        self._external_access_control = None
        self.discriminator = None
        if local_access_control is not None:
            self.local_access_control = local_access_control
        self.external_access_control = external_access_control

    @property
    def local_access_control(self):
        """Gets the local_access_control of this PolicyAdministrationPoint.  # noqa: E501


        :return: The local_access_control of this PolicyAdministrationPoint.  # noqa: E501
        :rtype: AccessControl
        """
        return self._local_access_control

    @local_access_control.setter
    def local_access_control(self, local_access_control):
        """Sets the local_access_control of this PolicyAdministrationPoint.


        :param local_access_control: The local_access_control of this PolicyAdministrationPoint.  # noqa: E501
        :type: AccessControl
        """

        self._local_access_control = local_access_control

    @property
    def external_access_control(self):
        """Gets the external_access_control of this PolicyAdministrationPoint.  # noqa: E501


        :return: The external_access_control of this PolicyAdministrationPoint.  # noqa: E501
        :rtype: bool
        """
        return self._external_access_control

    @external_access_control.setter
    def external_access_control(self, external_access_control):
        """Sets the external_access_control of this PolicyAdministrationPoint.


        :param external_access_control: The external_access_control of this PolicyAdministrationPoint.  # noqa: E501
        :type: bool
        """
        if external_access_control is None:
            raise ValueError("Invalid value for `external_access_control`, must not be `None`")  # noqa: E501

        self._external_access_control = external_access_control

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
        if issubclass(PolicyAdministrationPoint, dict):
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
        if not isinstance(other, PolicyAdministrationPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
