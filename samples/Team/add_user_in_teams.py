from py_grafana import Grafana, BasicToken, Team

grafana = Grafana().connect("localhost", 3000)

bt = BasicToken("admin", "admin")

grafana.user_api.set_token(bt)


# Adding Team
org = grafana.organization_api.get_current_organization()
team = Team()
team.name = "team with members"
team.orgId = org.orgId

grafana.team_api.add_team(team)

users = grafana.user_api.fetch_users()


for user in users:
    grafana.team_api.add_user_in_team(team, user)
