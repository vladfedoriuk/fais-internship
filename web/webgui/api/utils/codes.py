from collections import namedtuple
from rest_framework import status

ResponseData = namedtuple(
    "ResponseData", ["http_status", "code", "message", "errors", "data"]
)
CodeData = namedtuple("CodeData", ["code", "text"])

CODE_400 = CodeData(400, "Invalid request.")
CODE_404 = CodeData(404, "Item was not found.")
CODE_401 = CodeData(401, "Unauthorized.")
CODE_200 = CodeData(200, "OK.")
CODE_201 = CodeData(201, "Item was created")
CODE_204 = CodeData(204, "No data matched the parameters.")
