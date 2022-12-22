from py_grafana.baseAPI import Base
from py_grafana.base import BaseObj
from py_grafana.grafana.dashboard.Dashboard import Dashboard
from typing import Dict


class Folder(BaseObj):
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
        self._dashboards = {}

    @property
    def dashboards(self) -> Dict[str, Dashboard]:
        """
        returns a map which consists of all the dashboards
        map[dashboard_title]: dashboard object
        """
        return self._dashboards

    def dict_to_obj(self, folder_dict):
        """
        Converts a dict to object of Folder type
        :param folder_dict: the folder json object
        :return: deserializes the dict to object
        """
        for key in self.__dict__:
            if key in folder_dict:
                self.__dict__[key] = folder_dict[key]

    def obj_to_dict(self):
        return self.__dict__


class FolderAPI(Base):

    def __init__(self, parent):
        super(FolderAPI, self).__init__(parent)

    def create_folder(self, folder):
        slug = "/api/folders"
        payload = {"uid": folder.uid, "title": folder.title}

        folder_json = self._create(slug, payload)
        if folder_json is not None:
            folder = Folder(folder_json["title"])
            folder.dict_to_obj(folder_json)
            self.parent._folders[folder.title] = folder

        return self

    def delete_folder(self, folder_name):
        if folder_name in self.parent.folders.keys():
            folder = self.parent.folders[folder_name]
            slug = "/api/folders/" + folder.uid
            self._remove(slug)
            del self.parent.folders[folder_name]

        return self

    def get_folder_by_uid(self, uid: str):

        slug = "/api/folders/"
        slug = slug + uid

        folder_json = self._fetch(slug)
        updated_folder = Folder(folder_json["id"], folder_json["title"])
        updated_folder.dict_to_obj(folder_json)

        # overwrite the folder
        self.parent._folders[updated_folder.title] = updated_folder

        return self

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

        folders_json = self._fetch(slug)

        for folder_data in folders_json:
            folder = Folder(folder_data["title"])
            folder.dict_to_obj(folder_data)

            # TODO Get all the attributes
            self.parent._folders[folder.title] = folder

        return self

