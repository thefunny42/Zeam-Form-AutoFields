
from zope import component
from grokcore.viewlet.util import sort_components
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

    def __init__(self, context):
        self.context = context


class FieldsCollector(object):
    """Collect AutoFields defined elsewhere.
    """

    def __init__(self, interface):
        self.interface = interface
        self.key = '_autofields_%s' % interface.__identifier__

    def __get__(self, obj, type=None):
        if obj is None:
            return Fields()

        cache = obj.__dict__.get(self.key, None)
        if cache is None:
            providers = component.subscribers((obj,), self.interface)
            providers = sort_components(providers)
            cache = Fields(*(p.fields for p in providers))
            obj.__dict__[self.key] = cache
        return cache

    def __set__(self, obj, value):
        raise AttributeError
