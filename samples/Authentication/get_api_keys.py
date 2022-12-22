from py_grafana import Grafana, Token

token = Token.BearerToken("eyJrIjoienZHR3pwclgyOXRmSWU3R2owa1VRUzVJY0Q1MXlIalUiLCJuIjoiYXNkIiwiaWQiOjF9")

grafana = Grafana().connect("localhost", 3000, token)

api_keys = grafana.authentication_api.get_api_keys()

for key in api_keys:
    print(key.obj_to_dict())