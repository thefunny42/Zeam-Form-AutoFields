
import zeam.form.autofields

from zope.app.wsgi.testlayer import BrowserLayer
from zope.configuration.config import ConfigurationMachine
from grokcore.component import zcml

FunctionalLayer = BrowserLayer(zeam.form.autofields)

def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok(module_name, config)
    config.execute_actions()
