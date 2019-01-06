class Entity:
    """
    Represents an object that can appear in the game
    """

    def description(self):
        """
        Get a description of this entity
        :return: A description of this entity
        """
        return self.__name__
