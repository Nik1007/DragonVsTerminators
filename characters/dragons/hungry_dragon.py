from .dragon import Dragon
import random

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    time_to_digest=3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.3
    implemented = True  # Change to True to view in the GUI
    food_cost =4

    # END 2.3

    def __init__(self, armor=1,digesting=0):
        # BEGIN 2.3
        "* YOUR CODE HERE *"
        Dragon.__init__(self,armor)
        self.digesting=digesting
        # END 2.3

    def eat_terminator(self, terminator):
        # BEGIN 2.3
        "* YOUR CODE HERE *"
        #print(terminator.armor)
        terminator.reduce_armor(terminator.armor)
        # END 2.3

    def action(self, colony):
        # BEGIN 2.3
        "* YOUR CODE HERE *"
        if self.digesting==0:
            if len(self.place.terminators)>0:
                terminator=random.choice(self.place.terminators)
                self.eat_terminator(terminator)
                self.digesting=self.time_to_digest
        elif self.digesting>0: 
            self.digesting-=1
        #print(self.armor)

