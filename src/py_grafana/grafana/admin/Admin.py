import json
from py_grafana.base import Base
import requests

class AdminAPI(Base):
    def __init__(self, parent):
        super(AdminAPI, self).__init__(parent)

    def fetch_settings(self):
        slug = "/api/admin/settings"
        url = self._connection.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._connection.Authorization is not None:
            if self._connection.Authorization.BasicToken is not None or self._connection.Authorization.BasicToken != "":
                headers["Authorization"] = self._connection.Authorization.get_basic_token()

        response = requests.get(url, headers=headers)

        # TODO: add response error handling

        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def update_settings(self):
        slug = "/api/admin/settings"
        # TODO Code for admin
        pass

    def fetch_grafana_stats(self):
        slug = "/api/admin/stats"
        url = self._connection.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._connection.Authorization is not None:
            if self._connection.Authorization.BasicToken is not None or self._connection.Authorization.BasicToken != "":
                headers["Authorization"] = self._connection.Authorization.get_basic_token()

        response = requests.get(url, headers=headers)

        # TODO: add response error handling

        if response.status_code == 200:
            return response.json()
        else:
            return {}


    def fetch_grafana_usage_report_preview(self):
        slug = "/api/admin/usage-report-preview"
        url = self._connection.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._connection.Authorization is not None:
            if self._connection.Authorization.BasicToken is not None or self._connection.Authorization.BasicToken != "":
                headers["Authorization"] = self._connection.Authorization.get_basic_token()

        response = requests.get(url, headers=headers)

        # TODO: add response error handling

        if response.status_code == 200:
            return response.json()
        else:
            return {}
        pass

    def create_global_user(self):
        slug = "/api/admin/users"
        pass

    def change_user_password_by_id(self, id, password):
        slug = "/api/admin/users/" + id + "/password"

    def change_user_permissions_by_id(self, id):
        slug = "/api/admin/users/" + id + "/permissions"

    def delete_user_by_id(self, id):
        slug = "/api/admin/users/" + id
        url = self._connection.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._connection.Authorization is not None:
            if self._connection.Authorization.BasicToken is not None or self._connection.Authorization.BasicToken != "":
                headers["Authorization"] = self._connection.Authorization.get_basic_token()

        response = requests.delete(url, headers=headers)

        # TODO: add response error handling

        if response.status_code == 200:
            return True
        else:
            return False

    def pause_all_alerts(self):
        slug = "/api/admin/pause-all-alerts"
        url = self._connection.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._connection.Authorization is not None:
            if self._connection.Authorization.BasicToken is not None or self._connection.Authorization.BasicToken != "":
                headers["Authorization"] = self._connection.Authorization.get_basic_token()

        payload = {"paused" : True}
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # TODO: add response error handling

        if response.status_code == 200:
            return True
        else:
            return False