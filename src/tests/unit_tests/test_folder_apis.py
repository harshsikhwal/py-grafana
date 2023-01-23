import pytest
from py_grafana import Folder, Token

def initial_cleanup(grafana):
    folders = grafana.folder_api.get_all_folders()
    for folder in folders:
        if folder.uid == "utfolder":
            grafana.folder_api.delete_folder(folder)

@pytest.mark.unittest
def test_create_and_get_folder(grafana):
    """
    This tests the create_folder,get_folder_by_uid and get_folder_by_id api of py_grafana package
    """
    bt = Token.BasicToken("admin", "admin")
    grafana.set_token_to_apis(bt)
    initial_cleanup(grafana)
    folder = Folder()
    folder.title = "utfolder"
    folder.uid = "utfolder"
    grafana.folder_api.create_folder(folder)

    # get folder by uid
    folder = grafana.folder_api.get_folder_by_uid("utfolder")
    assert folder.uid == "utfolder"
    assert folder.title == "utfolder"

    # get folder by id
    folder = grafana.folder_api.get_folder_by_id(folder.id)
    assert folder.uid == "utfolder"
    assert folder.title == "utfolder"

    # general cleanup
    grafana.folder_api.delete_folder(folder)

@pytest.mark.unittest
def test_update_folder(grafana):
    """
    This tests the update_folder api of py_grafana package
    """
    # setup
    bt = Token.BasicToken("admin", "admin")
    grafana.set_token_to_apis(bt)
    initial_cleanup(grafana)
    folder = Folder()
    folder.title = "utfolder"
    folder.uid = "utfolder"
    folder = grafana.folder_api.create_folder(folder)

    # test_get_all_folders
    folder.title = "new_ut_folder"
    grafana.folder_api.update_folder(folder)

    # get folder by id
    folder = grafana.folder_api.get_folder_by_id(folder.id)
    assert folder.title == "new_ut_folder"

    # general cleanup
    grafana.folder_api.delete_folder(folder)

@pytest.mark.unittest
def test_get_all_folders(grafana):
    """
    This tests the get_all_folders api of py_grafana package
    """
    # setup
    bt = Token.BasicToken("admin", "admin")
    grafana.set_token_to_apis(bt)
    folder = Folder()
    initial_cleanup(grafana)
    folder.title = "utfolder"
    folder.uid = "utfolder"
    grafana.folder_api.create_folder(folder)

    # test_get_all_folders
    folders = grafana.folder_api.get_all_folders()
    assert len(folders) > 0
    # general cleanup
    grafana.folder_api.delete_folder(folder)

@pytest.mark.unittest
def test_delete_folder(grafana):
    """
    This tests the delete_folder api api of py_grafana package
    """
    # setup
    bt = Token.BasicToken("admin", "admin")
    grafana.set_token_to_apis(bt)
    initial_cleanup(grafana)
    folder = Folder()
    folder.title = "utfolder"
    folder.uid = "utfolder"
    grafana.folder_api.create_folder(folder)

    # test_delete_folder
    grafana.folder_api.delete_folder(folder)

    folders = grafana.folder_api.get_all_folders()
    for folder in folders:
        assert "utfolder" != folder.title

if __name__ == "__main__":
    pytest.main(
        [
            "--server",
            "localhost",
            "--port",
            "3000",
            "-s",
            "-o",
            "log_cli=1",
            "-o",
            "log_cli_level=INFO",

            __file__,
        ]
    )
