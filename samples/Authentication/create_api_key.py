from py_grafana import Grafana, Token, APIKey

token = Token.BearerToken("eyJrIjoienZHR3pwclgyOXRmSWU3R2owa1VRUzVJY0Q1MXlIalUiLCJuIjoiYXNkIiwiaWQiOjF9")

grafana = Grafana().connect("localhost", 3000, token)

api_key = APIKey()
api_key.name = "new admin 2"
api_key.role = "admin"

print(grafana.authentication_api.create_api_key(api_key))

