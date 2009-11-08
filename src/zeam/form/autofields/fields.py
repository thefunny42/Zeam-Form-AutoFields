
from zope import components

from zeam.form.fields import Fields


class AutoFields(Fields):
    """Represent a list of automatic fields.
    """

    def __call__(self, context):
        return self


class FieldsCollector(object):
    """Collect AutoFields defined elsewhere.
    """

    def __init__(self, interface):
        self.interface = interface
        self.__cache = None

    def __get__(self, obj, type=None):
        if self.__cache is None:
            self.__cache =Fields(
                *components.subscribers((obj,), self.interface))
        return self.__cache

    def __set__(self, obj, value):
        raise AttributeError
