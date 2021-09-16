from .dragon import Dragon


class BodyguardDragon(Dragon):
    """BodyguardDragon provides protection to other Dragons."""

    name = 'Bodyguard'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.2
    implemented = True  # Change to True to view in the GUI
    is_container=True
    food_cost=4
    def __init__(self, armor=2):
        Dragon.__init__(self, armor)
        self.contained_dragon = None  # The Dragon hidden in this bodyguard

    def can_contain(self, other):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        if other.is_container==False and self.contained_dragon==None:
            return True
        else:
            return False    
        # END 3.2

    def contain_dragon(self, dragon):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        #print(dragon)
        self.contained_dragon=dragon
        # END 3.2

    def action(self, colony):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        
        #f.reduce_armor(1)
        #print(self.place)
        if self.contained_dragon!=None:
            self.contained_dragon.action(colony)

        # END 3.2
