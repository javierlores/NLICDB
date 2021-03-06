""" 
Tests for the Query module
"""

__author__ = "Javier Lores"

import sys
sys.path.append("../src")
from query import *
sys.path.append("../../concourse/concourse-driver-python")
from concourse import Operator
import unittest



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
        input_text = "Some input text"
        self.assertRaises(NotImplementedError, 
                          queryInstance.interpret, 
                          input_text)

    def test_interpret_unmatched_regex(self):
        """ 
        This function tests the the return value of interpret is 
        false when there is an unmatched regex.
        """
        class SomeQuery(Query):
            def _pattern(self):
                return r'someregexpattern'


        queryInstance = SomeQuery()
        input_text = "Some input text"
        result = queryInstance.interpret(input_text)

        self.assertFalse(result)


class TestFindQuery(unittest.TestCase):
    """ 
    This class tests the FindQuery class.
    """
    def test_interpret_matched_regex(self):
        """ 
        This function tests the FindQuery interpret method
        to ensure proper matching of regex.
        """
        queryInstance = FindQuery()
        input_text = "find employees whose age greater 25"
        expected_result = ['find', 'age', Operator.GREATER_THAN, 25]
        result = queryInstance.interpret(input_text)

        self.assertEqual(result, expected_result)


    def test_interpret_unmatched_regex(self):
        """ 
        This function tests the FindQuery interpret method
        to ensure that any instance where the first word is not
        find fails.
        """
        queryInstance = FindQuery()
        input_text = "search employees age greater 25"
        result = queryInstance.interpret(input_text)

        self.assertFalse(result)


class TestGetQuery(unittest.TestCase):
    """ 
    This class tests the GetQuery class.
    """
    def test_interpret_matched_regex(self):
        """ 
        This function tests the GetQuery interpret method
        to ensure proper matching of regex.
        """
        queryInstance = GetQuery()
        input_text = "get country user whose id 2"
        expected_result = ['get', 'country', 2]
        result = queryInstance.interpret(input_text)

        self.assertEqual(result, expected_result)


    def test_interpret_unmatched_regex(self):
        """ 
        This function tests the GetQuery interpret method
        to ensure that any instance where the first word is not
        find fails.
        """
        queryInstance = GetQuery()
        input_text = "country user whose id 2"
        result = queryInstance.interpret(input_text)

        self.assertFalse(result)


class TestSetQuery(unittest.TestCase):
    """ 
    This class tests the SetQuery class.
    """
    def test_interpret_matched_regex(self):
        """ 
        This function tests the SetQuery interpret method
        to ensure proper matching of regex.
        """
        queryInstance = SetQuery()
        input_text = "set name dwight user whose id 3"
        expected_result = ['set', 'name', 'dwight', 3]
        result = queryInstance.interpret(input_text)

        self.assertEqual(result, expected_result)


    def test_interpret_unmatched_regex(self):
        """ 
        This function tests the SetQuery interpret method
        to ensure that any instance where the first word is not
        find fails.
        """
        queryInstance = SetQuery()
        input_text = "name dwight user whose id 3"
        result = queryInstance.interpret(input_text)

        self.assertFalse(result)


class TestRemoveQuery(unittest.TestCase):
    """ 
    This class tests the RemoveQuery class.
    """
    def test_interpret_matched_regex(self):
        """ 
        This function tests the RemoveQuery interpret method
        to ensure proper matching of regex.
        """
        queryInstance = RemoveQuery()
        input_text = "remove age 18 user whose id 1"
        expected_result = ['remove', 'age', 18, 1]
        result = queryInstance.interpret(input_text)

        self.assertEqual(result, expected_result)


    def test_interpret_unmatched_regex(self):
        """ 
        This function tests the RemoveQuery interpret method
        to ensure that any instance where the first word is not
        find fails.
        """
        queryInstance = RemoveQuery()
        input_text = "age 18 user whose id 1"
        result = queryInstance.interpret(input_text)

        self.assertFalse(result)

