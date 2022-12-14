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

class MultiLanguageProperty(SubmodelElement):
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
        'value': 'list[LangString]',
        'value_id': 'Reference'
    }
    if hasattr(SubmodelElement, "swagger_types"):
        swagger_types.update(SubmodelElement.swagger_types)

    attribute_map = {
        'value': 'value',
        'value_id': 'valueId'
    }
    if hasattr(SubmodelElement, "attribute_map"):
        attribute_map.update(SubmodelElement.attribute_map)

    def __init__(self, value=None, value_id=None, *args, **kwargs):  # noqa: E501
        """MultiLanguageProperty - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._value_id = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if value_id is not None:
            self.value_id = value_id
        SubmodelElement.__init__(self, *args, **kwargs)

    @property
    def value(self):
        """Gets the value of this MultiLanguageProperty.  # noqa: E501


        :return: The value of this MultiLanguageProperty.  # noqa: E501
        :rtype: list[LangString]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MultiLanguageProperty.


        :param value: The value of this MultiLanguageProperty.  # noqa: E501
        :type: list[LangString]
        """

        self._value = value

    @property
    def value_id(self):
        """Gets the value_id of this MultiLanguageProperty.  # noqa: E501


        :return: The value_id of this MultiLanguageProperty.  # noqa: E501
        :rtype: Reference
        """
        return self._value_id

    @value_id.setter
    def value_id(self, value_id):
        """Sets the value_id of this MultiLanguageProperty.


        :param value_id: The value_id of this MultiLanguageProperty.  # noqa: E501
        :type: Reference
        """

        self._value_id = value_id

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
        if issubclass(MultiLanguageProperty, dict):
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
        if not isinstance(other, MultiLanguageProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
