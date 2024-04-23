
import queue





def BFS(myMap, start_node, goal):
   
    visited = [start_node]
    Q = queue.Queue()
    Q.put(start_node)
    came_from = {} 

    while not Q.empty():
        current_node = Q.get()
        for dict_keys in myMap.find_all_neighbors(current_node):
            if dict_keys == goal:
                
                Q.put(dict_keys)
                visited.append(dict_keys)
                came_from[dict_keys] = current_node
               
                current_node = goal
                
                number_of_nodes_visited = len(visited)
                return (reconstructPath(myMap, came_from, current_node), number_of_nodes_visited, len(Q.queue))
            elif dict_keys not in visited:
                Q.put(dict_keys)
                visited.append(dict_keys)
                came_from[dict_keys] = current_node  

        


  

    return "Could not find a path"


def reconstructPath(myMap, cameFrom, current):

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


