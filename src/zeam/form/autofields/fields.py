
from zope import component
import martian

from zeam.form.base import Fields
from zeam.form.base.interfaces import IFormCanvas

class group(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    validate = martian.validateInterfaceOrClass


class AutoFields(object):
    """Create a list of automatic fields.
    """
    martian.baseclass()

    fields = Fields()

    def __new__(self, context):
        return self.fields


class FieldsCollector(object):
    """Collect AutoFields defined elsewhere.
    """

    def __init__(self, interface):
        self.interface = interface
        self.key = '_autofields_%s' % interface.__identifier__

    def __get__(self, obj, type=None):
        cache = obj.__dict__.get(self.key, None)
        if cache is None:
            cache = Fields(
                *component.subscribers((obj,), self.interface))
            obj.__dict__[self.key] = cache
        return cache

    def __set__(self, obj, value):
        raise AttributeError
