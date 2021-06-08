from collections import namedtuple
from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidParametersName(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "There are no configuration class with such name."
    default_code = "invalid_configuration_name"


ResponseData = namedtuple(
    "ResponseData", ["http_status", "code", "message", "errors", "data"]
)
CodeData = namedtuple("CodeData", ["code", "text"])

CODE_404 = CodeData(404, "Item was not found.")
CODE_401 = CodeData(404, "Unauthorized.")
CODE_200 = CodeData(200, "OK.")
CODE_201 = CodeData(201, "Item was created")
CODE_204 = CodeData(204, "No data matched the parameters.")
