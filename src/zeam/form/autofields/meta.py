
from zope import component
from zope.component import interface
import martian

from zeam.form.autofields import fields


class AutoFieldGrokker(martian.ClassGrokker):
    martian.component(fields.AutoFields)
    martian.directive(fields.form)
    martian.directive(fields.group)

    def execute(self, factory, form, group, config, **kw):
        config.action(
            discriminator=None,
            callable=self.registerSubscriber,
            args=(factory, (form,), group,),)
        config.action(
            discriminator=None,
            callable=interface.provideInterface,
            args=('', form))
        config.action(
            discriminator=None,
            callable=interface.provideInterface,
            args=('', group))
        return True

    def registerSubscriber(self, factory, required, provided):
        sitemanager = component.getGlobalSiteManager()
        sitemanager.registerSubscriptionAdapter(factory, required, provided)
