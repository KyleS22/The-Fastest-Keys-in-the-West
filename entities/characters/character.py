from Engine.Exceptions import exceptions
from Engine.Exceptions.exceptions import PlayerDeadException, CharacterDeadException, ItemNotFoundException
from entities.entity import Entity
from entities.weapons.weapon import Weapon


class Character(Entity):
    """
    A Character in the game
    """

    def __init__(self):
        self.__name = None
        self.__level = None
        self.__current_health = None
        self.__max_health = None
        self.__accuracy = None
        self.__current_weapon = None
        self.__inventory = []
        self.__is_dead = False

    def description(self):
        """
        return a description string for this character
        :return:
        """
        pass

    def equip_weapon(self, weapon_name):
        """
        Equip the given weapon if it is in the inventory, and place the
        currently equipped weapon into the inventory
        :param weapon: A weapon to equip
        :return: None
        """

        if self.__is_dead:
            raise CharacterDeadException("You cannot equip a dead character.")

        for item, quantity in self.__inventory:
            if isinstance(item, Weapon) and item.get_name() == weapon_name:
                self.add_to_inventory(self.__current_weapon)
                self.__current_weapon = item
                self.remove_from_inventory(weapon_name, 1)

        raise ItemNotFoundException("The requested weapon is not in the inventory")

    def add_to_inventory(self, item_to_add, quantity_to_add):
        """
        Add the given item to the inventory, or increases the count for that item if it already exists
        :param item_to_add: The item to add
        :param quantity_to_add: The amount to add
        :return: None
        """
        # If there is already an instance of the item in the class, update it
        if any(isinstance(item, item_to_add.__class__) for item,  _  in self.__inventory):
            self.__inventory[:] = [(item, quantity) if not isinstance(item, item_to_add.__class__)
                                   else (item, quantity + quantity_to_add)
                                   for (item, quantity) in self.__inventory]

        else:
            self.__inventory.append((item_to_add, quantity_to_add))


    def remove_from_inventory(self, item_name, amount):
        """
        Remove the amount of the item matching item_name from the inventory
        :param item_name: The name of the item to remove
        :return: None
        """
        pass

    def show_inventory(self):
        """
        Returns a string representation of the characters inventory
        :return: A string representation of the characters inventory
        """

    def attack(self, other):
        """
        Attack the given character with the currently equipped weapon
        :param other: The other character to attack
        :return: A description of what happened, based on the weapon, skill, and description of the other
        """
        pass

    def take_damage(self, amount):
        """
        Take an amount of damage
        :param amount: The amount of damage to take
        :return: None
        """
        pass

    def heal(self, amount):
        """
        Heal an amount of health up to the character's max health
        :param amount: The amount to heal by
        :return: None
        """
        pass

    def taunt(self, other, taunt=None):
        """
        Taunt the given character with the given taunt.  The taunt is returned so that it can
        be displayed in the narritive.  If taunt is None, a random taunt will be chosen from a pre-determined
        list of spicy taunts
        :param other: The character to taunt
        :param taunt: The taunt to use (None if you wish to have one generated)
        :return: A string representing the taunt, and its affect on the character
        """
        pass

    def become_taunted(self, taunt=None):
        """
        The character has a random chance of becoming taunted.  This temporarily decreases accuracy.
        :return: True if taunted, false otherwise
        """
        pass

    def become_untaunted(self):
        """
        Undo the taunting
        :return: None
        """
        pass