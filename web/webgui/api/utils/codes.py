from collections import namedtuple

ResponseData = namedtuple('ResponseData', ['http_status', 'code', 'message', 'errors', 'data'])
CodeData = namedtuple('CodeData', ['code', 'text'])

CODE_404 = CodeData(404, 'Item was not found.')
CODE_200 = CodeData(200, 'OK.')
CODE_204 = CodeData(204, 'No data matched the parameters.')
