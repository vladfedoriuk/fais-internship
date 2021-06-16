from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidConfigurationName(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "There is no configuration class with such a name."
    default_code = "invalid_configuration_name"


class InvalidVersion(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "A version must be a positive integer"
    default_code = "invalid_version"


class InvalidRunId(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "There is no such run"
    default_code = "invalid_run_id"


class EmptyQueryset(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = "There are no data matched to extract"
    default_code = "empty_queryset"
