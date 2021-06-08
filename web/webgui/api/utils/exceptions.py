from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidConfigurationName(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "There is no configuration class with such a name."
    default_code = "invalid_configuration_name"


class InvalidVersion(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "a version must be a positive integer"
    default_code = "invalid_version"
