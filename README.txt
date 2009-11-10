====================
zeam.form.autofields
====================

``zeam.form.autofields`` is able to collect fields definition for your
form. This enable you to create forms with a plugable list of fields.

.. contents::

Example
=======

You need first to define a group of fields. This will be just an
interface::

  >>> from zope.interface import Interface

  >>> class IReplyFields(Interface):
  ...    pass

Now you can define groups of fields::

  >>> from zeam.form import base, autofields

  >>> class ReplyInformation(autofields.AutoFields):
  ...     autofields.group(IReplyFields)
  ...     autofields.order(0)
  ...     fields = base.Fields(base.Field('Comment'))

  >>> class ReplyBlogInformation(autofields.AutoFields):
  ...     autofields.group(IReplyFields)
  ...     autofields.order(10)
  ...     fields = base.Fields(base.Field('Blog URL'))

And you will be able to use those fields on your form somewhere else::

  >>> class ReplyForm(base.Form):
  ...     fields = autofields.FieldsCollector(IReplyFields)

API
===

In addition to its API, ``zeam.form.autofields`` export the one of
``zeam.form.base``.

Classes
-------

``AutoFields``
   Base classes used to define a group of Fields to be included in a form.

Directives
----------

``group``
   Directive used on ``AutoFields`` which select for which group you
   whish to provide the fields for. A group is just a plain zope
   interface, that will be given as parameter to the
   ``FieldsCollector``.

``view``
   Directive used on ``AutoFields`` that will let you specify for
   which Form (or view) you whish to provide the fields for. This
   directive is not required, and default to ``IBrowserView``.

``order``
   Optional directive which let decide in wich order the fields will
   included at the end.

Properties
----------

``FieldsCollector``
   Property used to collect form Fields for you.

