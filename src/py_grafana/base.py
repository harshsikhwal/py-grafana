

class BaseObj(object):
    """
    A base class for all py-grafana objects
    """

    def __str__(self):
        object_str = ""
        object_str += "%s %s : \n" % (self.__class__.__name__, "Info")
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue
            object_str += "   %s: %s\n" % (key, str(value))
        return object_str

