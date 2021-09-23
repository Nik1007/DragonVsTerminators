class Fighter:
    """A Fighter, the base class of Dragon and Terminator, has armor and a Place."""
    is_dragon = False
    damage = 0
    is_watersafe=False
    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, armor, place=None):
        """Create a Fighter with an ARMOR amount and a starting PLACE."""
        self.armor = armor
        self.place = place  # set by Place.add_fighter and Place.remove_fighter

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the fighter from its place if it
        has no armor remaining.

        >>> test_fighter = Fighter(5)
        >>> test_fighter.reduce_armor(2)
        >>> test_fighter.armor
        3
        """
        #print("Hey")
        self.armor -= amount
        if self.armor <= 0 and (self.is_dragon==False or self.is_container==False):
            self.place.remove_fighter(self)
            #print("Hi")
            self.death_callback()
        elif self.armor <= 0 and self.is_container==True:
            temp=self.contained_dragon
            place=self.place
            self.place.remove_fighter(self)
            self.death_callback()
            place.dragon=temp
           # print(place.dragon)

    def action(self, colony):
        """The action performed each turn.

        colony -- The DragonColony, used to access game state information.
        """

    def death_callback(self):
        # overriden by the gui
        pass

    def __repr__(self):
        cname = type(self).__name__
        return '{0}({1}, {2})'.format(cname, self.armor, self.place)
