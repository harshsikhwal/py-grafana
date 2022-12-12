

class Base(object):
    """
    This is the base class which includes connection info and all the shared operations across different modules
    of the py grafana lib, in future further more operations/properties can be added
    """
    __slots__ = (
        "_connection",
        "_parent",
    )

    def __init__(self, parent):
        self._parent = parent
        if self._parent is not None:
            self._connection = parent._connection

    @property
    def parent(self):
        """The parent object of the current object
        Returns
        -------
        - obj: The parent object of the current object or None if there is no parent for this object
        """
        return self._parent

    def _create(self, url_slug: str, payload: dict, token: None) -> dict:
        """
        This function creates a new object
        :param url_slug: url_slug of the object you want to create
        :param payload: properties of the object you want to create
        :param token: the token class passes: BasicToken, BearerToken
        :return: response json
        """
        return self._connection.create(url_slug, payload, token)

    def _remove(self, url_slug: str, token: None):
        """
        This functions deletes an existing object
        :param url_slug: url_slug of the object you want to delete
        :param token: the token class passes: BasicToken, BearerToken
        """
        return self._connection.delete(url_slug, token)
        
    def _fetch(self, url_slug: str, token: None):
        """
        This functions is used for GET operations
        :param url_slug: url_slug of the object you want to get
        :param token: the token class passes: BasicToken, BearerToken
        """
        return self._connection.fetch(url_slug, token)

    def _put(self, url_slug: str, payload: dict, token: None) -> dict:
        """
        A wrapper over PUT
        :param url_slug: url_slug of the object you want to create
        :param payload: properties of the object you want to create
        :param token: the token class passes: BasicToken, BearerToken
        :return: response json
        """
        return self._connection.put(url_slug, payload, token)

    def _patch(self, url_slug: str, payload: dict, token: None) -> dict:
        """
        A wrapper over PATCH
        :param url_slug: url_slug of the object you want to create
        :param payload: properties of the object you want to create
        :param token: the token class passes: BasicToken, BearerToken
        :return: response json
        """
        return self._connection.patch(url_slug, payload, token)
