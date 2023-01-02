import warnings
from py_grafana.baseAPI import Base
from py_grafana.base import BaseObj


class Dashboard(BaseObj):
    """A class that stores the dashboard data"""

    def __init__(self, title, version=0, refresh="25s"):
        """ Dashboard initializer
        :param title: The title of the dashboard
        :param version: the version of the dashboard
        :param refresh: Refresh interval: decimal with suffix: ms, s, m, h, d
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
        self.title = title
        self.uid = None
        self.version = version
        self.weekStart = ""
        self.refresh = refresh
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


class DashboardAPI(Base):
    """
    This API class provides APIs for operations regarding dashboards
    """

    def __init__(self, parent):
        super(DashboardAPI, self).__init__(parent)

    def create_dashboard(self, folder, dashboard_title: str):
        """
            :folder: the folder object under which you want to create a dashboard
            :dashboard_title: the title for the new dashboard
            :"raises: warning if not status success and exception for rest issues
            :returns: DashboardAPI instance
        """

        slug = "/api/dashboards/db"
        dashboard = Dashboard(dashboard_title)
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

        dashboard_json = self._create(slug, payload)

        if dashboard_json is not None:

            if dashboard_json["status"] != "success":
                warnings.warn("Status for creation of dashboard was not success success:" + dashboard_json["status"])

            dashboard.dict_to_obj(dashboard_json)
            self.parent.folders[folder.title]._dashboards[dashboard.title] = dashboard

        return self

    def fetch_dashboard_by_uid(self, uid: str) -> Dashboard:
        """
        :uid: uid of the dashboard which you want
        :returns: the fetched dashboard with the uid provided or None
        :raises: exception if there is any problem with the rest call
        """
        slug = "/api/dashboards/uid/" + uid
        dashboard_json = self._fetch(slug)

        dashboard = None
        if dashboard_json is not None and "dashboard" in dashboard_json:
            meta_json = dashboard_json["meta"]
            dashboard_json = dashboard_json["dashboard"]
            dashboard = Dashboard(dashboard_json["title"])
            dashboard.dict_to_obj(dashboard_json)
            dashboard.dict_to_obj(meta_json)

            folder_title = meta_json["folderTitle"]
            if self.parent.folders.get(folder_title, None) is not None:
                folder = self.parent.folders[folder_title]
                if folder.dashboards.get(dashboard.title, None) is not None:
                    del folder.dashboards[dashboard.title]
                    folder.dashboards[dashboard.title] = dashboard

        return dashboard

    def fetch_home_dashboard(self):
        slug = "/api/dashboards/home"
        dashboard_json = self._fetch(slug)

        dashboard = None
        if dashboard_json is not None and "dashboard" in dashboard_json:
            meta_json = dashboard_json["meta"]
            dashboard_json = dashboard_json["dashboard"]
            dashboard = Dashboard(dashboard_json["title"])
            dashboard.dict_to_obj(dashboard_json)
            dashboard.dict_to_obj(meta_json)

        return dashboard

    def delete_dashboard(self, dashboard):
        slug = "/api/dashboards/uid/" + dashboard.uid
        self._remove(slug)

        for folder_name in self.parent.folders.keys():
            folder = self.parent.folders[folder_name]
            if folder.dashboards.get(dashboard.title, None) is not None:
                del folder.dashboards[dashboard.title]

        return self

    def update_dashboard(self, dashboard):
        """
        :dashboard: the update dashboard object which we want to update in the server
        """
        # finding the folder of the dashboard

        parent = None
        for folder_name in self.parent.folders.keys():
            folder = self.parent.folders[folder_name]
            if folder.dashboards.get(dashboard.title, None):
                parent = folder
                break

        if parent is not None:
            slug = "/api/dashboards/db"
            dashboard_payload = dashboard.__dict__
            payload = {
                "folderUid": parent.uid,
                "dashBoard": dashboard_payload,
                "message": "updating db",
                "overwrite": True
            }

            dashboard_json = self._create(slug, payload)

            if dashboard_json is not None:

                if dashboard_json["status"] != "success":
                    warnings.warn("Status for update of dashboard was not success success:" + dashboard_json["status"])

                dashboard.dict_to_obj(dashboard_json)
                parent.dashboards[dashboard.title] = dashboard

        return self


