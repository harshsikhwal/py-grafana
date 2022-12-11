from py_grafana.grafana.folder.Folder import FolderAPI
from py_grafana.grafana.datasource.DataSource import DataSourceAPI
from py_grafana.grafana.users.User import UserAPI
from py_grafana.base import Base
from py_grafana.connection import Connection
from base64 import b64encode

#TODO: shift to another location
class Authorization:
    def __init__(self):
        self.APIToken = None
        self.BasicToken = None


    def generate_basic_token(self, username, password):
        self.BasicToken = b64encode(username + ":" + password)

    def get_basic_token(self):
        if self.BasicToken != "" and self.BasicToken != None:
            return "Basic " + self.BasicToken

    def get_api_token(self):
        if self.APIToken != "" and self.APIToken != None:
            return "Bearer " + self.APIToken

class Grafana(Base):

    def __init__(self):
        super(Grafana, self).__init__(None)
        self._folders = {}
        self._data_sources = {}
        self._authorization = Authorization()

    @property
    def users_api(self) -> UserAPI:
        """
        Create the User API instance.
        :return: user api
        """
        return UserAPI(self)

    @property
    def folders_api(self) -> FolderAPI:
        """
        Create the Folder API instance.
        :return: folder api
        """
        return FolderAPI(self)

    @property
    def datasource_api(self) -> DataSourceAPI:
        """
        Create the Datasource API instance.
        :return: datasource api
        """
        return DataSourceAPI(self)

    def connect(self, ip: str, port: int):
        """
        Creates a connection with the grafana server
        :param ip: ip/hostname of the grafana server
        :param port: port at which the grafana server is running
        :return: returns Grafana object
        """
        self._connection = Connection(ip, port)
        return self
