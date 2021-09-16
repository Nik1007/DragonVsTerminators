from . import Place


class Water(Place):
    """Water is a place that can only hold watersafe fighters."""
    def __init__(self,name):
        Place.__init__(self,name)


    def add_fighter(self, fighter):
        """Add a Fighter to this place. If the fighter is not watersafe, reduce
        its armor to 0."""
        # BEGIN 4.1
        "*** YOUR CODE HERE ***"
        Place.add_fighter(self,fighter)
        fighter.place=self   
        #print(fighter.place)    
        if not fighter.is_watersafe:
            #print(fighter)
            fighter.reduce_armor(fighter.armor)
        