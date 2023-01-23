import warnings
from py_grafana.baseAPI import Base
from py_grafana.base import BaseObj


class Dashboard(BaseObj):
    """A class that stores the dashboard data"""

    def __init__(self):
        """
        Dashboard initializer
        """
        self.editable = True
        self.fiscalYearStartMonth = 0
        self.graphTooltip = 0
        self.id = None
        self.links = []
        self.liveNow = False
        self.panels = {}
        self.schemaVersion = 37
        self.style = "dark"
        self.tags = []
        self.time = {
            "from": "now-6h",
            "to": "now"
        }
        self.templating = {
            "list": []
        }
        self.timepicker = {}
        self.timezone = "browser"
        self.title = None
        self.uid = None
        self.version = None
        self.weekStart = ""
        self.refresh = "25s"
        self.slug = ""
        self.url = ""

    def add_tag(self, tag):
        """
        Add a string tag to Tags
        :param tag: A string tag
        :return: None
        """
        self.tags.append(tag)

    def clear_tags(self):
        """
        Clears all the existing tags
        :return: None
        """
        self.tags.clear()

    def add_panel(self, panel):
        """
        Adds a Panel object to Grafana
        :param panel: Panel
        :return: Adds panel to the panel map
        """
        self.panels[panel.title] = [panel]

    def delete_panel(self, panel_title="", panel=None):
        """
        Deletes a panel from dashboard object
        Need to call update dashboard after execution
        :param panel_title: The panel title (optional)
        :param panel: The panel object (optional)
        :return: None
        """
        # TODO: add try catch?

        if panel_title != "":
            del self.panels[panel_title]
        elif panel is not None:
            del self.panels[panel.title]

    def dict_to_obj(self, dashboard_dict):
        """
        Converts a dict to object of Dashboard type
        :param dashboard_dict: the dict
        :return: deserializes the dict to object
        """
        for key in self.__dict__:
            if key in dashboard_dict:
                self.__dict__[key] = dashboard_dict[key]
        return self

    def obj_to_dict(self):
        # Serialize Panels
        return self.__dict__


class DashboardAPI(Base):
    """
    This API class provides APIs for operations regarding dashboards
    """

    def __init__(self, parent):
        super(DashboardAPI, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def create_dashboard(self, folder, dashboard: Dashboard):
        # POST /api/dashboards/db
        slug = "/api/dashboards/db"
        payload = {
            "folderUid": folder.uid,
            "dashBoard": {
                "id": dashboard.id,
                "uid": dashboard.uid,
                "title": dashboard.title,
                "version": dashboard.version,
                "refresh": dashboard.refresh
            }
        }

        dashboard_json = self._create(slug, token=self.basic_token, payload=payload)

        if dashboard_json is not None:

            if dashboard_json["status"] != "success":
                warnings.warn("Status for creation of dashboard was not success success:" + dashboard_json["status"])

            return Dashboard().dict_to_obj(dashboard_json)

    def fetch_dashboard_by_uid(self, uid: str) -> Dashboard:
        # GET /api/dashboards/uid/:uid
        slug = "/api/dashboards/uid/" + uid
        dashboard_json = self._fetch(slug, token=self.basic_token)
        if dashboard_json is not None and "dashboard" in dashboard_json:
            return Dashboard().dict_to_obj(dashboard_json["dashboard"])

    def fetch_home_dashboard(self):
        # GET /api/dashboards/home
        slug = "/api/dashboards/home"
        dashboard_json = self._fetch(slug, token=self.basic_token)

        if dashboard_json is not None and "dashboard" in dashboard_json:
            return Dashboard().dict_to_obj(dashboard_json["dashboard"])

    def delete_dashboard(self, dashboard):
        # DELETE /api/dashboards/uid/:uid
        slug = "/api/dashboards/uid/" + dashboard.uid
        return self._remove(slug, token=self.basic_token)

    def update_dashboard(self, folder, dashboard: Dashboard, commit_message: str, overwrite=True):
        # POST /api/dashboards/db

        slug = "/api/dashboards/db"
        dashboard_payload = dashboard.obj_to_dict()
        payload = {
            "folderUid": folder.uid,
            "dashBoard": dashboard_payload,
            "message": commit_message,
            "overwrite": overwrite
        }

        dashboard_json = self._create(slug, token=self.basic_token, payload=payload)

        if dashboard_json is not None:

            if dashboard_json["status"] != "success":
                warnings.warn("Status for update of dashboard was not success success:" + dashboard_json["status"])

            return Dashboard().dict_to_obj(dashboard_json)
