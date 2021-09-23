from characters.dragons.scuba_thrower import ScubaThrower
import utils
class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    food_cost=7
    instanced=False
    king=0
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        "* YOUR CODE HERE *"
        ScubaThrower.__init__(self,armor)
        if DragonKing.king==0:
            #print(self.armor)
            #print("king")
            DragonKing.king=1
            self.instanced=True 
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "* YOUR CODE HERE *"
        if self.instanced==False:
            #print(self.armor)
            self.reduce_armor(self.armor)
        else:
            ScubaThrower.action(self,colony)  
            temp=self.place.exit
            dragons=[] 
            while temp:
                if temp.dragon:
                    if temp.dragon.is_container:
                        dragons.append(temp.dragon.contained_dragon)
                    dragons.append(temp.dragon)    
                temp=temp.exit
            temp_dragons=dragons.copy()  
            i=0;  
            for _ in temp_dragons:
                if dragons[i]!=None and dragons[i].is_buffed==False:
                    dragons[i].damage=2*dragons[i].damage
                    dragons[i].is_buffed=True
                i=i+1    


            #self.throw_at(self.nearest_terminator(colony.skynet))
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "* YOUR CODE HERE *"
        ScubaThrower.reduce_armor(self,self.armor)
        if self.instanced==True and self.armor==0:
            utils.terminators_win()