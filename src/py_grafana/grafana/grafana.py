from py_grafana.grafana.folder.Folder import FolderAPI
from py_grafana.grafana.datasource.DataSource import DataSourceAPI
from py_grafana.grafana.users.User import UserAPI
from py_grafana.base import Base
from py_grafana.connection import Connection
from py_grafana.grafana.admin.Admin import AdminAPI
from py_grafana.grafana.authentication.Authentication import AuthenticationAPI
from py_grafana.grafana.organization.Organization import OrganizationAPI
from py_grafana.grafana.team.Team import TeamAPI

class Grafana(Base):

    def __init__(self):
        super(Grafana, self).__init__(None)
        self._folders = {}
        self._data_sources = {}
        self._admin_api_ = None
        self._organization_api = None
        self._user_api = None
        self._team_api = None
        self._folder_api_ = None

    @property
    def admin_api(self) -> AdminAPI:
        """
        Create the Admin API instance.
        :return: admin api
        """
        if self._admin_api_ is None:
            self._admin_api_ = AdminAPI(self)
        return self._admin_api_

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
        if self._folder_api_ is None:
            self._folder_api_ = AdminAPI(self)
        return FolderAPI(self)

    @property
    def organization_api(self) -> OrganizationAPI:
        """
        Create the User API instance.
        :return: user api
        """
        if self._organization_api is None:
            self._organization_api = OrganizationAPI(self)
        return self._organization_api

    @property
    def team_api(self) -> TeamAPI:
        """
        Create the User API instance.
        :return: user api
        """
        if self._team_api is None:
            self._team_api = TeamAPI(self)
        return self._team_api

    @property
    def user_api(self) -> UserAPI:
        """
        Create the User API instance.
        :return: user api
        """
        if self._user_api is None:
            self._user_api = UserAPI(self)
        return self._user_api

    @property
    def folders(self):
        return self._folders

    def connect(self, ip: str, port: int, auth=None):
        """
        Creates a connection with the grafana server
        :param ip: ip/hostname of the grafana server
        :param port: port at which the grafana server is running
        :param auth: authentication to be used by Connecting
        :return: returns Grafana object
        """
        self._connection = Connection(ip, port, auth)
        return self
