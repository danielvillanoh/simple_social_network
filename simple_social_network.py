""" A simple social network for tracking conncections between people """


class Person:
    """A person in the social network 
    
    Attributes:
        names (str): the person's name
        connections (set of Person): other people in the social network 
            who know this person.

    """
    def __init__(self,name):
        """ Initalize a new Person object"""
        self.name = name
        self.conncetion = set()
    
    def conncect(self,person2):
        """Conncect with person2
        
        Args:
            person2 (Person): the other person to connect to.
        
        """
        