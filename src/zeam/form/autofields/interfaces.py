
from zope import interface

from zeam.form.base.interfaces import IZeamFormBaseAPI


class IZeamFormAutoFieldsAPI(IZeamFormBaseAPI):
    """API exported by zeam.form.autofields.
    """

    AutoFields = interface.Attribute(
        u"A definition of fields to be collected")
    FieldsCollector = interface.Attribute(
        u"A property collecting auto fields for the given object")
    FieldsDataManager = interface.Attribute(
        u"A property that creates a adaptive data manager for auto fields")

    view = interface.Attribute(
        u"Directive to restrict to which object the fields are collected for")
    group = interface.Attribute(
        u"Directive to restrict to which group the fields are collected for")
    order = interface.Attribute(
        u"Directive to order autofields amongst themselves")
