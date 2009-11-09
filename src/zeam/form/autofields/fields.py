
from zope import component
from grokcore import component as grok
import martian

from zeam.form.base import Fields
from zeam.form.base.interfaces import IFormCanvas


class form(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    default = IFormCanvas


class group(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    default = None


class AutoFields(object):
    """Create a list of automatic fields.
    """
    grok.baseclass()

    fields = Fields()

    def __new__(self, context):
        return self.fields


class FieldsCollector(object):
    """Collect AutoFields defined elsewhere.
    """

    def __init__(self, interface):
        self.interface = interface
        self.__cache = None

    def __get__(self, obj, type=None):
        if self.__cache is None:
            self.__cache = Fields(
                *component.subscribers((obj,), self.interface))
        return self.__cache

    def __set__(self, obj, value):
        raise AttributeError
