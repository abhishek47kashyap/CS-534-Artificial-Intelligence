##  LIST OF FUNCTIONS
##
##  vacuum(location, status)
##  configuration(robot_position, dirt_locations)


import random   # to simulate dirt popping up in any or no location
from statistics import mean   # to compute mean performance

performance = []  # list of performance scores for all 8 configurations
lifetime = 1000   # performance evaluated over 1000 time-steps



## cleaning current location
def vacuum(location, status):
    if status == "dirty":
        return "suck"
    elif location == 'A':
        return "move right"
    elif location == 'B':
        return "move left"



## starting off from an initial configuration
def configuration(robot_position, dirt_locations):
    score = 0
    print ("Robot's initial position -", robot_position)
    print ("Dirty areas -", dirt_locations)
    
    for i in range(1, lifetime):
        if robot_position in dirt_locations:
            action = vacuum(robot_position, "dirty")
            del dirt_locations[dirt_locations.index(robot_position)]
                
        else:
            action = vacuum(robot_position, "clean")
        
        if action == "move right":
            robot_position = 'B'
        elif action == "move left":
            robot_position = 'A'
            
        # updating score
        score = score + (2 - len(dirt_locations))
        
        # random dirt generator
        location = random.randint(0, 3)
        if location == 1:
            dirt_locations.append('A')
        elif location == 2:
            dirt_locations.append('B')
        elif location == 3:
            dirt_locations.append('A')
            dirt_locations.append('B')

        # to ensure there's only one copy of A and/or B in the list
        dirt_locations = list(set(dirt_locations))

    print("Score =", score)
    print("---------------------")
    return score       



## 1 : Robot location - A, Dirt locations - A, B
print("Config. 1")
performance.append(configuration('A', ['A', 'B']))
 
## 2 : Robot location - B, Dirt locations - A, B
print("Config. 2")
performance.append(configuration('B', ['A', 'B']))

## 3 : Robot location - A, Dirt locations - A
print("Config. 3")
performance.append(configuration('A', ['A']))

## 4 : Robot location - B, Dirt locations - A
print("Config. 4")
performance.append(configuration('B', ['A']))

## 5 : Robot location - A, Dirt locations - B
print("Config. 5")
performance.append(configuration('A', ['B']))

## 6 : Robot location - B, Dirt locations - B
print ("Config. 6")
performance.append(configuration('B', ['B']))

## 7 : Robot location - A, Dirt locations - []
print("Config. 7")
performance.append(configuration('A', []))

## 8 : Robot location - B, Dirt locations - []
print("Config. 8")
performance.append(configuration('B', []))

print()
print("Mean performance score = ",mean(performance))
