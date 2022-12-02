import json
class User:
    """A class that stores the User data"""
    def __init__(self):
        """
        {
            "id": 1,
            "name": "Admin",
            "login": "admin",
            "email": "admin@mygraf.com",
            "isAdmin": true,
            "isDisabled": false,
            "lastSeenAt": "2020-04-10T20:29:27+03:00",
            "lastSeenAtAge': "2m",
            "authLabels": ["OAuth"]
        },"""

        self.id = None
        self.name = None
        self.login = None
        self.email = None
        self.isAdmin = None
        self.isDisabled = None
        self.lastSeenAt = None
        self.lastSeenAtAge = None
        self.authLabels = None

    def to_json(self):
        user_json = {}
        if self.id is not None:
            user_json["id"] = self.id
        if self.name is not None:
            user_json["name"] = self.name
        if self.login is not None:
            user_json["login"] = self.login
        if self.email is not None:
            user_json["email"] = self.email
        if self.isAdmin is not None:
            user_json["isAdmin"] = self.isAdmin
        if self.isDisabled is not None:
            user_json["isDisabled"] = self.isDisabled
        if self.lastSeenAt is not None:
            user_json["lastSeenAt"] = self.lastSeenAt
        if self.lastSeenAtAge is not None:
            user_json["lastSeenAtAge"] = self.lastSeenAtAge
        if self.authLabels is not None:
            user_json["authLabels"] = self.authLabels
        return user_json

