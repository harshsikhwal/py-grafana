from py_grafana.baseAPI import Base
from py_grafana.grafana.users.User import User


class Organization:
    """A class that stores the Organization data"""

    def __init__(self):
        self.id = None
        self.name = None
        # TODO need an address class
        self.address = {}
        # TODO add teams map and user map

    def dict_to_obj(self, organization_dict):
        for key in self.__dict__:
            if key in organization_dict:
                self.__dict__[key] = organization_dict[key]
        return self

    def obj_to_dict(self):
        return self.__dict__


class AdminOrgAPIPool(Base):

    def __init__(self, parent):
        super(AdminOrgAPIPool, self).__init__(parent)
        self.basic_token = None

    def set_token(self, basic_token):
        self.basic_token = basic_token

    def get_organization(self, organization: Organization) -> Organization or None:
        # GET /api/orgs/:orgId
        slug = "/api/orgs/" + str(organization.id)
        organization_dict = self._fetch(slug, token=self.basic_token)

        if organization_dict is not None:
            return Organization().dict_to_obj(organization_dict)
        return None

    def get_organization_by_id(self, organization_id: int) -> Organization or None:
        # GET /api/orgs/:orgId
        slug = "/api/orgs/" + str(organization_id)
        organization_dict = self._fetch(slug, token=self.basic_token)

        if organization_dict is not None:
            return Organization().dict_to_obj(organization_dict)
        return None

    def get_organization_by_name(self, org_name: str) -> Organization:
        # GET /api/orgs/name/:orgName
        slug = "/api/orgs/name/" + org_name
        organization_dict = self._fetch(slug, token=self.basic_token)

        if organization_dict is not None:
            return Organization().dict_to_obj(organization_dict)
        return None

    def create_organization(self, organization: Organization):
        # POST /api/orgs
        slug = "/api/orgs"
        organization_dict = self._create(slug, organization.obj_to_dict(), token=self.basic_token)

        if organization_dict is not None:
            organization.id = organization_dict["orgId"]
            return organization
        return {}

    def fetch_all_organizations(self):
        # GET /api/orgs?perpage=10&page=1
        slug = "/api/orgs"
        organization_dict = self._fetch(slug, token=self.basic_token)

        organizations = []
        if organization_dict is not None:
            for org in organization_dict:
                organizations.append(Organization().dict_to_obj(org))
        return organizations

    def delete_organization_by_id(self, organization_id: int):
        # DELETE /api/orgs/:orgId
        slug = "/api/orgs/" + str(organization_id)
        return self._remove(slug, token=self.basic_token)

    def delete_organization(self, organization: Organization):
        # DELETE /api/orgs/:orgId
        slug = "/api/orgs/" + str(organization.id)
        return self._remove(slug, token=self.basic_token)

    def get_users_in_organization_by_id(self, org_id: int):
        # GET /api/orgs/:orgId/users
        slug = "/api/orgs/" + str(org_id) + "/users"
        user_dict = self._fetch(slug, token=self.basic_token)

        users = []
        if user_dict is not None:
            for user in user_dict:
                users.append(User().dict_to_obj(user))
        return users

    def get_users_in_organization(self, org):
        # GET /api/orgs/:orgId/users
        slug = "/api/orgs/" + str(org.id) + "/users"
        user_dict = self._fetch(slug, token=self.basic_token)

        users = []
        if user_dict is not None:
            for user in user_dict:
                users.append(User().dict_to_obj(user))
        return users

    def add_user_in_organization(self, org: Organization, user: User, role="Viewer"):
        # POST /api/orgs/:orgId/users
        slug = "/api/orgs/" + str(org.id) + "/users"

        loginOrEmail = user.email if user.email != "" and user.email is not None else user.name
        user_payload = {"loginOrEmail": loginOrEmail, "role": role}
        return self._create(slug, payload=user_payload, token=self.basic_token)

    def delete_user_in_organization(self, org: Organization, user: User):
        # DELETE /api/orgs/:orgId/users/:userId
        slug = "/api/orgs/" + str(org.id) + "/users/" + str(user.id)
        return self._remove(slug, token=self.basic_token)


class OrganizationAPI(Base):

    def __init__(self, parent):
        super(OrganizationAPI, self).__init__(parent)
        self.basic_token = None
        self._admin_api_pool_ = None

    @property
    def admin_api_pool(self) -> AdminOrgAPIPool:
        """
        Create the Admin Org API instance.
        :return: admin api
        """
        if self._admin_api_pool_ is None:
            self._admin_api_pool_ = AdminOrgAPIPool(self.parent)
        return self._admin_api_pool_

    def set_token(self, basic_token):
        self.basic_token = basic_token
        self.admin_api_pool.set_token(basic_token)

    def get_current_organization(self):
        # GET /api/org/
        slug = "/api/org/"
        organization_dict = self._fetch(slug, token=self.basic_token)

        if organization_dict is not None:
            return Organization().dict_to_obj(organization_dict)

    def get_all_users_in_current_organization(self):
        # GET /api/org/users
        slug = "/api/org/users"
        user_dict = self._fetch(slug, token=self.basic_token)

        users = []
        if user_dict is not None:
            for user in user_dict:
                users.append(User().dict_to_obj(user))
        return users

    def update_user_in_current_organization(self, user: User):
        # PATCH /api/org/users/:userId
        slug = "/api/org/users/" + str(user.id)
        return self._patch(slug, payload=user.obj_to_dict(), token=self.basic_token)

    def delete_user_in_current_organization_by_id(self, user_id: int):
        # DELETE /api/org/users/:userId
        slug = "/api/org/users/" + str(user_id)
        return self._remove(slug)

    def delete_user_in_current_organization(self, user: User):
        # DELETE /api/org/users/:userId
        slug = "/api/org/users/" + str(user.id)
        return self._remove(slug)

    def update_current_organization(self, organization: Organization):
        # PUT /api/org
        slug = "/api/org"
        payload = organization.obj_to_dict()
        return self._put(slug, payload=payload, token=self.basic_token)

    def add_user_in_current_organization(self, user: User, role="Viewer"):
        # POST /api/org/users
        slug = "/api/org/users"
        payload = {
            "role": role,
            "loginOrEmail": user.email
        }
        return self._put(slug, payload=payload, token=self.basic_token)
