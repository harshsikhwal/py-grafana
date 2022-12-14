from py_grafana.base import Base


class AdminAPI(Base):
    def __init__(self, parent):
        super(AdminAPI, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def fetch_settings(self):
        # GET /api/admin/settings
        slug = "/api/admin/settings"
        return self._fetch(slug, token=self.basic_token)

    def update_settings(self, settings: dict):
        """
        Updates the Grafana settings. Currently, it only supports updates on the auth.saml section.
        :param settings: A settings dictionary
        """
        # PUT /api/admin/settings
        slug = "/api/admin/settings"
        return self._put(slug, settings, token=self.basic_token)

    def fetch_grafana_stats(self):
        # GET /api/admin/stats
        slug = "/api/admin/stats"
        return self._fetch(slug, token=self.basic_token)

    def fetch_grafana_usage_report_preview(self):
        # GET /api/admin/usage-report-preview
        slug = "/api/admin/usage-report-preview"
        return self._fetch(slug, token=self.basic_token)

    def create_global_user(self, user):
        # POST /api/admin/users
        slug = "/api/admin/users"

        user_dict = self._create(slug, user.obj_to_dict(), token=self.basic_token)
        if user_dict is not None:
            user.dict_to_obj(user_dict)
            return user
        else:
            return None


    def change_user_password(self, user):
        # PUT /api/admin/users/:id/password
        slug = "/api/admin/users/" + str(user.id) + "/password"
        password = {"password": user.password}

        return self._put(slug, password, token=self.basic_token)

    def change_user_permissions(self, user, permissions):
        # PUT /api/admin/users/:id/permissions
        slug = "/api/admin/users/" + str(user.id) + "/permissions"
        return self._put(slug, permissions, token=self.basic_token)

    def change_user_permissions_by_id(self, user_id, permissions):
        # PUT /api/admin/users/:id/permissions
        slug = "/api/admin/users/" + str(user_id) + "/permissions"
        return self._put(slug, permissions, token=self.basic_token)

    def delete_user(self, user):
        # DELETE /api/admin/users/:id
        slug = "/api/admin/users/" + str(user.id)
        return self._remove(slug, token=self.basic_token)

    def delete_user_by_id(self, user_id):
        # DELETE /api/admin/users/:id
        slug = "/api/admin/users/" + str(user_id)
        return self._remove(slug, token=self.basic_token)

    def pause_all_alerts(self, pause: bool):
        # POST /api/admin/pause-all-alerts
        slug = "/api/admin/pause-all-alerts"
        payload = {"paused": pause}
        return self._create(slug, payload, token=self.basic_token)
