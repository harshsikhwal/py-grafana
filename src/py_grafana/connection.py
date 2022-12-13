import requests
import json


class Connection(object):
    """
    This is the base class which maintains all the connection info and operation and stuff
    in future further more properties shared by all can
    """

    def __init__(self, ip, port, auth=None):
        self._ip = ip
        self._port = port
        self._method = "http://"
        self._host = self._method + self._ip + ":" + str(self._port)
        self.headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if auth is not None:
            self.headers["Authorization"] = auth.get_complete_token_as_string()

    @property
    def host(self) -> str:
        return self._host

    def construct_url(self, slug: str) -> str:
        return self._host + slug

    def process_response(self, response, op_type: str):
        if response.status_code == 200:
            if response.content != b'':
                return response.json()
        else:
            # TODO: need more finer exceptions
            print(response.content)
            raise Exception("Rest operation %s failed with status code %s" % (op_type, str(response.status_code)))

    def create(self, slug, payload, token=None):
        headers = self.headers.copy()
        if token is not None:
            headers["Authorization"] = token.get_token_str()
        response = requests.post(self.construct_url(slug), data=json.dumps(payload), headers=headers)
        return self.process_response(response, "POST")

    def delete(self, slug, token=None):
        headers = self.headers.copy()
        if token is not None:
            headers["Authorization"] = token.get_token_str()
        response = requests.delete(self.construct_url(slug), headers=headers, verify=False)
        self.process_response(response, "DELETE")

    def fetch(self, slug, token=None):
        headers = self.headers.copy()
        if token is not None:
            headers["Authorization"] = token.get_token_str()
        response = requests.get(self.construct_url(slug), headers=headers, verify=False)
        return self.process_response(response, "GET")

    def put(self, slug, payload, token=None):
        headers = self.headers.copy()
        if token is not None:
            headers["Authorization"] = token.get_token_str()

        response = requests.put(self.construct_url(slug), data=json.dumps(payload), headers=headers)

        return self.process_response(response, "PUT")

    def patch(self, slug, payload, token=None):
        headers = self.headers.copy()
        if token is not None:
            headers["Authorization"] = token.get_token_str()
        response = requests.patch(self.construct_url(slug), data=json.dumps(payload), headers=headers)

        return self.process_response(response, "PATCH")
