from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    implemented = True  # Change to True to view in the GUI
    food_cost=5
    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount=1):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
        # BEGIN 2.2
        "* YOUR CODE HERE *"
        
        
        armor=self.armor
        if(len(self.place.terminators)>0):
            x=len(self.place.terminators)*amount
            if self.armor-x >0:
                self.armor-=x
                terminators = self.place.terminators.copy()
                for terminator in terminators:
                    terminator.reduce_armor(x)
               
            else:
                self.armor=0
                terminators = self.place.terminators.copy()
                for terminator in terminators:
                    terminator.reduce_armor(armor+self.damage)
                self.place.remove_fighter(self)
                self.death_callback()