import Dashboard
import json
import requests
import Folder
import DataSource
import User
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

    def add_datasource(self, datasource):
        slug = "/api/datasources"
        url = self.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self.Authorization != "":
            headers["Authorization"] = self.Authorization
        if self.Authorization != "":
            headers["Authorization"] = self.Authorization
        response = requests.post(url, data=datasource.to_json(), headers=headers, verify=False)

        # TODO: add response error handling

        if response.status_code == 200:
            datasource.json_to_obj(response.json())
            self.Datasource[datasource.name] = datasource

    def delete_datasource(self, datasource_name="", datasource_id="", datasource_uid=""):

        slug = "/api/datasources/"
        if datasource_id != "":
            slug = slug + datasource_id
            for datasource in self.Datasources:
                if datasource.id == datasource_id:
                    datasource_name = datasource.name
                    break
        elif datasource_name != "":
            slug = slug + "name/" + datasource_name
        elif datasource_uid != "":
            slug = slug + "uid/" + datasource_uid
            for datasource in self.Datasources:
                if datasource.uid == datasource_uid:
                    datasource_name = datasource.name
                    break
        else:
            return

        url = self.Host + slug
        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self.Authorization != "":
            headers["Authorization"] = self.Authorization
        response = requests.delete(url, headers=headers, verify=False)
        # TODO: add error handling

        if response.status_code == 200:
            del self.Datasources[datasource_name]

    def create_folder(self, folder):
        slug = "/api/folders"
        url = self.Host + slug

        commit_json = {"uid": folder.uid, "title": folder.title}
        print(commit_json)

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self.Authorization != "":
            headers["Authorization"] = self.Authorization
        response = requests.post(url, data=commit_json, headers=headers, verify=False)

        # TODO: add response error handling

        if response.status_code == 200:
            folder_json = response.json()
            """
            {
              "id":1,
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
            }
            """
            if "id" in folder_json:
                folder.id = folder_json["id"]

            if "url" in folder_json:
                folder.url = folder_json["url"]

            if "hasAcl" in folder_json:
                folder.hasAcl = folder_json["hasAcl"]

            if "canSave" in folder_json:
                folder.canSave = folder_json["canSave"]

            if "canEdit" in folder_json:
                folder.canEdit = folder_json["canEdit"]

            if "canAdmin" in folder_json:
                folder.canAdmin = folder_json["canAdmin"]

            if "createdBy" in folder_json:
                folder.createdBy = folder_json["createdBy"]

            if "created" in folder_json:
                folder.created = folder_json["created"]

            if "updatedBy" in folder_json:
                folder.updatedBy = folder_json["updatedBy"]

            if "updated" in folder_json:
                folder.updated = folder_json["updated"]

            if "version" in folder_json:
                folder.version = folder_json["version"]

            self.Folders[folder.title] = folder

        # add more codes:
        """
            200 – Created
            400 – Errors (invalid json, missing or invalid fields, etc)
            401 – Unauthorized
            403 – Access Denied
            409 - Folder already exists
        """

    def delete_folder(self, folder_name):
        if folder_name in self.Folders:
            folder = self.Folders[folder_name]
            # get the slug
            slug = folder.url
            url = self.Host + slug
            headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
            if self.Authorization != "":
                headers["Authorization"] = self.Authorization
            response = requests.delete(url, headers=headers, verify=False)
            # TODO: add error handling

            if response.status_code == 200:
                print("Folder deleted successfully!")
                del self.Folders[folder_name]

    def get_folder_by_uid(self, folder):

        slug = "/api/folders/"
        url = self.Host + slug + folder.uid
        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self.Authorization != "":
            headers["Authorization"] = self.Authorization
        response = requests.get(url, headers=headers, verify=False)

        # TODO: add response error handling

        if response.status_code == 200:
            folder_json = response.json()
            """
            {
              "id":1,
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
            }
            """
            if "id" in folder_json:
                folder.id = folder_json["id"]

            if "url" in folder_json:
                folder.url = folder_json["url"]

            if "hasAcl" in folder_json:
                folder.hasAcl = folder_json["hasAcl"]

            if "canSave" in folder_json:
                folder.canSave = folder_json["canSave"]

            if "canEdit" in folder_json:
                folder.canEdit = folder_json["canEdit"]

            if "canAdmin" in folder_json:
                folder.canAdmin = folder_json["canAdmin"]

            if "createdBy" in folder_json:
                folder.createdBy = folder_json["createdBy"]

            if "created" in folder_json:
                folder.created = folder_json["created"]

            if "updatedBy" in folder_json:
                folder.updatedBy = folder_json["updatedBy"]

            if "updated" in folder_json:
                folder.updated = folder_json["updated"]

            if "version" in folder_json:
                folder.version = folder_json["version"]

            # overwrite the folder
            self.Folders[folder.title] = folder

    def update_folder(self):
        """
        JSON Body schema:
uid – Provide another unique identifier than stored to change the unique identifier.
title – The title of the folder.
version – Provide the current version to be able to update the folder. Not needed if overwrite=true.
overwrite – Set to true if you want to overwrite existing folder with newer version.
        :return:
        """
        pass

    def get_all_folders(self):
        # TODO need a way to retrieve General Folder
        slug = "/api/folders"
        url = self.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self.Authorization != "":
            headers["Authorization"] = self.Authorization
        response = requests.get(url, headers=headers, verify=False)

        if response.status_code == 200:
            folders = response.json()
            for folder_data in folders:
                """
                [
                    {
                        "id":1,
                        "uid": "nErXDvCkzz",
                        "title": "Department ABC"
                    },
                    {
                        "id":2,
                        "uid": "k3S1cklGk",
                        "title": "Department RND"
                    }
                ]"""

                folder = self.Folder()
                folder.id = folder_data["id"]
                folder.uid = folder_data["uid"]
                folder.title = folder_data["title"]

                # TODO Get all the attributes
                # self.Folders[folder.title] = folder
                self.get_folder_by_uid(folder)

    def print_folders(self):
        for folder in self.Folders:
            print(self.Folders[folder].__dict__)

    def get_dashboard_json(self, dashboard):
        """
        get_dashboard_json generates JSON from grafanalib Dashboard object
        :param dashboard - Dashboard() created via grafanalib
        """
        # grafanalib generates json which need to pack to "dashboard" root element
        return json.dumps({"dashboard": dashboard.to_json_data()}, sort_keys=True, indent=2)

    def commit_dashboard_to_grafana(self, dashboard, message, overwrite=False):

        slug = "/api/dashboards/db"
        url = self.Host + slug

        commit_json = {"dashboard": dashboard.to_json()}
        commit_json["message"] = message
        commit_json["overwrite"] = overwrite

        print(commit_json)

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self.Authorization != "":
            headers["Authorization"] = self.Authorization
        response = requests.post(url, data=commit_json, headers=headers, verify=False)
        # TODO: add error handling

        if response.status_code == 200:
            dashboard_json = response.json()
            """
            {
              "id": 7,
              "slug": "new-dashboard-4",
              "status": "success",
              "uid": "bEdjeXO4k",
              "url": "/d/bEdjeXO4k/new-dashboard-4",
              "version": 1
            }
            """
            if "id" in dashboard_json:
                dashboard.id = dashboard_json["id"]

            if "slug" in dashboard_json:
                dashboard.slug = dashboard_json["slug"]

            if "uid" in dashboard_json:
                dashboard.uid = dashboard_json["uid"]

            if "url" in dashboard_json:
                dashboard.url = dashboard_json["url"]

            if "version" in dashboard_json:
                dashboard.version = dashboard_json["version"]
