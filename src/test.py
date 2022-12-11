import pygrafana
from Folder import Folder
from enum import Enum
import Errors

grafana = pygrafana.Grafana("localhost", "3000")

folder = Folder(title="nf", uid="nf")

folder = grafana.folders_api().create_folder(folder)

folder = grafana.folders_api().create_folder_by_name("new folder")


grafana.Folder[folder.title] = folder


user = grafana.users_api().get_user_by_username("vb")

