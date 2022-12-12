from py_grafana.base import Base
from py_grafana.token import BearerToken


class Authentication:
    def __init__(self, name, role, seconds_to_live=0):
        self.id = None
        self.name = name
        self.role = role
        self.seconds_to_live = seconds_to_live

    def set_token(self, token):
        self.token = token

    def dict_to_obj(self, authentication_dict):
        for key in self.__dict__:
            if key in authentication_dict:
                self.__dict__[key] = authentication_dict[key]

        if "key" in authentication_dict:
            token = BearerToken(authentication_dict["key"])
            self.token = token

    def obj_to_dict(self):
        return self.__dict__


class AuthenticationAPI(Base):
    def __init__(self, parent):
        super(AuthenticationAPI, self).__init__(parent)

    def get_api_keys(self):
        # GET /api/auth/keys
        slug = "/api/auth/keys"
        return self._connection.fetch(slug)

    def create_api_key(self, auth: Authentication):
        # POST /api/auth/keys
        slug = "/api/auth/keys"
        api_key = self._connection.create(slug, auth.obj_to_dict())
        if api_key is not None:
            token = BearerToken(api_key["key"])
            auth.set_token(token)
            return True
        else:
            return False

    def delete_api_key_by_id(self, id):
        # DELETE /api/auth/keys/:id
        slug = "/api/auth/keys/" + str(id)
        return self._connection.delete(slug)
