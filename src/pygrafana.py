import Dashboard
import json
import requests
from Folder import FolderAPI
from DataSource import DataSourceAPI
from User import UserAPI
import Errors


class Grafana:

    def __init__(self, ip, port):
        self.IP = ip
        self.Port = port
        self.Connection = "http://"
        self.Host = self.Connection + self.IP + ":" + self.Port
        self.Folders = {}
        self.Datasources = {}
        self.Authorization = ""

    def users_api(self) -> UserAPI:
        """
        Create the User API instance.
        :return: user api
        """
        return UserAPI(self)

    def folders_api(self) -> FolderAPI:
        """
        Create the Folder API instance.
        :return: folder api
        """
        return FolderAPI(self)

    def datasource_api(self) -> DataSourceAPI:
        """
        Create the Datasource API instance.
        :return: datasource api
        """
        return DataSourceAPI(self)

