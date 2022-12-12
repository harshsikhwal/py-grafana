from py_grafana.grafana.folder.Folder import FolderAPI
from py_grafana.grafana.datasource.DataSource import DataSourceAPI
from py_grafana.grafana.users.User import UserAPI
from py_grafana.base import Base
from py_grafana.connection import Connection
from py_grafana.grafana.admin.Admin import AdminAPI
from py_grafana.grafana.authentication.Authentication import AuthenticationAPI


class Grafana(Base):

    def __init__(self):
        super(Grafana, self).__init__(None)
        self._folders = {}
        self._data_sources = {}

    @property
    def admin_api(self) -> AdminAPI:
        """
        Create the Admin API instance.
        :return: admin api
        """
        return AdminAPI(self)

    @property
    def authentication_api(self) -> AuthenticationAPI:
        """
        Create the Authentication API instance.
        :return: authentication api
        """
        return AuthenticationAPI(self)

    @property
    def datasource_api(self) -> DataSourceAPI:
        """
        Create the Datasource API instance.
        :return: datasource api
        """
        return DataSourceAPI(self)

    @property
    def folders_api(self) -> FolderAPI:
        """
        Create the Folder API instance.
        :return: folder api
        """
        return FolderAPI(self)

    @property
    def users_api(self) -> UserAPI:
        """
        Create the User API instance.
        :return: user api
        """
        return UserAPI(self)

    def connect(self, ip: str, port: int, auth=None):
        """
        Creates a connection with the grafana server
        :param ip: ip/hostname of the grafana server
        :param port: port at which the grafana server is running
        :return: returns Grafana object
        """
        self._connection = Connection(ip, port, auth)
        return self
