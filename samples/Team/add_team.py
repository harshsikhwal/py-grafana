from py_grafana import Grafana, Team, Token

grafana = Grafana().connect("localhost", 3000)

bt = Token.BasicToken("admin", "admin")
grafana.organization_api.set_token(bt)

org = grafana.organization_api.get_current_organization()

team = Team()
team.name = "the best team"
team.orgId = org.orgId

bt = Token.BasicToken("admin", "admin")
grafana.team_api.set_token(bt)
grafana.team_api.add_team(team)
