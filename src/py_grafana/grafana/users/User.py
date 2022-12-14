from py_grafana.base import Base
# from py_grafana.grafana.organization.Organization import Organization
# from py_grafana.grafana.team.Team import Team

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

    def update_user(self, user):
        # PUT /api/users/:id
        slug = "/api/users/" + str(user.id)
        return self._put(slug, payload=user.obj_to_dict(), token=self.basic_token)

    # def get_organization_for_user(self, user):
    #     # GET /api/users/:id/orgs
    #     slug = "/api/users/" + str(user.id) + "/orgs"
    #     org_dict = self._fetch(slug, token=self.basic_token)
    #     organizations = []
    #     if org_dict is not None:
    #         for org in org_dict:
    #             organizations.append(Organization().dict_to_obj(org))
    #     return organizations
    #
    # def get_team_for_user(self, user):
    #     # GET /api/users/:id/teams
    #     slug = "/api/users/" + str(user.id) + "/teams"
    #     team_dict = self._fetch(slug, token=self.basic_token)
    #     teams = []
    #     if team_dict is not None:
    #         for team in team_dict:
    #             teams.append(Team().dict_to_obj(team))
    #     return teams

    # TODO need a better name for this function
    def get_actual_user(self):
        # GET /api/user
        slug = "/api/user"
        user_dict = self._fetch(slug, token=self.basic_token)
        if user_dict is not None:
            return User().dict_to_obj(user_dict)

    def star_dashboard(self, dashboard):
        # POST /api/user/stars/dashboard/:dashboardId
        slug = "/api/user/stars/dashboard/" + str(dashboard.id)
        message = self._put(slug, token=self.basic_token)
        if message is not None:
            if message["message"] == "Dashboard starred!":
                return True
        return False

    def unstar_dashboard(self, dashboard):
        # DELETE /api/user/stars/dashboard/:dashboardId
        slug = "/api/user/stars/dashboard/" + str(dashboard.id)
        message = self._remove(slug, token=self.basic_token)
        if message is not None:
            if message["message"] == "Dashboard unstarred":
                return True
        return False

