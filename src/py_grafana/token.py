from base64 import b64encode


class Token:
    def __init__(self, token_type, token):
        self.TokenType = token_type
        self.Token = token

    def get_token_str(self):
        return self.TokenType + " " + self.Token


class BasicToken(Token):
    def __init__(self, username, password):
        b64 = (b64encode(bytes(username + ":" + password, 'utf-8'))).decode('utf-8')
        super(BasicToken, self).__init__("Basic", b64)


class BearerToken(Token):
    def __init__(self, token):
        super(BearerToken, self).__init__("Bearer", token)
