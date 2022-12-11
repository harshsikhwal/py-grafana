class PyGrafanaError(Exception):
    """The base error class for all PyGrafana errors"""

    def __init__(self, message, status_code=None):
        self._message = message
        self._status_code = status_code

    @property
    def message(self):
        return self._message

    @property
    def status_code(self):
        return self._status_code

    def __str__(self):
        return self._message

    def __repr__(self):
        return self._message


class AccessDeniedException(PyGrafanaError):
    def __init__(self, message, status_code=None):
        super(AccessDeniedException, self).__init__(message, status_code)

class AttributeTypeErrorException(PyGrafanaError):
    def __init__(self, message, status_code=None):
        super(AttributeTypeErrorException, self).__init__(message, status_code)