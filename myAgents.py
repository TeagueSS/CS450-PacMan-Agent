
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent

# each time the game invokes nextAction,
# nextAction will make a call for each ghost to see
# if the pacman is in danger.
class TimidAgent(Agent):


    # Location for Project 1:
    #
    """
    A simple agent for PacMan
    """
    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """


        # Your code
        raise NotImplemented
    
    def getAction(self, state):
        """
        state - GameState

         Each round we need to see if packman is in danger
         based off what happened last turn ->


         1. See how far the agents on the board are from packman (Search)
            TODO: Build search algorithm for finding packman distance


         2. Use this information to help pacman decide if he is in danger
         (We loop from closest to furthest ghost checking each one)
            -> Danger is Defined as matching the following criteria:
                1.The ghost and the pacman are in the same row or column.
                    -> TODO: Figure out how to check board conditons
                2.The ghost is within dist units (formal argument to the method) of the pacman.
                    -> Provided by method
                3.The ghost is not frightened (see the Ghost state for how to check for this).
                    -> Provided by ghost state


         3. ->IF IN DANGER -> (if pacman is (inDanger) we use that bool to indicate we need to flee)
            We check for lega directions in the following order:
            1.reversing the current direction,
            2. turning to the left
            3. then turning to the right
            else:  none of these are legal, we continue in the direction of the danger, or
            stop if no move is legal (only possible in contrived boards).

        4. -> If not in danger ->
            We act like left turn agent (We can just copy that code)


        Fill in appropriate documentation
        """

        # Search ->
        #mazeDistance()




        raise NotImplemented
