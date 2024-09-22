
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
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """

        # 1. Is the Ghost scared?
        # We can assume we are in danger if the ghost isn't scared and vice versa
        inDanger = not ghost.isScared()

        # Marking our ghost position
        ghostPosition = ghost.getPosition

        # 2. Conditon 2 -> is the distance less than or equal to our provided
        # distance
        if(not inDanger):
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
                    return   Directions.EAST

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




        ## TODO if we are in danger but they don't share a column where are they relative to:
        #   # pacman (Up down left right ) -> this can just be a switch statement

        # We can assume PacMan isn't in danger if we haven't decided so already and return
        return Directions.STOP
        # Now that we know the distance we need to find the moves between our two
        # entities throuugh BFS

        raise NotImplemented
    
    def getAction(self, state):
        """
        state - GameState

         Each round we need to see if packman is in danger
         based off what happened last turn ->


         1. See how far the agents on the board are from packman (Search)
            TODO: Build search algorithm for finding packman distance
        """
        # Getting the position of pacMan
        pacmanPosition = state.getPacmanPosition
        # Finding out how many ghosts we have so we can check the
        # positon of all of our ghosts ->
        ghostPositions = state.getGhostPositions
        # Now that we have the number of agents we need to check each one
        ''' Possibly should be defined as:
            for ghostIndex in range(len(state.getGhostPositions())):
    ghostState = state.getGhostState(ghostIndex)

        But we won't know till testing 
        '''

        for ghost in ghostPositions:
            # Seeing if this ghost puts us in danger
            # Here we are passing the game, and our ghost position
            inDanger = self.inDanger(state, pacmanPosition, ghost)
            # This will either return ->
                    # If the pacman is not in danger, we return Directions.STOP
                    # If the pacman is in danger we return the direction to the ghost.

            # If we're in danger follow down bellow \/




        """

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
