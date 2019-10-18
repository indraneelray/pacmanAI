# pacmanAgents.py
# ---------------
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


from pacman import Directions
from game import Agent
from heuristics import *
import random
import Queue

class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
        return actions[random.randint(0,len(actions)-1)]

class OneStepLookAheadAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        legal = state.getLegalPacmanActions()
        # get all the successor state for these actions
        successors = [(state.generatePacmanSuccessor(action), action) for action in legal]
        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(admissibleHeuristic(state), action) for state, action in successors]
        # get best choice
        bestScore = min(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # return random action from the list of the best actions
        return random.choice(bestActions)

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # Return no action if state is win or lose   
        if state.isWin() or state.isLose():
            return []
        
        # We store state, action, cost to track parent action
        fringe = []
        node = {}
        node["state"] = state
        node["action"] = []
        node["cost"] = 0
        fringe.append(node)

        while fringe:
            # Pop first element out of the queue
            f_node = fringe.pop(0)
            if f_node["state"].isWin() or f_node["state"].isLose():
                return []

            # get all legal actions for pacman 
            legal = f_node["state"].getLegalPacmanActions()
            # get all the successor state for these actions
            successors = [(state.generatePacmanSuccessor(action), action) for action in legal]            

            for state, action in successors:
                # If we run out of generatePacmanSuccessor(action) calls, return the leaf node action with minimum cost
                if state is None or state.isWin() or state.isLose():
                    # choose best action
                    scored = [node["cost"] for node in fringe]
                    if not scored:
                        continue
                    bestScore = min(scored)
                    bestActions = [node["action"] for node in fringe if node["cost"] == bestScore]
                    # We only return the first parent action which led to the best action
                    bestFirstActions = [x[0] for x in bestActions]
                    return random.choice(bestFirstActions)
                s_node = {}
                s_node["state"] = state
                s_node["action"] = f_node["action"] + [action]
                childCost = admissibleHeuristic(state)
                s_node["cost"] = childCost
                fringe.append(s_node)


class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):   
        # Return no action if state is win or lose 
        if state.isWin() or state.isLose():
            return []
        # We store state, action, cost to track parent action
        fringe = []
        node = {}
        node["state"] = state
        node["action"] = []
        node["cost"] = 0
        fringe.append(node)

        while fringe:
            # Pop last element out of the stack
            f_node = fringe.pop()
            if f_node["state"].isWin() or f_node["state"].isLose():
                return []
            # get all legal actions for pacman 
            legal = f_node["state"].getLegalPacmanActions()
            # get all the successor state for these actions
            successors = [(state.generatePacmanSuccessor(action), action) for action in legal]            

            for state, action in successors:
                # If we run out of generatePacmanSuccessor(action) calls, return the leaf node action with minimum cost
                if state is None or state.isWin() or state.isLose():
                    scored = [node["cost"] for node in fringe]
                    if not scored:
                        continue
                    bestScore = min(scored)
                    bestActions = [node["action"] for node in fringe if node["cost"] == bestScore]
                    # We only return the first parent action which led to the best action
                    bestFirstActions = [x[0] for x in bestActions]
                    return random.choice(bestFirstActions)
                s_node = {}
                s_node["state"] = state
                s_node["action"] = f_node["action"] + [action]
                childCost = admissibleHeuristic(state)
                s_node["cost"] = childCost
                fringe.append(s_node)

class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        if state.isWin() or state.isLose():
            return []
        # We store state, action, cost and admissible heuristic to track node
        fringe = []
        node = {}
        node["state"] = state
        node["action"] = []
        node["cost"] = 0
        node["admissibleHeuristic"] = admissibleHeuristic(state) + node["cost"]
        fringe.append((node))
        while fringe:
            f_node = fringe.pop(0)
            #print f_node["state"]
            if f_node["state"].isWin() or f_node["state"].isLose():
                return []

            # get all legal actions for pacman 
            legal = f_node["state"].getLegalPacmanActions()
            # get all the successor state for these actions
            successors = [(state.generatePacmanSuccessor(action), action) for action in legal]            

            for state, action in successors:
                # If we run out of generatePacmanSuccessor(action) calls, return the leaf node action with minimum cost
                if state is None or state.isWin() or state.isLose():
                    scored = [node[1]["cost"] for node[1] in fringe]
                    if not scored:
                        continue
                    bestScore = min(scored)
                    bestActions = [node["action"] for node in fringe if node["cost"] == bestScore]
                    # We only return the first parent action which led to the best action
                    bestFirstActions = [x[0] for x in bestActions]
                    return random.choice(bestFirstActions)
                s_node = {}
                s_node["state"] = state
                s_node["action"] = f_node["action"] + [action]
                s_node["admissibleHeuristic"] = admissibleHeuristic(state) 
                # f(n) = g(n) + h(n)
                s_node["cost"] = f_node["cost"] + s_node["admissibleHeuristic"]
                fringe.append((s_node))
                fringe.sort(key=lambda k: k['cost'])  

