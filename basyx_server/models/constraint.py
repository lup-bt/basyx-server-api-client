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

class Constraint(object):
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
        'model_type': 'ModelType'
    }

    attribute_map = {
        'model_type': 'modelType'
    }

    def __init__(self, model_type=None):  # noqa: E501
        """Constraint - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self.discriminator = None
        self.model_type = model_type

    @property
    def model_type(self):
        """Gets the model_type of this Constraint.  # noqa: E501


        :return: The model_type of this Constraint.  # noqa: E501
        :rtype: ModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this Constraint.


        :param model_type: The model_type of this Constraint.  # noqa: E501
        :type: ModelType
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

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
        if issubclass(Constraint, dict):
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
        if not isinstance(other, Constraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
