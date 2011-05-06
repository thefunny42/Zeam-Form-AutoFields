
from zope import component
from zope.component import interface
import grokcore.view
import martian

from zeam.form.autofields import fields


class AutoFieldGrokker(martian.ClassGrokker):
    martian.component(fields.AutoFields)
    martian.directive(grokcore.view.view)
    martian.directive(fields.group)

    def execute(self, factory, view, group, config, **kw):
        config.action(
            discriminator=None,
            callable=self.registerSubscriber,
            args=(factory, (view,), group,),)
        config.action(
            discriminator=None,
            callable=interface.provideInterface,
            args=('', view))
        config.action(
            discriminator=None,
            callable=interface.provideInterface,
            args=('', group))
        return True

    def registerSubscriber(self, factory, required, provided):
        sitemanager = component.getGlobalSiteManager()
        sitemanager.registerSubscriptionAdapter(factory, required, provided)
