import json
import requests

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

class FolderAPI(object):

    def __init__(self, grafana):
        self._grafana = grafana

    def create_folder(self, folder):
        slug = "/api/folders"
        url = self._grafana.Host + slug

        commit_json = {"uid": folder.uid, "title": folder.title}
        print(commit_json)

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._grafana.Authorization != "":
            headers["Authorization"] = self._grafana.Authorization
        response = requests.post(url, data=json.dumps(commit_json), headers=headers)

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

            self._grafana.Folders[folder.title] = folder
            return folder

        # add more codes:
        """
            200 – Created
            400 – Errors (invalid json, missing or invalid fields, etc)
            401 – Unauthorized
            403 – Access Denied
            409 - Folder already exists
        """

    def delete_folder(self, folder_name):
        if folder_name in self._grafana.Folders:
            folder = self._grafana.Folders[folder_name]
            # get the slug
            slug = folder.url
            url = self._grafana.Host + slug
            headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
            if self._grafana.Authorization != "":
                headers["Authorization"] = self._grafana.Authorization
            response = requests.delete(url, headers=headers, verify=False)
            # TODO: add error handling

            if response.status_code == 200:
                print("Folder deleted successfully!")
                del self._grafana.Folders[folder_name]

    def get_folder_by_uid(self, folder):

        slug = "/api/folders/"
        url = self._grafana.Host + slug + folder.uid
        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._grafana.Authorization != "":
            headers["Authorization"] = self._grafana.Authorization
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
            self._grafana.Folders[folder.title] = folder

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
        url = self._grafana.Host + slug

        headers = {"Accept": "application/json", 'Content-Type': 'application/json'}
        if self._grafana.Authorization != "":
            headers["Authorization"] = self._grafana.Authorization
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

                folder = self._grafana.Folder()
                folder.id = folder_data["id"]
                folder.uid = folder_data["uid"]
                folder.title = folder_data["title"]

                # TODO Get all the attributes
                # self.Folders[folder.title] = folder
                self._grafana.get_folder_by_uid(folder)

    def print_folders(self):
        for folder in self._grafana.Folders:
            print(self._grafana.Folders[folder].__dict__)
