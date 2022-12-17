from py_grafana.baseAPI import Base
from py_grafana.grafana.users.User import User

class Team:
    """A class that stores the Team data"""
    def __init__(self):
        self.id = None
        self.orgId = None
        self.name = None
        self.email = None
        self.avatarUrl = None
        self.memberCount = None
        self.created = None
        self.updated = None
        self.theme = None
        self.homeDashboardId = None
        self.timezone = None

    def dict_to_obj(self, team_dict):
        for key in self.__dict__:
            if key in team_dict:
                self.__dict__[key] = team_dict[key]
        return self

    def obj_to_dict(self):
        return self.__dict__


class TeamAPI(Base):

    def __init__(self, parent):
        super(TeamAPI, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def fetch_teams(self) -> [Team]:
        """
        Returns a list of teams
        """
        # GET /api/teams/search
        # TODO need a way for perpage?
        slug = "/api/teams/search"
        team_dict = self._fetch(slug, token=self.basic_token)
        teams = []
        if team_dict is not None:
            for team in team_dict["teams"]:
                teams.append(Team().dict_to_obj(team))
        return teams

    def get_team_by_id(self, id) -> Team:
        # GET /api/teams/:id
        slug = "/api/teams/" + str(id)
        team_dict = self._fetch(slug, token=self.basic_token)
        if team_dict is not None:
            return Team().dict_to_obj(team_dict)
        return None

    def add_team(self, team):
        # POST /api/teams
        slug = "/api/teams/"
        success_json = self._create(slug, team.obj_to_dict(), token=self.basic_token)
        if success_json is not None:
            team.id = success_json["teamId"]

    def delete_team(self, team):
        # DELETE /api/teams/:id
        slug = "/api/teams/" + str(team.id)
        return self._remove(slug, token=self.basic_token)

    def get_team_members(self, team) -> User or None:
        # GET /api/teams/:teamId/members
        slug = "/api/teams/" + str(team.id) + "/members"
        user_dict = self._fetch(slug, token=self.basic_token)

        users = []
        if user_dict is not None:
            for user in user_dict:
                users.append(User().dict_to_obj(user))
        return users

    def add_user_in_team(self, team: Team, user: User):
        # POST /api/teams/:teamId/members
        slug = "/api/teams/" + str(team.id) + "/members"
        user_payload = {"userId" : user.id}
        return self._create(slug, payload=user_payload, token=self.basic_token)

    def delete_user_in_team(self, team: Team, user: User):
        # DELETE /api/teams/:teamId/members/:userId
        slug = "/api/teams/" + str(team.id) + "/members/" + str(user.id)
        return self._remove(slug, token=self.basic_token)

    def get_team_preference(self, team) -> Team:
        # GET /api/teams/:teamId/preferences
        slug = "/api/teams/" + str(team.id) + "/preferences"
        team_preference_dict = self._fetch(slug, token=self.basic_token)
        if team_preference_dict is not None:
            return team.dict_to_obj(team_preference_dict)
        else:
            return team

    def update_team_preference(self, team):
        # PUT /api/teams/:teamId/preferences
        slug = "/api/teams/" + str(team.id) + "/preferences"
        # TODO need to check if the PUT takes the whole team object
        payload = team.obj_to_dict()
        return self._put(slug, payload=payload, token=self.basic_token)




