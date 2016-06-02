__author__ = "Javier Lores"


class QueryGraph(object):
    """ 
    A database query can be thought as a graph where each node is a variable 
    and each edge is a relation. As such, this class implements such a graph
    to represent a database query in abstract form.

    An example graph would be as follows:


              ------  relation    -------
              |node| ------------ |term4|
              ------              -------
                 |
                 |
              relation
                 | 
               ------  relation   -------
               |node| ----------- |term3|
               ------             -------
              /      \
      relation        \
            /          relation
           /            \
          /              \
       -------          -------
       |term1|          |term2|
       -------          -------


    For more concrete example, assume a database with records organized as:
    record: id, name, dept, gender, country, salary, age, spouse

    Then let us assume a natural language query is posed such as:
    "What country is dwight from?"

    The corresponding Concourse API call would be 
    get("country", find("name", Operator.EQUALS, "dwight"))

               -----              ---------
               |get| ------------ |country|
               -----              ---------
                 |
                 |
                 |
                 | 
               ------             --------
               |find| ----------- |dwight|
               ------             --------
              /      \
             /        \
            /          \
           /            \
          /              \
       ------          -----------------
       |name|          |Operator.EQUALS|
       ------          -----------------

    Because the questions and therefore graph are small, the implementation 
    is likely irrelavent. Nonetheless, this class implements the graph using 
    adjacency list. The reason for this is simply there is no need for fast 
    lookup as can be done with an adjacency matrix.
    """

    def __init__(self):
        """ 
        Creates a new empty graph.
        """
        self.nodes = {}
        self.head = None


    def insert_node(self, data, node=None):
        """ 
        Adds a node to the graph with an edge connected to 'node'.
        The new node is assigned 'data' and is returned.

        :param node: The node to connect to the new node
        :param data: The data to store in the new node
        
        :return The newly created node
        """
        # Create the new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        # If this node is connected to another node
        if node:
            self.nodes[new_node] = [node]
            self.nodes[node].append(new_node)
        # If there is no neighbor to this node
        else:
            self.nodes[new_node] = []

        return new_node


    def collapse(self):
        """ 
        This function collapses a graph such that each child node is 
        collapsed into its parent. The graph is traversed in a pre-order
        DFS to do so.
        """
        def dfs(node, visited=None, collapsed=None):
            # On first call, create visited and collapsed sets
            if visited is None:
                visited = set()
                collapsed = []

            # Visit node
            visited.add(node)

            # Add the node and a list for its children (if there are children)
            collapsed.append(node.data)
            if set(self.nodes[node])-visited:
                collapsed.append([])

            # Visit neighboring nodes recursively
            for next in self.nodes[node]:
                if next not in visited:
                    dfs(next, visited, collapsed[1])
            return visited, collapsed

        # Execute the DFS search
        visited, collapsed = dfs(self.head)
        
        return collapsed


class Node(object):
    """ 
    This class represents a graph node that contains data.
    """
    def __init__(self, data):
        self.data = data
        
