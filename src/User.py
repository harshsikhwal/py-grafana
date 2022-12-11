import json
import requests


class User:
    """A class that stores the User data"""

    def __init__(self):
        """
          "id": "1",
          "email": "user@mygraf.com",
          "name": "admin",
          "login": "admin",
          "theme": "light",
          "orgId": 1,
          "isGrafanaAdmin": true,
          "isDisabled": true,
          "isExternal": false,
          "authLabels": [],
          "updatedAt": "2019-09-09T11:31:26+01:00",
          "createdAt": "2019-09-09T11:31:26+01:00",
          "avatarUrl": "",
        """

        self.id = None
        self.name = None
        self.login = None
        self.email = None
        self.theme = "light"
        self.orgId = None
        self.isAdmin = None
        self.isGrafanaAdmin = True
        self.isDisabled = None
        self.isExternal = False
        self.authLabels = []
        self.updatedAt = None
        self.avatarUrl = None
        self.lastSeenAt = None
        self.lastSeenAtAge = None

    def json_to_obj(self, user_json):
        self.id = user_json["id"]
        self.email = user_json["email"]
        self.name = user_json["name"]
        self.login = user_json["login"]
        self.theme = user_json["theme"]
        self.orgId = user_json["orgId"]
        self.isGrafanaAdmin = user_json["isGrafanaAdmin"]
        self.isDisabled = user_json["isDisabled"]
        self.isExternal = user_json["isExternal"]
        self.authLabels = user_json["authLabels"]
        self.updatedAt = user_json["updatedAt"]
        self.createdAt = user_json["createdAt"]
        self.avatarUrl = user_json["avatarUrl"]

    def to_json(self):
        user_json = {}
        if self.id is not None:
            user_json["id"] = self.id
        if self.name is not None:
            user_json["name"] = self.name
        if self.login is not None:
            user_json["login"] = self.login
        if self.email is not None:
            user_json["email"] = self.email
        if self.isAdmin is not None:
            user_json["isAdmin"] = self.isAdmin
        if self.isDisabled is not None:
            user_json["isDisabled"] = self.isDisabled
        if self.lastSeenAt is not None:
            user_json["lastSeenAt"] = self.lastSeenAt
        if self.lastSeenAtAge is not None:
            user_json["lastSeenAtAge"] = self.lastSeenAtAge
        if self.authLabels is not None:
            user_json["authLabels"] = self.authLabels
        return user_json


class UserAPI(object):

    def __init__(self, grafana):
        self._grafana = grafana

    def get_users(self):
        pass

    def get_user_by_username(self, username):
        slug = "/api/users/lookup?loginOrEmail="
        url = self._grafana.Host + slug + username

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._grafana.Authorization != "":
            headers["Authorization"] = self._grafana.Authorization

        response = requests.get(url, headers=headers)

        # TODO: add response error handling

        if response.status_code == 200:
            user_json = response.json()
            user = User()
            user.json_to_obj(user_json)
            return user

    def get_user_by_email(self, email):
        slug = "/api/users/lookup?loginOrEmail="
        url = self._grafana.Host + slug + email

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._grafana.Authorization != "":
            headers["Authorization"] = self._grafana.Authorization

        response = requests.get(url, headers=headers)

        # TODO: add response error handling

        if response.status_code == 200:
            user_json = response.json()
            user = User()
            user.json_to_obj(user_json)
            return user

    def get_user_by_id(self, id):
        slug = "/api/users"
        url = self._grafana.Host + slug + id

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._grafana.Authorization != "":
            headers["Authorization"] = self._grafana.Authorization

        response = requests.get(url, headers=headers)

        # TODO: add response error handling

        if response.status_code == 200:
            user_json = response.json()
            user = User()
            user.json_to_obj(user_json)
            return user