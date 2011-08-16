
from zope import component
from zope.browser.interfaces import IBrowserView
from grokcore.component.util import sort_components
import martian

from zeam.form.base import Fields


class group(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    validate = martian.validateInterfaceOrClass


class AutoFields(object):
    """Create a list of automatic fields.
    """
    martian.baseclass()

    fields = Fields()

    def __init__(self, context, request):
        self.context = context
        self.request = request


class FieldsCollector(object):
    """Collect AutoFields defined elsewhere.
    """

    def __init__(self, interface):
        self.interface = interface
        self.key = '_autofields_%s' % interface.__identifier__

    def __get__(self, form, type=None):
        if form is None:
            return Fields()

        cache = form.__dict__.get(self.key, None)
        if cache is None and IBrowserView.providedBy(form):
            providers = component.subscribers(
                (form.context, form), self.interface)
            providers = sort_components(providers)
            cache = Fields(*(p.fields for p in providers))
            form.__dict__[self.key] = cache
        return cache

    def __set__(self, form, value):
        raise AttributeError
