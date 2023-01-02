from py_grafana.grafana.folder.Folder import FolderAPI, Folder
from py_grafana.grafana.dashboard.Dashboard import DashboardAPI
from py_grafana.grafana.dashboard.panel.Panel import PanelAPI
from py_grafana.grafana.datasource.DataSourceAPI import DataSourceAPI
from py_grafana.grafana.users.User import UserAPI
from py_grafana.baseAPI import Base
from py_grafana.connection import Connection
from py_grafana.grafana.admin.Admin import AdminAPI
from py_grafana.grafana.authentication.Authentication import AuthenticationAPI
from py_grafana.grafana.organization.Organization import OrganizationAPI
from py_grafana.grafana.team.Team import TeamAPI
from typing import Dict


class Grafana(Base):

    def __init__(self):
        super(Grafana, self).__init__(None)
        self._folders = {}
        self._data_sources = {}
        self._admin_api_ = None
        self._datasource_api_ = None
        self._organization_api = None
        self._user_api = None
        self._team_api = None
        self._folder_api_ = None
        self._authentication_api_ = None
        self._dashboard_api_ = None
        self._panel_api_ = None

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
        if self._authentication_api_ is None:
            self._authentication_api_ = AuthenticationAPI(self)
        return self._authentication_api_

    @property
    def dashboard_api(self) -> DashboardAPI:
        """
        Create the DashBoard API instance.
        :return: dashboard api
        """
        if self._dashboard_api_ is None:
            self._dashboard_api_ = DashboardAPI(self)
        return self._dashboard_api_

    def datasource_api(self) -> DataSourceAPI:
        """
        Create the Datasource API instance.
        :return: datasource api
        """
        if self._datasource_api_ is None:
            self._datasource_api_ = DataSourceAPI(self)
        return self._datasource_api_

    @property
    def folders(self) -> Dict[str, Folder]:
        return self._folders

    @property
    def folders_api(self) -> FolderAPI:
        """
        Create the Folder API instance.
        :return: folder api
        """
        if self._folder_api_ is None:
            self._folder_api_ = FolderAPI(self)
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
    def panel_api(self) -> PanelAPI:
        """
        Create the User API instance.
        :return: user api
        """
        if self._panel_api_ is None:
            self._panel_api_ = PanelAPI(self)
        return self._panel_api_

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
