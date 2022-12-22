
class DataSource:
    """A class that stores the DataSource data"""

    def __init__(self):
        self.id = None
        self.orgId = None
        self.uid = None
        self.name = None
        self.type = None
        self.typeLogoUrl = None
        self.access = None
        self.url = None
        self.password = None
        self.user = None
        self.database = None
        self.basicAuth = None
        self.isDefault = None
        self.jsonData = {}
        self.secureJsonData = {}
        self.readOnly = None

    def obj_to_dict(self):
        return self.__dict__

    def dict_to_obj(self, datasource_dict):
        """
        Converts a dict to Datasource object type
        :param datasource_dict: the datasource dict
        :return: None
        """

        for key in datasource_dict:
            json_dict = {}
            if key in self.__dict__:
                self.__dict__[key] = datasource_dict[key]
            else:
                json_dict[key] = datasource_dict[key]
        if json_dict is not None and len(json_dict) > 0:
            self.__dict__["jsonData"] = json_dict
