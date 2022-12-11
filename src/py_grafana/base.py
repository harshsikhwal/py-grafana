

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

    def _create(self, url: str, payload: dict) -> dict:
        """
        This function basically creates a new object
        :param url: url of the object you want to create
        :param payload: properties of the object you want to create
        :return: response json
        """
        return self._connection.create(url, payload)

    def _remove(self, url: str):
        """
        This functions basically removes an exsisting object
        :param url:
        """
        self._connection.delete(url)
