import json
import requests


class Dashboard:
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
        self.uid: None
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

    def to_json(self):
        """
        Serializes the given object to json
        :return: Json of the object
        """
        return json.loads(
            json.dumps(self, default=lambda o: getattr(o, '__dict__', str(o)))
        )

    def dict_to_obj(self, j):
        """
        Converts a dict to object of Dashboard type
        :param j: the dict
        :return: deserializes the dict to object
        """
        self.__dict__ = json.loads(j)

    """
    Sample Response:
        "annotations":
        {
            "list":
            [
              {
                "builtIn": 1,
                "datasource":
                {
                  "type": "grafana",
                  "uid": "-- Grafana --"
                },
                "enable": true,
                "hide": true,
                "iconColor": "rgba(0, 211, 255, 1)",
                "name": "Annotations & Alerts",
                "target":
                {
                  "limit": 100,
                  "matchAny": false,
                  "tags": [],
                  "type": "dashboard"
                },
                "type": "dashboard"
                }
            ]
        },
        "editable": true,
        "fiscalYearStartMonth": 0,
        "graphTooltip": 0,
        "id": null,
        "links": [],
        "liveNow": false,
        "panels": [],
        "schemaVersion": 37,
        "style": "dark",
        "tags": [],
        "templating":
        {
            "list": []
        },
        "time":
        {
            "from": "now-6h",
            "to": "now"
        },
        "timepicker": {},
        "timezone": "",
        "title": "New dashboard",
        "uid": "C2Gxi_dVz",
        "version": 1,
        "weekStart": ""
    """

class DashboardAPI(object):

    def __init__(self, grafana):
        self._grafana = grafana

    def add_dashboard(self, dashboard, message, overwrite=False):

        slug = "/api/dashboards/db"
        url = self._grafana.Host + slug

        commit_json = {"dashboard": dashboard.to_json()}
        commit_json["message"] = message
        commit_json["overwrite"] = overwrite

        print(commit_json)

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._grafana.Authorization != "":
            headers["Authorization"] = self._grafana.Authorization
        response = requests.post(url, data=commit_json, headers=headers, verify=False)
        # TODO: add error handling

        if response.status_code == 200:
            dashboard_json = response.json()
            """
            {
              "id": 7,
              "slug": "new-dashboard-4",
              "status": "success",
              "uid": "bEdjeXO4k",
              "url": "/d/bEdjeXO4k/new-dashboard-4",
              "version": 1
            }
            """
            if "id" in dashboard_json:
                dashboard.id = dashboard_json["id"]

            if "slug" in dashboard_json:
                dashboard.slug = dashboard_json["slug"]

            if "uid" in dashboard_json:
                dashboard.uid = dashboard_json["uid"]

            if "url" in dashboard_json:
                dashboard.url = dashboard_json["url"]

            if "version" in dashboard_json:
                dashboard.version = dashboard_json["version"]
