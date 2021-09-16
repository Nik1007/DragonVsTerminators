from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True # Change to True to view in the GUI
    food_cost=6
    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
        BodyguardDragon.action(self,colony)
        temp=self.place.terminators.copy()
        for i in temp:
            i.reduce_armor(self.damage)
