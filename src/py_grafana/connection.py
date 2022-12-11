import requests
import json


class Connection(object):
    """
    This is the base class which maintains all the connection info and operation and stuff
    in future further more properties shared by all can
    """

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self._method = "http://"
        self._host = self._method + self._ip + ":" + str(self._port)
        self.headers = {"Accept": "application/json", 'Content-Type': 'application/json'}

    @property
    def host(self) -> str:
        return self._host

    def get_final_url(self, url: str) -> str:
        return self._host + url

    def process_response(self, response, op_type: str):
        if response.status_code == 200:
            return response.json()
        else:
            # TODO: need more finer exceptions
            raise Exception("error in rest operation " + op_type)

    def create(self, url, payload):
        response = requests.post(self.get_final_url(url), data=json.dumps(payload), headers=self.headers)
        return self.process_response(response, "POST")

    def delete(self, url):
        response = requests.delete(self.get_final_url(url), headers=self.headers, verify=False)
        self.process_response(response, "DELETE")
