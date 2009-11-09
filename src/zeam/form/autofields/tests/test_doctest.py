
import unittest

from zope.testing import doctest
from grokcore.component.testing import grok_component

from zeam.form.autofields.testing import FunctionalLayer, setUp, tearDown

def test_suite():
    optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    globs= {'grok_component': grok_component}

    suite = unittest.TestSuite()
    for filename in ['fields.txt',]:
        test = doctest.DocFileSuite(
            filename,
            optionflags=optionflags,
            setUp=setUp,
            tearDown=tearDown,
            globs=globs)
        test.layer = FunctionalLayer
        suite.addTest(test)

    return suite
