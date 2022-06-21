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
from basyx_server.models.submodel_element import SubmodelElement  # noqa: F401,E501

class File(SubmodelElement):
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
        'value': 'str',
        'mime_type': 'str'
    }
    if hasattr(SubmodelElement, "swagger_types"):
        swagger_types.update(SubmodelElement.swagger_types)

    attribute_map = {
        'value': 'value',
        'mime_type': 'mimeType'
    }
    if hasattr(SubmodelElement, "attribute_map"):
        attribute_map.update(SubmodelElement.attribute_map)

    def __init__(self, value=None, mime_type=None, *args, **kwargs):  # noqa: E501
        """File - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._mime_type = None
        self.discriminator = None
        self.value = value
        self.mime_type = mime_type
        SubmodelElement.__init__(self, *args, **kwargs)

    @property
    def value(self):
        """Gets the value of this File.  # noqa: E501


        :return: The value of this File.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this File.


        :param value: The value of this File.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def mime_type(self):
        """Gets the mime_type of this File.  # noqa: E501


        :return: The mime_type of this File.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this File.


        :param mime_type: The mime_type of this File.  # noqa: E501
        :type: str
        """
        if mime_type is None:
            raise ValueError("Invalid value for `mime_type`, must not be `None`")  # noqa: E501

        self._mime_type = mime_type

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
        if issubclass(File, dict):
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
        if not isinstance(other, File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
