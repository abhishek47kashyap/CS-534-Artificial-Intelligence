## NOTE
## This program has been written in Python 3.5.2.
## Attempts to run this on lower versions might produce unexpected errors.
## For eg., Python 3 treats print() as a function unlike Python 2.

# States are represented as [m, c, b] where:
# m - no. of missionaries on the wrong side of the river
# c - no. of cannibals on the wrong side of the river
# b - no. of boats on the wrong side of the river

## LIST OF FUNCTIONS
##
## valid(child) - checks if m and/or c is between 0-3 and if m >= c
## generate_children(state) - generates child states of 'state'

import copy

start = [3, 3, 1]
goal = [0, 0, 0]
moves = [[1, 1, 1], [0, 1, 1], [0, 2, 1], [1, 0, 1], [2, 0, 1]]

def valid(child):   # Checks for illegal states
    if child[0] >= child[1]:
        if child[0] <= 3 and child[1] <=3 and child[0] >= 0 and child[1] >= 0:
            if child not in closed:
                return "valid"
    else:
        return "illegal"

def generate_children(state):   # Generates children nodes from 'state'
    next_states = []
    child = []
    for next_move in moves:
        if state[2] == 1:
            child = [x - y for x, y in zip(state, next_move)]
        else:
            child = [x + y for x, y in zip(state, next_move)]

        if valid(child) == "valid" and child not in frontier:
            next_states.append(child)

    return next_states
            

goal_found = 0; # will be updated to 1 if goal found
current = []    # current node for expansion
frontier = [copy.deepcopy(start)]   # states to be expanded
closed = []     # already explored states
child_parent = []   # keeps track of parent of every child
path = []   # nodes from 'start' to 'goal'

while current != goal:
    current = frontier.pop(0)
    
    if current == goal:
        goal_found = 1
        break
    else:
        children = generate_children(current)

        for k in range(len(children)):
            child_parent.append([children[k], current])
        
        closed.append(current)
        frontier += children


if goal_found == 1:
    print("Goal reached!")
    child = copy.deepcopy(goal)
    path.append(goal)

    while child != start:
        for j in range(len(child_parent)):
            if child == child_parent[j][0]:
                child = child_parent[j][1]
                path.append(child)
            
    path.reverse()
    print("Path :", path)
else:
    print("Goal not found!")
    

