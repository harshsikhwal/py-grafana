from py_grafana import Grafana, BasicToken, Team

grafana = Grafana().connect("localhost", 3000)

org = grafana.organization_api.get_current_organization()

team = Team()
team.name = "my new team"
team.orgId = org.orgId

grafana.team_api.add_team(team)
