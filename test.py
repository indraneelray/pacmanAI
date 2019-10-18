""" 
[(<__main__.GameState instance at 0x100ddecb0>, 'West'), (<__main__.GameState instance at 0x100ddedd0>, 'East')]

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  frontier = util.PriorityQueue()
  visited = dict()

  state = problem.getStartState()
  node = {}
  node["parent"] = None
  node["action"] = None
  node["state"] = state
  node["cost"] = 0
  node["eval"] = heuristic(state, problem)
  # A* use f(n) = g(n) + h(n)
  frontier.push(node, node["cost"] + node["eval"])

  while not frontier.isEmpty():
    node = frontier.pop()
    state = node["state"]
    cost = node["cost"]
    v = node["eval"]

    if visited.has_key(state):
      continue

    visited[state] = True
    if problem.isGoalState(state) == True:
      break

    for child in problem.getSuccessors(state):
      if not visited.has_key(child[0]):
        sub_node = {}
        sub_node["parent"] = node
        sub_node["state"] = child[0]
        sub_node["action"] = child[1]
        sub_node["cost"] = child[2] + cost
        sub_node["eval"] = heuristic(sub_node["state"], problem)
        frontier.push(sub_node, sub_node["cost"] + node["eval"])

  actions = []
  while node["action"] != None:
    actions.insert(0, node["action"])
    node = node["parent"]

  return actions


def aStarSearch(problem, heuristic=nullHeuristic):
    "*** YOUR CODE HERE ***"

    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    visitedNodes = []

    pQueue = util.PriorityQueue()
    #((coordinate/node , action to current node , cost to current node),priority)
    pQueue.push((startingNode, [], 0), 0)

    while not pQueue.isEmpty():

        currentNode, actions, prevCost = pQueue.pop()

        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                newCostToNode = prevCost + cost
                heuristicCost = newCostToNode + heuristic(nextNode,problem)
                pQueue.push((nextNode, newAction, newCostToNode),heuristicCost)

    util.raiseNotDefined() """

action = ['N', 'S'] 
print action + ['S']

class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    #global expanded = []

    def registerInitialState(self, state):
        expanded = []

        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP
                #global expanded
                #visited = []
                #global expanded = []
                actionstochild = []
                fringe = []
                #expanded += [state]
                #global visitedglobaldfs
                #visitedglobaldfs += [state]
                cost = admissibleHeuristic(state) + 0
                fringe.append((0, state, actionstochild, cost))
                flag = 0
                while fringe:
                    depth, curr_state, actionstocurr, huescore = fringe.pop(0)

                    if curr_state.isWin():
                        return actionstocurr[0]

                    legal = curr_state.getLegalPacmanActions()

                    successors = [(curr_state.generatePacmanSuccessor(action), action) for action in legal]
                    for successor in successors:
                        if successor[0] is None:

                            sorted(fringe, key = lambda x: (-x[3]))
                            succ_depth, statee, succ_action, cost = fringe.pop(0)
                            return succ_action[0]

                        succ_state = successor[0]
                        succ_action = actionstocurr + [successor[1]]
                        succ_depth = len(succ_action)
                        succ_score = admissibleHeuristic(succ_state) + succ_depth


                        if succ_state.isWin():
                            return succ_action[0]
                        fringe.append([succ_depth, succ_state, succ_action, succ_score])
                        sorted(fringe, key = lambda x: (-x[3]))

                if fringe:
                    sorted(fringe, key = lambda x: (-x[3]))
                    succ_depth, statee, succ_action, cost = fringe.pop(0)
                    return succ_action[0]

                    class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts

    #fringe will contain: depth, state, path, visited


    def registerInitialState(self, state):

        #change parameters ---> add score
        # each item in fringe contains the following elements:
        # ---------- depth, state, actionstogethere, loacl visited
        return;



    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write DFS Algorithm instead of returning Directions.STOP
        #print("called")
        print("-----------------------------------------------------")
        visited = []
        actionstochild = []
        fringe = list()
        global visitedglobaldfs
        visitedglobaldfs += [state]
        print(visitedglobaldfs)
        cost = admissibleHeuristic(state)
        fringe.append((0, state, actionstochild, cost))
        flag = 0
        while fringe:
            #print("len of fringe")
            #print(len(fringe))
            #print("loooooooooooooooop")
            depth, curr_state, actionstocurr, huescore = fringe.pop()
            visited = visited + [curr_state]

            if curr_state.isWin():
                return actionstocurr[0]

            legal = curr_state.getLegalPacmanActions()

            successors = [(curr_state.generatePacmanSuccessor(action), action) for action in legal]
            for successor in successors:
                #print((successor[0]))
                if successor[0] is None:
                    flag = 1
                    #continue
                    break

                #time.sleep(100)
            if not flag:
                    for successor in successors:
                        succ_state = successor[0]
                        succ_action = actionstocurr + [successor[1]]
                        succ_depth = len(succ_action)
                        succ_score = admissibleHeuristic(succ_state)
                    #print("------------------------------------")
                    #print(succ_score)

                    #if succ_state not in visited and succ_state not in visitedglobaldfs:
                    #if succ_state not in visitedglobaldfs:

                        #if succ_state.isLose():
                        #    continue
                        if succ_state.isWin():
                            return succ_action[0]
                        fringe.append([succ_depth, succ_state, succ_action, succ_score])
            #        print("visited:")
            #        print(visited)
            #        print("fringe:")
            #        print(fringe)
                    #time.sleep(20)
            if flag:
                fringe.append([depth, curr_state, actionstocurr, huescore])
                break
            #    return actionstocurr[0]
            #when will it come out of the while loop:
            # 1. When generatePacmanSuccessor gives none
            # 2. When fringe is empty
        if fringe:

            scored = [(succ_action[0], cost) for succ_depth, statee, succ_action, cost in fringe]
            bestScore = min(scored)[1]
            bestActions = [pair[0] for pair in scored if pair[1] == bestScore]
                #print(random.choice(bestActions))
            bestchoice = random.choice(bestActions)
            #print(bestchoice)
            #time.sleep(5)
            return bestchoice