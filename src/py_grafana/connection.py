

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

    @property
    def host(self) -> str:
        return self._host
