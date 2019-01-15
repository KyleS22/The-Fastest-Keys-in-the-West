class PlayerDeadException(Exception):
    """
    Exception for when the player is dead
    """
    def __init__(self, message):
        self.message = message


class CharacterDeadException(Exception):
    """
    Exception for when a given character is dead
    """
    def __init__(self, message):
        self.message = message


class WeaponEmptyException(Exception):
    """
    Exception for when a weapon is empty
    """

    def __init__(self, message):
        self.message = message


class ItemNotFoundException(Exception):
    """
    Exception for when an item is not found in the inventory
    """

    def __init__(self, message):
        self.message = message