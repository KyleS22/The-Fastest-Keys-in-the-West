from Engine.Exceptions import exceptions
from entities.entity import Entity


class Character(Entity):
    """
    A Character in the game
    """

    def __init__(self, name):
        self.__name = name
        self.__level = None
        self.__current_health = None
        self.__max_health = None
        self.__accuracy = None
        self.__current_weapon = None
        self.__inventory = []

    # TODO: Functionality common among any character in the game
