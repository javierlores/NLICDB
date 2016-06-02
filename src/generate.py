__author__ = "Javier Lores"


from preprocess import *
from query_graph import *
from query import *

QUERY_TYPES = [FindQuery,
               SetQuery,
               GetQuery,
               RemoveQuery]

class Generator(object):
    """ 
    This class is used to generate a natural language query into a function 
    call into the Concourse API.
    """
    @staticmethod
    def generate(query):
        """ 
        This function accepts a natural language query and generates a
        function call into the Concourse API. The return query is in the
        format [func, [arg1, arg2, func[arg1, arg2...]]]

        :param query: the natural language query

        :return the generated query 
        """

        def _create_graph(values):
            """ 
            This function builds a graph from a list of values
            It does so by first creating an unconnected graph from the values,
            then merging on similar nodes to create the final query.
            """
            # Create the graph
            graph = QueryGraph()

            # Create a separate graph for every detected query
            for match in values:
                relation, terms = match[0], match[1:]
                node = graph.insert_node(relation)
                for term in terms:
                    graph.insert_node(term, node)

            # TODO: Merge queries
            return graph


        # Preprocess the query
        query = Preprocessor.preprocess(query)

        # Find any query type matches for the query
        matches = []
        for query_type in QUERY_TYPES:
            # Check if the query is matched by the query type
            query_type_instance = query_type()
            match = query_type_instance.interpret(query)

            # If the query is a match add it
            if match:
                matches.append(match)

        # Ensure we found a match for the query
        if not matches:
            return False

        # Create the abstract query graph to represent our database query
        graph = _create_graph(matches)

        # Create our Concourse query
        generated_query = graph.collapse()

        # SPECIAL CASE:
        # The find function call for Concourse accepts kwargs so
        # We need to set that up here
        if generated_query[0] == 'find':
            kwargs = {}
            kwargs['key'] = generated_query[1][0]
            kwargs['operator'] = generated_query[1][1]
            kwargs['value'] = generated_query[1][2]
            generated_query[1] = kwargs

        return generated_query


        


