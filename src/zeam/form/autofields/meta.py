
from zope.interface import Interface
import grokcore.component
import grokcore.view
import martian

from zeam.form.autofields import fields


class AutoFieldGrokker(martian.ClassGrokker):
    martian.component(fields.AutoFields)
    martian.directive(grokcore.view.view)
    martian.directive(grokcore.component.context, get_default=lambda *x, **y: Interface)
    martian.directive(fields.group)

    def execute(self, factory, context, view, group, config, **kw):
        config.action(
            discriminator=None,
            callable=grokcore.component.util.provideSubscriptionAdapter,
            args=(factory, (context, view,), group,),)
        config.action(
            discriminator=None,
            callable=grokcore.component.util.provideInterface,
            args=('', view))
        config.action(
            discriminator=None,
            callable=grokcore.component.util.provideInterface,
            args=('', group))
        return True
