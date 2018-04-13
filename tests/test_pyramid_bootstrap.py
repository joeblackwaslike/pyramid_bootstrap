import unittest

from pyramid.config import Configurator
from pyramid.testing import cleanUp
from pyramid import testing

import pyramid_bootstrap


class PyramidBootstrapTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def test_placeholder(self):
        self.assertTrue(True)

    def tearDown(self):
        testing.tearDown()


if __name__ == '__main__':
    unittest.main()
