""" 
Tests for the Preprocessing module
"""

__author__ = "Javier Lores"


import sys
sys.path.append("../src")
import unittest
from preprocess import Preprocessor


class TestPreprocessor(unittest.TestCase):
    """ 
    This class tests the Preprocessor class.
    """
    def test_preprocess(self):
        """ 
        Perform a few tests on the preprocess function.
        """
        # Test a Set function text string
        input_text = "Set the age to 18 of the user whose id is 1"
        expected_text = "set age 18 user whose id 1"

        preprocessed_text = Preprocessor.preprocess(input_text)
        self.assertEqual(preprocessed_text, expected_text)

        # Test a Get function text string
        input_text = "Get the salary of the user whose id is 2"
        expected_text = "get salary user whose id 2"

        preprocessed_text = Preprocessor.preprocess(input_text)
        self.assertEqual(preprocessed_text, expected_text)

        # Test a Get function text string
        input_text = "Remove the name John from the user whose id is 3"
        expected_text = "remove name john user whose id 3"

        preprocessed_text = Preprocessor.preprocess(input_text)
        self.assertEqual(preprocessed_text, expected_text)

        # Test a Get function text string
        input_text = "Find employees whose country is equal to USA"
        expected_text = "find employees whose country equal usa"

        preprocessed_text = Preprocessor.preprocess(input_text)
        self.assertEqual(preprocessed_text, expected_text)
