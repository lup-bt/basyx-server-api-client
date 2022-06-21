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

class Permission(object):
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
        'permission': 'Reference',
        'kind_of_permission': 'str'
    }

    attribute_map = {
        'permission': 'permission',
        'kind_of_permission': 'kindOfPermission'
    }

    def __init__(self, permission=None, kind_of_permission=None):  # noqa: E501
        """Permission - a model defined in Swagger"""  # noqa: E501
        self._permission = None
        self._kind_of_permission = None
        self.discriminator = None
        self.permission = permission
        self.kind_of_permission = kind_of_permission

    @property
    def permission(self):
        """Gets the permission of this Permission.  # noqa: E501


        :return: The permission of this Permission.  # noqa: E501
        :rtype: Reference
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this Permission.


        :param permission: The permission of this Permission.  # noqa: E501
        :type: Reference
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def kind_of_permission(self):
        """Gets the kind_of_permission of this Permission.  # noqa: E501


        :return: The kind_of_permission of this Permission.  # noqa: E501
        :rtype: str
        """
        return self._kind_of_permission

    @kind_of_permission.setter
    def kind_of_permission(self, kind_of_permission):
        """Sets the kind_of_permission of this Permission.


        :param kind_of_permission: The kind_of_permission of this Permission.  # noqa: E501
        :type: str
        """
        if kind_of_permission is None:
            raise ValueError("Invalid value for `kind_of_permission`, must not be `None`")  # noqa: E501
        allowed_values = ["Allow", "Deny", "NotApplicable", "Undefined"]  # noqa: E501
        if kind_of_permission not in allowed_values:
            raise ValueError(
                "Invalid value for `kind_of_permission` ({0}), must be one of {1}"  # noqa: E501
                .format(kind_of_permission, allowed_values)
            )

        self._kind_of_permission = kind_of_permission

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
        if issubclass(Permission, dict):
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
        if not isinstance(other, Permission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other