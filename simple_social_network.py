""" A simple social network for tracking conncections between people """


class Person:
    """A person in the social network 
    
    Attributes:
        names (str): the person's name
        connections (set of Person): other people in the social network 
            who know this person.
        
    """