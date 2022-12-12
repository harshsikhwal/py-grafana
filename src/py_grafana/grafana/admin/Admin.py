from py_grafana.base import Base
from py_grafana.token import BasicToken


class AdminAPI(Base):
    def __init__(self, parent, basic_token: BasicToken):
        super(AdminAPI, self).__init__(parent)
        self.BasicToken = basic_token

    def fetch_settings(self):
        # GET /api/admin/settings
        slug = "/api/admin/settings"
        return self._connection.fetch(slug, token=self.BasicToken)

    def update_settings(self, settings: dict):
        # PUT /api/admin/settings
        slug = "/api/admin/settings"
        return self._connection.put(slug, settings, token=self.BasicToken)

    def fetch_grafana_stats(self):
        # GET /api/admin/stats
        slug = "/api/admin/stats"
        return self._connection.fetch(slug, token=self.BasicToken)

    def fetch_grafana_usage_report_preview(self):
        # GET /api/admin/usage-report-preview
        slug = "/api/admin/usage-report-preview"
        return self._connection.fetch(slug, token=self.BasicToken)

    def create_global_user(self, user):
        # POST /api/admin/users
        slug = "/api/admin/users"
        return self._connection.create(slug, user.to_dict(), token=self.BasicToken)

    def change_user_password_by_id(self, id, password):
        # PUT /api/admin/users/:id/password
        slug = "/api/admin/users/" + id + "/password"
        password = {"password": password}
        return self._connection.put(slug, password, token=self.BasicToken)

    def change_user_permissions_by_id(self, id, permissions):
        # PUT /api/admin/users/:id/permissions
        slug = "/api/admin/users/" + str(id) + "/permissions"
        return self._connection.put(slug, permissions, token=self.BasicToken)

    def delete_user_by_id(self, id):
        # DELETE /api/admin/users/:id
        slug = "/api/admin/users/" + str(id)
        return self._connection.delete(slug, token=self.BasicToken)

    def pause_all_alerts(self, pause: bool):
        # POST /api/admin/pause-all-alerts
        slug = "/api/admin/pause-all-alerts"
        payload = {"paused": pause}
        return self._connection.create(slug, payload, token=self.BasicToken)
