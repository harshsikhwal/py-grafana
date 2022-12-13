import json
import requests
from py_grafana.base import Base

class User:
    """A class that stores the User data"""

    def __init__(self):
        self.id = None
        self.name = None
        self.login = None
        self.password = None
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

    def dict_to_obj(self, user_dict):
        for key in self.__dict__:
            if key in user_dict:
                self.__dict__[key] = user_dict[key]
        return self

    def obj_to_dict(self):
        return self.__dict__


class UserAPI(Base):

    def __init__(self, parent):
        super(UserAPI, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def fetch_users(self):
        """
        Returns a list of Users
        """
        # GET /api/users
        # TODO need a way for perpage?
        slug = "/api/users"
        user_dict = self._fetch(slug, token=self.basic_token)
        users = []
        if user_dict is not None:
            for user in user_dict:
                users.append(User().dict_to_obj(user))
        return users


    def get_user_by_id(self, id):
        # GET /api/users/:id
        slug = "/api/users/" + str(id)
        user_dict = self._fetch(slug, token=self.basic_token)
        if user_dict is not None:
            return User().dict_to_obj(user_dict)
        return {}


    def get_user_by_username(self, username):
        # GET /api/users/lookup?loginOrEmail=user@mygraf.com
        slug = "/api/users/lookup?loginOrEmail=" + username
        user_dict = self._fetch(slug, token=self.basic_token)
        if user_dict is not None:
            return User().dict_to_obj(user_dict)
        return {}

    def get_user_by_email(self, email):
        # GET /api/users/lookup?loginOrEmail=user@mygraf.com
        slug = "/api/users/lookup?loginOrEmail=" + email
        user_dict = self._fetch(slug, token=self.basic_token)
        if user_dict is not None:
            return User().dict_to_obj(user_dict)
        return {}


    def update_user_by_id(self, id, user):
        # PUT /api/users/:id
        slug = "/api/users/" + str(id)
        return self._put(slug, payload=user.obj_to_dict(), token=self.basic_token)

    # def get_organisation_for_user_by_id(self, id):
    #     # GET /api/users/:id/orgs
    #     slug = "/api/users/" + str(id) + "/orgs"
    #     user_dict = self._fetch(slug, token=self.basic_token)
    #     if user_dict is not None:
    #         return User().dict_to_obj(user_dict)
    #     return {}