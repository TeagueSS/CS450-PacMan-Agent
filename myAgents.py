
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent
from util import manhattanDistance


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
        # Saving our pacman position from the pacman agent himself ->

        pacManPosition = pacman.getPosition()
        ghostPosition = ghost.getPosition()
        # Conditions that determine the pacman is danger
        isGhostScared = ghost.isScared()
        sameRow = (ghostPosition[1] == pacManPosition[1])
        sameColumn = (ghostPosition[0] == pacManPosition[0])
        distance = manhattanDistance(pacManPosition, ghostPosition)

        # Check if Pacman is in danger
        if not isGhostScared and (distance <= dist):
            if sameRow:
                if ghostPosition[0] > pacManPosition[0]:
                    return Directions.EAST
                else:
                    return Directions.WEST

            if sameColumn:
                if ghostPosition[1] > pacManPosition[1]:
                    return Directions.NORTH
                else:
                    return Directions.SOUTH

        return Directions.STOP



    def getAction(self, state):

        # Getting the position of pacMan
        packMan = state.getPacmanState()

        # Finding out how many ghosts we have so we can check the
        # positon of all of our ghosts ->
        ghostPositions = state.getGhostPositions
        # Now that we have the number of agents we need to check each one

        '''  2. Use this information to help pacman decide if he is in danger
         (We loop from closest to furthest ghost checking each one)
            -> Danger is Defined as matching the following criteria:
                1.The ghost and the pacman are in the same row or column.
                    -> TODO: Figure out how to check board conditons (What about walls???)
                2.The ghost is within dist units (formal argument to the method) of the pacman.
                    -> Provided by method
                3.The ghost is not frightened (see the Ghost state for how to check for this).
                    -> Provided by ghost state
        '''
        # Setting our default Direction to the direction we are currently headed
        #TODO ERROR HERE
        #state.getDirection()
        # Getting our ghost states as an array
        ghostStates = state.getGhostStates()  # Retrieves a list of ghost states
        # Checking if pacman is in danger ->
        #for ghostState in ghostStates:
        #    returnDirection = self.inDanger(state, pacmanPosition, ghostState)
        desiredDirection = packMan.getDirection()
        # Carlos' Version: The previous loop kept on checking for Pacman in danger
        # This way it checks for danger once at time and it takes better decision according to the Ghosts' location.

        ''''''

        for ghostState in ghostStates:
            dangerDirection = self.inDanger(packMan, ghostState)
            if dangerDirection != Directions.STOP:

                # Chaning it so that it just reverses heading
                # Desired Direction
                desiredDirection = dangerDirection
                dangerDirection = packMan.getDirection()
                #We need to try it so that he just reverses regardless of
                #where the danger is relative to him

                #HERE IS WHAT WE CHANCE
                desiredLeft = Directions.LEFT
                # We know the direction of the danger we just need to see where that is
                # Relative to pacman
                if(dangerDirection == Directions.NORTH):
                    # Return south
                    desiredDirection = Directions.SOUTH
                    desiredLeft = Directions.EAST
                # If our danger is south
                elif(dangerDirection == Directions.SOUTH):
                    desiredDirection = Directions.NORTH
                    desiredLeft = Directions.WEST
                # If our danger Direction is East
                elif(dangerDirection == Directions.EAST):
                    desiredDirection = Directions.WEST
                    desiredLeft = Directions.NORTH
                # If our danger Direction is west
                elif(dangerDirection == Directions.WEST):
                    desiredDirection = Directions.EAST
                    desiredLeft = Directions.SOUTH

                #TODO possible error could be that we return the direction of the ghost,
                # not the direction of the ghost relative to pacman ->

                # We can say we are in danger and need to navagate for being in danger ->
                '''
                 reversing the current direction, turning to the left, then
                 turning to the right. If none of these are legal, 
                 we continue in the direction of the danger, 
                '''
                # Getting our legal action for pacman to do ->
                legal = state.getLegalPacmanActions()
                # Getting the direction that pacman is currently going ->
                agentState = state.getPacmanState()
                heading = agentState.getDirection()
                # see if the opposite direction of the Ghost is legal
                # See if turning around is legal
                if(desiredDirection in legal):
                    # if turning around from the danger is legal then turn around
                    return desiredDirection
                # If we can't go back lets go left
                elif(desiredLeft in legal):
                    # If we can turn left, lets turn left!
                    return Directions.LEFT[heading]
                #see if we can turn right
                elif(Directions.RIGHT[heading] in legal):
                    return Directions.RIGHT[heading]
                #Otherwise we can't do anything but continue down our current course!
                else:
                    # Returning our current heading
                    return heading

        '''
         3. -> IF IN DANGER -> (if pacman is (inDanger) we use that bool to indicate we need to flee)
            We check for lega directions in the following order:
            1.reversing the current direction,
            2. turning to the left
            3. then turning to the right
            else:  none of these are legal, we continue in the direction of the danger, or
            stop if no move is legal (only possible in contrived boards).
        '''

        '''
        4. -> If not in danger ->
            We act like left turn agent (We can just copy that code)
        '''
        #TODO we still need the switch statement to see where the danger
        # is relative to us

        # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        # Get the agent's state from the game state and find agent heading
        agentState = state.getPacmanState()
        heading = agentState.getDirection()

        if heading == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH

        # Turn left if possible
        left = Directions.LEFT[heading]  # What is left based on current heading
        if left in legal:
            action = left
        else:
            # No left turn
            if heading in legal:
                action = heading  # continue in current direction
            elif Directions.RIGHT[heading] in legal:
                action = Directions.RIGHT[heading]  # Turn right
            elif Directions.REVERSE[heading] in legal:
                action = Directions.REVERSE[heading]  # Turn around
            else:
                action = Directions.STOP  # Can't move!

        return action

        # Checking for github