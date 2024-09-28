
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
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column, -> Does this even require walls?
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """
        inDanger = False
        # We're going to make this false for now ->
        # Marking our ghost position
        ghostPosition = ghost.getPosition()
        #TODO 2. Conditon 2 -> is the distance less than or equal to our provided
        # distance

        # Getting our distance from the Manhattan function
        distance = manhattanDistance(pacManPosition, ghostPosition)
        # Checking if it is greater than our distance
        if distance <= dist:
            inDanger = True

        #TODO 3. Check if we are in the same row or column as our ghost
        # We have to check both row and column so checking row first

        # Saving our walls / gameBoard
        #walls = state.getWalls()
        # Checking if they share a y height
        if(pacManPosition[1] == ghostPosition[1] ):
            # If they share a column then we are in danger ->
            inDanger = True
        # Checking if they share a row ->
        elif(pacManPosition[0] == ghostPosition[0]):
            inDanger = True

        ''' STEP 4: if we are in danger (Which we should already know), we need to return 
        from what direction the danger is coming from -> '''


        # Checking if the ghosts are scared,
        # We can't be in danger if the ghosts are scared ->

        # We can assume we are in danger if the ghost isn't scared and vice versa
        if(inDanger & ghost.isScared()):
            # Seeing if our ghost is scared
            inDanger = False
            return Directions.STOP


        if (inDanger):
            # Check if Pacman and the ghost are in the same row
            if pacManPosition[1] == ghostPosition[1]:
                # If Pacman is to the left of the ghost, return EAST
                if pacManPosition[0] < ghostPosition[0]:
                    return Directions.EAST
                # Otherwise, Pacman is to the right of the ghost, return WEST
                else:
                    return Directions.WEST
            # If not in the same row, check if they are in the same column
            elif pacManPosition[0] == ghostPosition[0]:
                # If Pacman is below the ghost, return NORTH
                if pacManPosition[1] < ghostPosition[1]:
                    return Directions.NORTH
                # Otherwise, Pacman is above the ghost, return SOUTH
                else:
                    return Directions.SOUTH
            # Check which direction is greater ->
            if(abs(pacManPosition[0] - ghostPosition[0]) >= abs(pacManPosition[1] - ghostPosition[1])):
                # Now we know that our x distance is greater
                # So lets return the closest y - Direction
                if(pacManPosition[1] > ghostPosition[1]):
                    # If pacman is above then our ghost is below!
                    return Directions.SOUTH
                else:
                    #Otherwise we can say the ghost is above pacman
                    return Directions.NORTH
            else:
                #now we know that our y distance is greater
                #So we return whatever x distance is greater
                if(pacManPosition[1] > ghostPosition[1]):
                    # If pacman is to the right then the ghost is to the left (West)
                    return Directions.WEST
                else:
                    # If pacman is to the left, then the ghost is to the right (East)
                    return Directions.EAST
            #If he isn't in danger then we can return stop ->
        return Directions.STOP



    def getAction(self, state):

        # Getting the position of pacMan
        packMan = state.getPacmanState()


        # Pass packman
        #pacmanPositionTwo = packMan.getPacmanPosition()
        #pacmanPosition = state.getPacmanPosition()



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
        # updating our default direction ->
        #agentState = state.getPacmanState()
        #returnDirection = agentState.getDirection()

        # Getting our ghost states as an array
        ghostStates = state.getGhostStates()  # Retrieves a list of ghost states
        # Checking if pacman is in danger ->
        #for ghostState in ghostStates:
        #    returnDirection = self.inDanger(state, pacmanPosition, ghostState)

        # Carlos' Version: The previous loop kept on checking for Pacman in danger
        # This way it checks for danger once at time and it takes better decision according to the Ghosts' location.
        for ghostState in ghostStates:
            dangerDirection = self.inDanger(packMan, ghostState)
            if dangerDirection != Directions.STOP:

                # Desired Direction
                desiredDirection = dangerDirection
                # We know the direction of the danger we just need to see where that is
                # Relative to pacman
                if(dangerDirection == Directions.NORTH):
                    # Return south
                    desiredDirection = Directions.SOUTH
                # If our danger is south
                elif(dangerDirection == Directions.SOUTH):
                    desiredDirection = Directions.NORTH
                # If our danger Direction is East
                elif(dangerDirection == Directions.EAST):
                    desiredDirection = Directions.WEST
                # If our danger Direction is west
                elif(dangerDirection == Directions.WEST):
                    desiredDirection = Directions.EAST



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
                elif(Directions.LEFT[heading] in legal):
                    # If we can turn left, lets turn left!
                    return Directions.LEFT[heading]
                #see if we can turn right
                elif(Directions.RIGHT[heading] in legal):
                    return Directions.RIGHT[heading]
                #Otherwise we can't do anything but continue down our current course!
                else:
                    # Returning our current heading
                    return heading

                #TODO Logic for what to do if we are in danger ->
                #TODO see if our direction is legal before returning it as our direction
                #return dangerDirection  # Immediately return when danger is found

                # IN it's simplist form it should look like this ->
                #if (returnDirection != Directions.STOP):
                  #  return returnDirection
        # If we're in danger follow down bellow \/
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