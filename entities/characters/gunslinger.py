from Engine.Exceptions import exceptions
from entities.characters.character import Character
from entities.entity import Entity


class Gunslinger(Character):
    """
    The main character of the game
    """

    def __init__(self, name):
        super(Gunslinger, self).__init__(name)
        self.__level = 1
        self.__experience = 0
        self.__max_health = 10
        self.__current_health = 10
        self.__accuracy = 0.1
        self.__current_weapon = None
        self.__inventory = []





