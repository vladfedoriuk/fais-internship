from collections import namedtuple

ResponseData = namedtuple('ResponseData', ['http_status', 'code', 'message', 'errors', 'data'])
CodeData = namedtuple('CodeData', ['code', 'text'])

CODE_405 = CodeData(405, 'Item was not found.')
CODE_200 = CodeData(200, 'OK.')
CODE_204 = CodeData(204, 'No data matched the parameters.')
