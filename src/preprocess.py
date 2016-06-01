__author__ = "Javier Lores"


import nltk


class Preprocessor(object):
    """ 
    A utility class to perform preprocessing on a string of text.
    """
    @staticmethod
    def preprocess(text):
        """ 
        This function performs preprocessing on a string. The following 
        preprocessing steps are performed:
            word tokenization
            lower casing
            stop word removal

        :param text: The text to preprocess

        :return The preprocessed text
        """
        # Word tokenization
        word_tokenizer = nltk.tokenize.WordPunctTokenizer()
        data = word_tokenizer.tokenize(text)

        # Convert text to lower case
        data = [word.lower() for word in data]

        # Stop word removal
        stopwords = set(nltk.corpus.stopwords.words('english'))
        data = [word for word in data if word not in stopwords]

        # Create a string from the data
        data = " ".join(data)

        return data
        
