
from zope.browser.interfaces import IBrowserView
from zeam.form.base.datamanager import ObjectDataManager
from zeam.form.ztk.datamanager import makeGenericAdaptiveDataManager


class FieldsDataManager(object):
    """Manage data with auto fields.
    """

    def __init__(self, fields_name='fields'):
        self.fields_name = fields_name
        self.key = '_automanager_%s' % fields_name

    def __get__(self, form, type=None):
        if form is None:
            return ObjectDataManager()

        cache = form.__dict__.get(self.key, None)
        if cache is None and IBrowserView.providedBy(form):
            fields = getattr(form, self.fields_name)
            cache = makeGenericAdaptiveDataManager(*fields)
            form.__dict__[self.key] = cache
        return cache

    def __set__(self, form, value):
        raise AttributeError
