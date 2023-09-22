class APIRequest:
    def __init__(self, endpoint):
        self._endpoint = endpoint
        self._headers = {}
        self._params = {}

    def set_header(self, key, value):
        self._headers[key] = value

    def set_param(self, key, value):
        self._params[key] = value

    def __str__(self):
        return f'Endpoint: {self._endpoint}, Headers: {self._headers}, Params: {self._params}'


class APIRequestBuilder:
    def __init__(self, endpoint):
        self.api_request = APIRequest(endpoint)

    def add_header(self, key, value):
        self.api_request.set_header(key, value)
        return self

    def add_param(self, key, value):
        self.api_request.set_param(key, value)
        return self

    def build(self):
        return self.api_request


# Usage
builder = APIRequestBuilder('/users')
custom_api_request = (builder.add_header('Authorization', 'Bearer token123')
                      .add_param('limit', '10')
                      .add_param('offset', '20')
                      .build())
print(custom_api_request)  # Outputs: Endpoint: /users, Headers: {'Authorization': 'Bearer token123'}, Params: {'limit': '10', 'offset': '20'}
