import json

class Folder:
    """A class that stores the Folder data."""
    def __init__(self, title, uid=None):
        """
        Folder initializer
        :param title: The name of the folder. This is required
        :param uid: The uid. User has a choice to give his own uid.
        """
        self.id = None
        self.uid = uid
        self.title = title
        self.url = None
        self.hasAcl = False
        self.canSave = True
        self.canEdit = True
        self.canAdmin = True
        self.createdBy = None  # admin
        self.created = None  # time stamp
        self.updatedBy = None  # admin
        self.updated = None  # time stamp
        self.version = None  # not true
        self.Dashboards = {}
        # self.parent = parent

    def dict_to_obj(self, j):
        """
        Converts a dict to object of Folder type
        :param j: the dict
        :return: deserializes the dict to object
        """
        self.__dict__ = json.loads(j)

    # TODO def add_dashboard code here

    # TODO need a shared object for pygrafana

    """
    Sample Response:
        "id": 1,
        "uid": "nErXDvCkzz",
        "title": "Department ABC",
        "url": "/dashboards/f/nErXDvCkzz/department-abc",
        "hasAcl": false,
        "canSave": true,
        "canEdit": true,
        "canAdmin": true,
        "createdBy": "admin",
        "created": "2018-01-31T17:43:12+01:00",
        "updatedBy": "admin",
        "updated": "2018-01-31T17:43:12+01:00",
        "version": 1
    """

