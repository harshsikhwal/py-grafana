from py_grafana import Grafana

grafana = Grafana().connect("localhost", 3000)

teams = grafana.team_api.fetch_teams()

for team in teams:
    print(team.obj_to_dict())
