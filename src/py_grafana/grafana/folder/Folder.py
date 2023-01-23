from py_grafana.baseAPI import Base
from py_grafana.base import BaseObj
from py_grafana.grafana.dashboard.Dashboard import Dashboard
from typing import Dict


class Folder(BaseObj):
    """A class that stores the Folder data."""
    def __init__(self):
        """
        Folder initializer
        :param title: The name of the folder. This is required
        :param uid: The uid. User has a choice to give his own uid.
        """
        self.id = None
        self.uid = None
        self.title = None
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

    def dict_to_obj(self, folder_dict):
        for key in self.__dict__:
            if key in folder_dict:
                self.__dict__[key] = folder_dict[key]
        return self

    def obj_to_dict(self):
        return self.__dict__


class FolderAPI(Base):

    def __init__(self, parent):
        super(FolderAPI, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def create_folder(self, folder: Folder):
        # POST /api/folders
        slug = "/api/folders"
        payload = {"uid": folder.uid, "title": folder.title}

        folder_json = self._create(slug, payload, token=self.basic_token)
        if folder_json is not None:
            return Folder().dict_to_obj(folder_json)

        return self

    def delete_folder(self, folder: Folder):
        # DELETE /api/folders/:uid
        slug = "/api/folders/" + folder.uid
        return self._remove(slug, token=self.basic_token)

    def get_folder_by_uid(self, uid: str):
        # GET /api/folders/:uid
        slug = "/api/folders/" + uid

        folder_json = self._fetch(slug, token=self.basic_token)
        if folder_json is not None:
            return Folder().dict_to_obj(folder_json)

    def get_folder_by_id(self, folder_id: int):
        # GET /api/folders/id
        slug = "/api/folders/id/" + str(folder_id)

        folder_json = self._fetch(slug, token=self.basic_token)
        if folder_json is not None:
            return Folder().dict_to_obj(folder_json)

    def update_folder(self, folder: Folder):
        # PUT /api/folders/:uid
        slug = "/api/folders/" + folder.uid
        payload = folder.obj_to_dict()
        folder_json = self._put(slug, payload=payload, token=self.basic_token)
        if folder_json is not None:
            return Folder().dict_to_obj(folder_json)


    def get_all_folders(self):
        # GET /api/folders
        slug = "/api/folders"

        folders_json = self._fetch(slug, token=self.basic_token)

        folders = []
        if folders_json is not None:
            for folder in folders_json:
                folders.append(Folder().dict_to_obj(folder))
        return folders

