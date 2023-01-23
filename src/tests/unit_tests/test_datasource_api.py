import pytest
from py_grafana import DataSource, Token

@pytest.mark.unittest
def fetch_all_datasource(grafana):
    fetched_db = grafana.dashboard_api.fetch_dashboard_by_uid(db.uid)
    assert fetched_db.title == "new_db"
    assert fetched_db.uid == db.uid
    assert fetched_db.id == db.id


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



