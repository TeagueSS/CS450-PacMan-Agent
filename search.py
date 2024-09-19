# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import game
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def genericSearch(problem, g, h):
    state = problem.getStartState()
    goal = problem.goal


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    #util.raiseNotDefined()

def breadthFirstSearch(problem):

    """Search the shallowest nodes in the search tree first."""
    ##PositionSearchProblem(gameState, start=point1, goal=point2, warn=False, visualize=False)
    # Important note:
    # All of your search functions need to return a list of actions that will
    # lead the agent from the start to the goal.

    # These actions all have to be legal moves:
    # - Valid directions
    # - No moving through walls

    # gaving our goal locally
    goal = problem.getGoalState()
    start = problem.getStartState()
    # How to get walls from our current state
    wallsGrid = problem.walls
    #Saving the width and height of our board:
    width = wallsGrid.width
    height = wallsGrid.height

    # We need to make a matrix of visited places to see
    # if we have already traveresed in our journey:
    visitedGrid = [[False for _ in range(height)] for _ in range(width)]

    # Marking our start state on this grid as true (This is where)
    # We are starting ->
    visitedGrid[start[0]][start[1]] = True

    #BFS algorithm
    # https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

    # We need to return a list of commands for how to move
    # So our Queue should compensate for this fact:

    # Once we have our stack ->
    # getting our board so we can see it
    print(wallsGrid)
    print("*****************************************")
    print(visitedGrid)

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch ##TODO






dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
