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


class FindQuery(Query):
    """ 
        An example query of this type would be:
        "Find users whose age is greater than 25"

        The corresponding Concourse API call would be:
        find("age", Operator.GREATER_THAN, 25)
    """

    def _pattern(self):
        """ 
        Returns the regex pattern to be matched for this query type.
        """
        return r'(find)(?:\s[a-zA-Z]+){0,2}\s(\w+)\s(\w+)\s(\w+)'


class GetQuery(Query):
    """ 
        An example query of this type would be:
        "Get the age for the user whose id is 1"

        The corresponding Concourse API call would be:
        get("age", 1)
    """

    def _pattern(self):
        """ 
        Returns the regex pattern to be matched for this query type.
        """
        return r'(get)\s([a-zA-Z]+)(?:[^\W]*\s)*(\d+)'


class SetQuery(Query):
    """ 
        An example query of this type would be:
        "Set the age to 18 for the user whose id is 1"

        The corresponding Concourse API call would be:
        set("age", 18, 1)
    """

    def _pattern(self):
        """ 
        Returns the regex pattern to be matched for this query type.
        """
        return r'(set)\s(\w+)\s(\w+)\s(?:[^\W]*\s)*(\d+)'

