__author__ = "Javier Lores"


import re


class Query(object):
    """ 
    This class is a template class that should be subclassed for
    every query type to be supported.
    """

    def _pattern(self):
        """ 
        This function should be implemented by the subclass. It
        should return a regex expression to match the query.
        """
        raise NotImplementedError()


    def interpret(self, query):
        """ 
        This function attempts to extract data from a natural language 
        query (already preprocessed) using the appropriate regex pattern. It will
        return False, if the extraction was unsucessful, otherwuse it will return
        the extracted data.

        :param query: The preprocessed query

        :return: False, if unsuccessful, otherwise return the extracted data
        """
        # Match regex groups in the query
        match = re.match(self._pattern(), query)

        # Ensure a match was found
        if match:
            return match.groups()
        else:
            return False
