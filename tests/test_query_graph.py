""" 
Tests for the QueryGraph module
"""

__author__ = "Javier Lores"

import sys
sys.path.append("../src")
import unittest
from query_graph import *


class TestQueryGraph(unittest.TestCase):
    """ 
    This class contains tests the QueryGraph class
    """
    def test_node_creation_in_empty_graph(self):
       """ 
       This functions tests the creation of nodes in the graph.
       In particular it tests when a node is added to an empty graph
       """
       # Create the graph
       graph = QueryGraph()

       # Test if the first node in a graph is created correctly
       # Create the graph
       graph = QueryGraph()

       # Test if the first node in a graph is created correctly
       data = "data"
       node = graph.insert_node(data)

       # Ensure the data is in the node
       self.assertEqual(node.data, data)

       # Ensure the node neighbor list is empty
       self.assertEqual(graph.nodes[node], [])


    def test_node_creation_in_connected_graph(self):
       """ 
       This functions tests the creation of nodes in the graph.
       In particular it tests when a node is added with an edge
       to another node.
       """
       # Create the graph
       graph = QueryGraph()
       
       # Create the first node
       data1 = "data1"
       node1 = graph.insert_node(data1)

       # Create the second node, with an edge to the first
       data2 = "data2"
       node2 = graph.insert_node(data2, nod2)

       # Ensure the nodes are in each others neighbor lists
       self.assertTrue(node1 in graph.nodes[node2])
       self.assertTrue(node2 in graph.nodes[node1])


    def test_node_creation_in_connected_graph(self):
       """ 
       This functions tests the creation of nodes in the graph.
       In particular it tests when a node is added without an edge
       to another node.
       """
       # Create the graph
       graph = QueryGraph()

       # Create the first node
       data1 = "data1"
       node1 = graph.insert_node(data1)

       # Create the second node, with no edge to the first
       data2 = "data2"
       node2 = graph.insert_node(data2)

       # Ensure the nodes are NOT in each others neighbor lists
       self.assertFalse(node1 in graph.nodes[node2])
       self.assertFalse(node2 in graph.nodes[node1])


    def test_graph_collapsation(self):
       """ 
       This functions tests if a graph is collapsed correctly. It tests
       a simple non-nested graph.
       """
       # Create the graph
       graph = QueryGraph()

       # Create some nodes
       data1 = "data1"
       data2 = "data2"
       data3 = "data3"
       data4 = "data4"
       node1 = graph.insert_node(data1)
       node2 = graph.insert_node(data2, node1)
       node3 = graph.insert_node(data3, node1)
       node4 = graph.insert_node(data4, node1)

       # Collapse the graph
       collapsed = graph.collapse()

       # Ensure we got the expected graph
       expected_collapsed = [node1.data, [node2.data, node3.data, node4.data]]
       self.assertEquals(collapsed, expected_collapsed)


