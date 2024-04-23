from map import Map

file= 'france.txt'
map = Map(file)

def ucs(myMap, start, goal):
    cameFrom = {}
    gscore = {}  # Initialize gscore dictionary
    gscore[start] = 0

    openSet = {start: 0}  # Add start node to openSet
    visisted = 0 

    while openSet:
        current = min(openSet, key=openSet.get)
       

        if current == goal:
            return (reconstructPath(myMap,cameFrom, current) ,visisted,len(openSet))
            # return "heck yes"
        del openSet[current]

        for neighbor in myMap.find_all_neighbors(current):
            tentative_gScore = gscore[current] + myMap.find_edge_weight(current, neighbor)
            if neighbor not in gscore or tentative_gScore < gscore[neighbor]:
                visisted+=1
                cameFrom[neighbor] = current
                gscore[neighbor] = tentative_gScore 

                if neighbor not in openSet:
                    openSet[neighbor] = gscore[neighbor]  

    return 'failure'



def reconstructPath(myMap,cameFrom, current):

    previous_node = current
    

    totalPath = [] 
    totalCost= 0 
    

    while current in cameFrom.keys():
        previous_node = current
        current = cameFrom[current]
        totalCost+=myMap.find_edge_weight(current, previous_node)
        move = previous_node
        totalPath.append(move)
    totalPath.append(current)
    totalPath.reverse()
    return (totalPath, totalCost)

# test_path = ucs(map, 'brest', 'nice')
# print("the path it took is :" , test_path[0][0])
# print ("the cost is :", test_path[0][1])
# print ( "the amount places exploried is: ", test_path[1] )

