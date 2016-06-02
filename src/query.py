__author__ = "Javier Lores"


import re
import sys
sys.path.append("../../concourse/concourse-driver-python/")
from concourse import Operator


OPERATOR_MAPPING = [(Operator.EQUALS, 'equal'),
                    (Operator.NOT_EQUALS, 'not equal'),
                    (Operator.GREATER_THAN, 'greater'),
                    (Operator.GREATER_THAN_OR_EQUALS, 'greater equal'),
                    (Operator.LESS_THAN, 'less'),
                    (Operator.LESS_THAN_OR_EQUALS, 'less equal'),
                    (Operator.BETWEEN, 'between'),
                    (Operator.REGEX, 'regex'),
                    (Operator.NOT_REGEX, 'not regex')]


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
        def is_int(text):
            """ 
            A helper function to check if a str is an int
            """
            try:
                int(text)
                return True
            except:
                return False

        # Match regex groups in the query
        match = re.match(self._pattern(), query)

        # Ensure a match was found
        if match:
            groups = match.groups()
            # Convert groups to appropriate types
            groups = [int(item) if is_int(item) else item for item in groups]

            # Convert operators to approriate types
            new_groups = []
            for item in groups:
                found = False
                for operator, mapping in OPERATOR_MAPPING:
                    if item == mapping:
                        new_groups.append(operator)
                        found = True
                if not found:
                    new_groups.append(item)
            return new_groups
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
        return r'(find)(?:\s\w+){0,2}\s(\w+)\s(\w+)\s(\w+)'


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
        return r'(get)\s(\w+)(?:[^\W]*\s)*(\d+)'


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


class RemoveQuery(Query):
    """ 
        An example query of this type would be:
        "Remove the age of 18 of the user whose id is 1"

        The corresponding Concourse API call would be:
        remove("age", 18, 1)
    """

    def _pattern(self):
        """ 
        Returns the regex pattern to be matched for this query type.
        """
        return r'(remove)\s(\w+)\s(\w+)\s(?:[^\W]*\s)*(\d+)'
