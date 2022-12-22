import pytest
from py_grafana import Folder

db = None


@pytest.mark.unittest
def test_fetch_home_dashboard(grafana):
    home_db = grafana.dashboard_api.fetch_home_dashboard()
    assert home_db.title == "Home"
    assert home_db.refresh == "25s"
    assert home_db.version == 0
    assert home_db.url == ""
    assert home_db.slug == ""


@pytest.mark.unittest
def test_create_dashboard(grafana):
    folder = Folder(title="unittest", uid="uZZZ")
    grafana.folders_api.create_folder(folder)
    grafana.dashboard_api.create_dashboard(folder, "new_db")
    global db
    db = grafana.folders["unittest"].dashboards["new_db"]
    assert db.title == "new_db"
    assert db.refresh == "25s"
    assert db.version == 1


@pytest.mark.unittest
def test_fetch_dashboard(grafana):
    global db
    assert db is not None
    fetched_db = grafana.dashboard_api.fetch_dashboard_by_uid(db.uid)
    assert fetched_db.title == "new_db"
    assert fetched_db.uid == db.uid
    assert fetched_db.id == db.id


@pytest.mark.unittest
def test_update_dashboard(grafana):
    global db
    assert db is not None
    db.refresh = 10
    folder = Folder(title="unittest", uid="uZZZ")
    folder.dashboards["new_db"] = db
    grafana.folders["unittest"] = folder
    grafana.dashboard_api.update_dashboard(db)
    update_db = grafana.dashboard_api.fetch_dashboard_by_uid(db.uid)
    assert update_db.title == "new_db"
    assert update_db.uid == db.uid
    assert update_db.id == db.id
    assert update_db.version == 2
    assert update_db.refresh == 10


@pytest.mark.unittest
def test_delete_dashboard(grafana):
    global db
    grafana.dashboard_api.delete_dashboard(db)
    try:
        grafana.dashboard_api.fetch_dashboard_by_uid(db.uid)
    except Exception as e:
        assert "Dashboard not found" in str(e)
    finally:
        # need to delete folder folder as well
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