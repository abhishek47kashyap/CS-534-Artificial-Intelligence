## LIST OF FUNCTIONS
##
##  vectorize(config) - converts matrix 'config' into a 1-D array
##  Nmod2_test(config) - for initial state 'config', determines reachable Goal state
##  index(config, element) - returns location of 'element' in the 3 X 3 matrix 'config'
##  heuristic(config) - returns the Manhattan Distance heuristic value
##  print_config(config) - prints out any state 'config' in a 3 X 3 grid

## NOTE
## This program has been written in Python 3.5.2.
## Attempts to run this on lower versions might produce unexpected errors.
## For eg., Python 3 treats print() as a function unlike Python 2.

import copy

Goal_A = [[1, 2, 3], [8, 'X', 4], [7, 6, 5]]
Goal_B = [['X', 1, 2], [3, 4, 5], [6, 7, 8]]

input_config = [[2, 8, 3], [1, 6, 4], [7, 'X', 5]]  # leads to Goal_A
# input_config = [[7, 2, 4], [5, 'X', 6], [8, 3, 1]]  # leads to Goal_B
# input_config = [[1, 8, 2], [7, 3, 5], [4, 6, 'X']]   # Random initial state

def vectorize(config):  # Vectorizes into a 1-D array
    v = []
    for i in range(0, len(config)):
        v.extend(config[i])
    return v

def Nmod2_test(config): # Performs the 'N mod 2' test
    vec = vectorize(config)
    del vec[vec.index('X')]
    Nmod2 = 0
    for N in range(0, len(vec)):
        count = 0
        for i in range((N+1), len(vec)):
            if vec[i] < vec[N]:
                count += 1
        Nmod2 += count
    return (Nmod2 % 2)

def index(config, element): # Determines index of 'element' in 'config'
    vec = vectorize(config)
    return [((int)(vec.index(element) / 3)), (vec.index(element) % 3)]
    
def heuristic(config):  # Calculates heuristics based on Manhattan Distance
    h = 0
    for N in range(1, 9):
        a = index(config, N)
        b = index(goal, N)
        h += abs(a[0] - b[0]) + abs(a[1] - b[1])
    return h
    
def print_config(config):   # Prints the state in a 3 X 3 grid
    print("-------")
    print(config[0])
    print(config[1])
    print(config[2])
    print("-------")
    print()


## PROGRAM STARTS HERE
print("Starting configuration:")
print_config(input_config)

status = "success"  # will be changed to 'failure' if the goal cannot be reached

# Making out the Goal state
if Nmod2_test(input_config) == Nmod2_test(Goal_A):
    print("Goal A configuration")
    print_config(Goal_A)
    goal = Goal_A
else:
    print("Goal B configuration")
    print_config(Goal_B)
    goal = Goal_B


current = input_config
frontier = []   # elements to be expanded
closed = []     # already expanded states
step_cost = 1   # cost function w.r.t. initial state

## A* SEARCH begins here
while current != goal:
    ind = index(current, 'X')   # position of 'X' (blank tile)

    # Adding valid neighbours of the blank tile to the Frontier
    top = [a + b for a, b, in zip(ind, [-1, 0])]
    bottom = [a + b for a, b in zip(ind, [1, 0])]
    left = [a + b for a, b in zip(ind, [0, -1])]
    right = [a + b for a, b in zip(ind, [0, 1])]

    [x_prev, y_prev] = ind
    
    if max(top) < 3 and min(top) >= 0:
        curr = copy.deepcopy(current)
        [x_new, y_new] = top
        curr[x_prev][y_prev], curr[x_new][y_new] = curr[x_new][y_new], curr[x_prev][y_prev]
        if curr not in closed:
            frontier.append([(step_cost + heuristic(curr)), curr])

    if max(bottom) < 3 and min(bottom) >= 0:
        curr = copy.deepcopy(current)
        [x_new, y_new] = bottom
        curr[x_prev][y_prev], curr[x_new][y_new] = curr[x_new][y_new], curr[x_prev][y_prev]
        if curr not in closed:
            frontier.append([(step_cost + heuristic(curr)), curr])

    if max(left) < 3 and min(left) >= 0:
        curr = copy.deepcopy(current)
        [x_new, y_new] = left
        curr[x_prev][y_prev], curr[x_new][y_new] = curr[x_new][y_new], curr[x_prev][y_prev]
        if curr not in closed:
            frontier.append([(step_cost + heuristic(curr)), curr])

    if max(right) < 3 and min(right) >= 0:
        curr = copy.deepcopy(current)
        [x_new, y_new] = right
        curr[x_prev][y_prev], curr[x_new][y_new] = curr[x_new][y_new], curr[x_prev][y_prev]
        if curr not in closed:
            frontier.append([(step_cost + heuristic(curr)), curr])

    closed.append(current)  # Already expanded state added to 'Closed List'

    if len(frontier) == 0:  # When there are no more states to be explored
        status = "failure"
        break

    # Sorting the elements in the 'Frontier'
    front = copy.deepcopy(frontier)
    frontier = []
    for states in sorted(front, key = lambda states: states[0]):    
        frontier.append(states)

    # Selecting state for further expansion
    current = frontier[0][1]
    del frontier[0]
    
    step_cost += 1

    

if status == "success":
    print("Goal state achieved!")
elif status == "failure":
    print("Goal not found!")

























