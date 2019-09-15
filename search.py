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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    # a = input('digite 42')
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    from game import Directions
    from util import Stack
    import copy
    # initialize problems
    currentState =  problem.getStartState()
    iCurrentDepth = 1
    # 666 because autograder expected the real dfs search and not the iterative one
    iMaxDepth = 666
    # moves = []
    visited = []
    stack = Stack()
    moveStack = Stack()
    # costStack = Stack()
    depthStack = Stack()
    #print "Stacks Criadas"
    while True:
        # inicializa pilhas
        stack.push(problem.getStartState())
        iCurrentDepth = 1
        moveStack.push([])
        depthStack.push(1)
        visited = []
        while iCurrentDepth < iMaxDepth:
            currentState = stack.pop()
            moves = moveStack.pop()
            visited.append(currentState)
            iCurrentDepth = depthStack.pop()
            
            if problem.isGoalState(currentState):
                #print "SAIDA DE movimentos", str(moves)
                return moves
            else:
                #print"estado atual", currentState
                NewStates = problem.getSuccessors(currentState)
                #print "sucessors", NewStates
                if moves is None:
                    moves = []
                    
                for (State, Action, Cost) in NewStates:
                    if State not in visited:
                        stack.push(State)
                        moveState = copy.deepcopy(moves)
                        moveState.append(Action) 
                        #print "Move state", str(moveState)
                        moveStack.push(moveState)       
                        depthStack.push(iCurrentDepth + 1)
                        
                #stackCp = copy.deepcopy(stack)
                #out = ""
                #while not stackCp.isEmpty():
                #    out = out + "," + str(stackCp.pop())
                
                # print "queue state", out 
        # print "Avanca iMaxDepth {0}".format(iMaxDepth)
        iMaxDepth +=1
         
            


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

class uniformCostNode:
    def __init__(self, Path, Node, Cost):
        self.path = Path
        self.node = Node
        self.cost = Cost
    def __eq__(self, other):
        return self.node == other.node
    def __ne__(self, other):
        return not self.__eq__(other)    
def uniformCostSearch(problem):
    import copy
    from util import PriorityQueue
    borda = PriorityQueue()
    closed_list = []
    current_path =[]
    cost = 0
    # pushes initial state to queue with zero priority
    borda.update(uniformCostNode(current_path, problem.getStartState(), cost), 0)
    while not borda.isEmpty():
                #(current_path,current_node, cost) = borda.pop()
        CurrentNode = borda.pop()
        current_path = CurrentNode.path
        current_node = CurrentNode.node
        cost =         CurrentNode.cost
        closed_list.append(current_node)
        if problem.isGoalState(current_node):
            #TODO adicionar lista
            #print "path returned {0}".format(str(current_path))
            return current_path
        NewStates = problem.getSuccessors(current_node)
        cost_until_father = cost #- heuristic(current_node, problem)
        for (childNode, Action, Cost) in NewStates:
            # only add not visited nodes
            if (childNode not in closed_list):
                # child_cost = cost_until_father + Cost + heuristic(childNode, problem)
                child_path = copy.deepcopy(current_path)
                child_path.append(Action)
                child_cost = problem.getCostOfActions(child_path)
                borda.update(uniformCostNode(child_path, childNode, child_cost), child_cost)
            else:
                print"child node {0} already in closed_list".format(str(childNode), str(closed_list)) 
    util.raiseNotFound()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

class aStarNode:
    def __init__(self, Path, Node, Cost):
        self.path = Path
        self.node = Node
        self.cost = Cost
    def __eq__(self, other):
        return self.node == other.node
    def __ne__(self, other):
        return not self.__eq__(other)
        
def aStarSearch(problem, heuristic=nullHeuristic):
    import copy
    from util import PriorityQueue
    borda = PriorityQueue()
    closed_list = []
    current_path =[]
    cost = 0
    # pushes initial state to queue with zero priority
    borda.update(aStarNode(current_path, problem.getStartState(), cost), 0)
    while not borda.isEmpty():
        #(current_path,current_node, cost) = borda.pop()
        CurrentNode = borda.pop()
        current_path = CurrentNode.path
        current_node = CurrentNode.node
        cost =         CurrentNode.cost
        #print "Expanded node {0} cost {1}".format(str(current_node), str(cost))
        closed_list.append(current_node)
        if problem.isGoalState(current_node):
            #TODO adicionar lista
            #print "path returned {0}".format(str(current_path))
            return current_path
        NewStates = problem.getSuccessors(current_node)
        cost_until_father = cost - heuristic(current_node, problem)
        for (childNode, Action, Cost) in NewStates:
            # only add not visited nodes
            if (childNode not in closed_list):
                # child_cost = cost_until_father + Cost + heuristic(childNode, problem)
                child_path = copy.deepcopy(current_path)
                child_path.append(Action)
                child_cost = problem.getCostOfActions(child_path) + heuristic(childNode, problem)
                borda.update(aStarNode(child_path, childNode, child_cost), child_cost)
            else:
                print"child node {0} already in closed_list".format(str(childNode), str(closed_list)) 
    #raise Exception "No path avaliable"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
