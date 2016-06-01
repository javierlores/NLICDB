""" 
Tests for the Query module
"""

__author__ = "Javier Lores"


import unittest
from query import *


class TestQuery(unittest.TestCase):
    """ 
    This class tests the abstract query class.
    """
    def test_no_pattern_imp(self):
        """ 
        This function tests to ensure that an error is thrown
        when subclasses of Query fail to implement _pattern()
        """
        class SomeQuery(Query):
            pass

        queryInstance = SomeQuery()
        input_text = ""
        self.assertRaises(NotImplementedError, 
                          queryInstance.interpret, 
                          input_text)

