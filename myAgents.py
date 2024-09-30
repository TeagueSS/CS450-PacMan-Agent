
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

        #Getting packman's position from his agent state ->
        pacManPosition = pacman.getPosition()
        #Getting Ghost's position from his agent State
        ghostPosition = ghost.getPosition()
        # Conditions that determine the pacman is danger
        # 1 if the ghost is scared
        isGhostScared = ghost.isScared()
        # 2 if they share a row or collumn
        sameRow = (ghostPosition[1] == pacManPosition[1])
        sameColumn = (ghostPosition[0] == pacManPosition[0])
        # 3 if their distance is smaller than 3
        distance = manhattanDistance(pacManPosition, ghostPosition)

        # Now we see if he is in danger ->
        if not isGhostScared and (distance <= dist):
            #If we pass the inital conditon we check for
            # if they're in the same row
            if sameRow:
                #If they are check the direction to return
                if ghostPosition[0] > pacManPosition[0]:
                    return Directions.EAST
                else:
                    return Directions.WEST

            if sameColumn:
                # If they're in the same column
                # WE need to see who's higher up ->
                if ghostPosition[1] > pacManPosition[1]:
                    return Directions.NORTH
                else:
                    return Directions.SOUTH
        #Otherwise we can assume he isn't in danger and return STOP
        return Directions.STOP



    def getAction(self, state):

        # Getting the position of pacMan
        packMan = state.getPacmanState()

        # Finding out how many ghosts we have so we can check the
        # positon of all of our ghosts ->
        ghostPositions = state.getGhostPositions
        # Now that we have the number of agents we need to check each one

        # Getting our ghost states as an array
        ghostStates = state.getGhostStates()  # Retrieves a list of ghost states

        # Saving pacman's current direction as his default ->
        desiredDirection = packMan.getDirection()

        # Carlos' Version: The previous loop kept on checking for Pacman in danger
        # This way it checks for danger once at time
        # #and it takes better decision according to the Ghosts' location.


        # Looping for all of the ghosts on the baord ->
        for ghostState in ghostStates:
            dangerDirection = self.inDanger(packMan, ghostState)
            # Seeing if we found danger
            if dangerDirection != Directions.STOP:
                # If we are in danger attempt to get away ->

                # Setting our default Direction to our current Direction ->
                dangerDirection = packMan.getDirection()
                # Marking what our left of our desired direction would be
                desiredLeft = Directions.LEFT
                # We know the direction of the danger we just need to see where that is
                # Relative to pacman
                if(dangerDirection == Directions.NORTH):
                    # Return south
                    desiredDirection = Directions.SOUTH
                    # Left of south is east
                    desiredLeft = Directions.EAST
                # If our danger is south
                elif(dangerDirection == Directions.SOUTH):
                    desiredDirection = Directions.NORTH
                    # Left of north is west
                    desiredLeft = Directions.WEST
                # If our danger Direction is East
                elif(dangerDirection == Directions.EAST):
                    desiredDirection = Directions.WEST
                    desiredLeft = Directions.NORTH
                # If our danger Direction is west
                elif(dangerDirection == Directions.WEST):
                    desiredDirection = Directions.EAST
                    desiredLeft = Directions.SOUTH

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
        4. -> If not in danger ->
            We act like left turn agent (We can just copy that code)
        '''

        #Normal Left turn Behavior ->
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
        # Returning our end action
        return action
