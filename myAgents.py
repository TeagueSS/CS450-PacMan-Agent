
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

    def inDanger(self,state , pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column, -> Does this even require walls?
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """

        # 1. Is the Ghost scared?
        # We can assume we are in danger if the ghost isn't scared and vice versa
        inDanger = not ghost.isScared()

        # Marking our ghost position
        ghostPosition = ghost.getPosition()

        # 2. Conditon 2 -> is the distance less than or equal to our provided
        # distance
        if(inDanger):
            # Getting our distance from the Manhattan function
            distance = manhattanDistance(pacman, ghostPosition)
            # Checking if it is greater than our distance
            if distance <= dist:
                inDanger = True

        #TODO 3. Check if we are in the same row or column as our ghost
        # We have to check both row and column so checking row first

        # Saving our direction (Where our ghost is at)
        # We can assume we aren't in danger and can edit it later
        ghostDirection = Directions.STOP

        # Saving our walls / gameBoard
        walls = state.getWalls()
        # Checking if they share a y height
        if(pacman[1] == ghostPosition[1] ):

            # if they do we can check their left and right and mark for line of site
            # Seeing who is on the left and who is on the right ->
            if(pacman[0] < ghostPosition[0]):
                # packman is to the left, we look right for a line of site ->
                # bool to mark if we can see the gost without a wall
                clearLineOfSight = True
                '''
                Starting at PacMans position we are going to increase to the right 
                Until we either reach a wall, or get to our Ghost's positon 
                '''
                checkRow = pacman[0]
                # While we have a clear line of site and we haven't passed our ghost's
                # x value (Row)
                while(clearLineOfSight and checkRow < ghostPosition[0]):
                    # Seeing if there is a wall in the way
                    if(walls[checkRow][pacman[1]]):
                        # If we found a wall our clear line of site is false
                        clearLineOfSight = False

                    #Otherwise there was no wall
                    else:
                        #And we increase our row shift ->
                        checkRow += 1

                # Now if we have seen a ghost
                if (clearLineOfSight):
                    # Returning to the right of us which should be east
                    return Directions.EAST

            # Otherwise we can the ghost is to the left of PacMan
            else:
                # bool to mark if we can see the gost without a wall
                clearLineOfSight = True
                # Marking where we are looking (Our starting x and y)
                checkRow = pacman[0]
                # While we have a clear line of site and we haven't passed our ghost's
                # x value (Row)
                while (clearLineOfSight and checkRow > ghostPosition[0]):
                    # Here our check walls should our x moving over and the same y as our PacMan
                    if (walls[checkRow][pacman[1]]):
                        # If we found a wall our clear line of site is false
                        clearLineOfSight = False
                    # Increasing our row shift
                    checkRow -= 1
                if (clearLineOfSight):
                    # Returning to the right of us which should be west as they are to
                    # The left and there is no wall
                    return Directions.WEST
        # If they don't share  column we check if they share a row ->
        elif(pacman[0] == ghostPosition[0]):
            # If they Share a row we can check up and down (If they can see each other in the column:
            # Marking the column we wish to check ->
            checkCol = pacman[1]
            # If pacman is higher look down
            if(pacman[1] > ghostPosition[1]):
                # bool to mark if we can see the gost without a wall
                clearLineOfSight = True
                # Looping while we haven't passed the ghost or ran into a wall ->
                while clearLineOfSight and checkCol < ghostPosition[1]:
                    # seeing if there's a wall
                    if walls[pacman[0]][checkCol]:
                        clearLineOfSight = False
                    checkCol += 1
                # If after checking along our column we can see the ghost return that
                # He is above us
                if clearLineOfSight:
                    return Directions.SOUTH  # Or SOUTH, based on direction

            # Otherwise we can assume pacman is lower and look up
            else:
                # bool to mark if we can see the gost without a wall
                clearLineOfSight = True
                # Looping while we haven't passed the ghost or ran into a wall ->
                while clearLineOfSight and checkCol > ghostPosition[1]:
                    # seeing if there's a wall
                    if walls[pacman[0]][checkCol]:
                        clearLineOfSight = False
                    checkCol -= 1
                # If after checking along our column we can see the ghost return that
                # He is above us
                if clearLineOfSight:
                    return Directions.NORTH  # Or SOUTH, based on direction

        ''' STEP 4: if we are in danger (Which we should already know), we need to return 
        from what direction the danger is coming from -> '''

        if (inDanger):
            # Check if Pacman and the ghost are in the same row
            if pacman[1] == ghostPosition[1]:
                # If Pacman is to the left of the ghost, return EAST
                if pacman[0] < ghostPosition[0]:
                    return Directions.EAST
                # Otherwise, Pacman is to the right of the ghost, return WEST
                else:
                    return Directions.WEST
            # If not in the same row, check if they are in the same column
            elif pacman[0] == ghostPosition[0]:
                # If Pacman is below the ghost, return NORTH
                if pacman[1] < ghostPosition[1]:
                    return Directions.NORTH
                # Otherwise, Pacman is above the ghost, return SOUTH
                else:
                    return Directions.SOUTH
        '''    # Check which direction is greater ->                                      |
            if(abs(pacman[0] - ghostPosition[0]) >= abs(pacman[1] - ghostPosition[1])):   |  
                # Now we know that our x distance is greater                              |
                # So lets return the closest y - Direction                                |
                if(pacman[1] > ghostPosition[1]):                                         |
                    # If pacman is above then our ghost is below!                         |
                    return Directions.SOUTH                                               |
                else:                                                                     |
                    #Otherwise we can say the ghost is above pacman                       |    Teague
                    return Directions.NORTH                                               |
            else:                                                                         |
                #now we know that our y distance is greater                               |
                #So we return whatever x distance is greater                              |
                if(pacman[1] > ghostPosition[1]):                                         |
                    # If pacman is to the right then the ghost is to the left (West)      |
                    return Directions.WEST                                                |
                else:                                                                     |
                    # If pacman is to the left, then the ghost is to the right (East)     |
                    return Directions.EAST                                                |
        '''
        #If he isn't in danger then we can return stop ->
        return Directions.STOP

        #raise NotImplemented
    
    def getAction(self, state):

        # Getting the position of pacMan
        pacmanPosition = state.getPacmanPosition()
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
        returnDirection = state.getDirection()

        # Getting our ghost states as an array
        ghostStates = state.getGhostStates()  # Retrieves a list of ghost states
        # Checking if pacman is in danger ->
        #for ghostState in ghostStates:
        #    returnDirection = self.inDanger(state, pacmanPosition, ghostState)

        # Carlos' Version: The previous loop kept on checking for Pacman in danger
        # This way it checks for danger once at time and it takes better decision according to the Ghosts' location.
        for ghostState in ghostStates:
            dangerDirection = self.inDanger(state, pacmanPosition, ghostState)
            if dangerDirection != Directions.STOP:
                return dangerDirection  # Immediately return when danger is found

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
        # IN it's simplist form it should look like this ->
        if(returnDirection != Directions.STOP):
            return returnDirection
        '''
        4. -> If not in danger ->
            We act like left turn agent (We can just copy that code)
        '''
        ##TODO This is the existing left turn agent code ->
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

