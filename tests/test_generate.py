""" 
Tests for the Generate module
"""

__author__ = "Javier Lores"

import sys
sys.path.append("../src")
import unittest
from generate import *


class TestGenerator(unittest.TestCase):
    """ 
    This class performs tests on the Generator class
    """
    def test_generate(self):
       """ 
       This function tests the generate function of the generator class.
       """
       test_input = "Get the age for the user whose id is 1"
       expected_output = ['get', ['age', 1]]
       output = Generator.generate(test_input)
       self.assertEqual(expected_output, output)

