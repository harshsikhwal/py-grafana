import pytest
from py_grafana import Folder


@pytest.mark.unittest
def test_create_folder(grafana):
    """
    This test basically checks the create folder api for py grafana
    """
    folder = Folder(title="unittest", uid="uZZZ")
    grafana.folders_api.create_folder(folder)
    assert len(grafana.folders) > 0
    assert grafana.folders["unittest"].uid == "uZZZ"
    assert grafana.folders["unittest"].id is not None


@pytest.mark.unittest
def test_get_all_folders(grafana):
    """
    This test basically checks the get all folders api call from py grafana
    """
    grafana._folders = {}
    grafana.folders_api.get_all_folders()
    assert len(grafana.folders) > 0
    assert "unittest" in grafana.folders.keys()


@pytest.mark.unittest
def test_delete_folder(grafana):
    """
    This test basically check the delete folder api call from py grafana
    """
    grafana.folders_api.get_all_folders()
    assert "unittest" in grafana.folders.keys()
    grafana.folders_api.delete_folder("unittest")
    assert "unittest" not in grafana.folders.keys()
    grafana.folders_api.get_all_folders()
    assert "unittest" not in grafana.folders.keys()


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