# worked with daniel 






def iterative_DLS(myMap, start_node, goal_node, depth_limit,explored):
    stack = [(start_node, [start_node])]
    path=[]
    visited = set()
    cameFrom = {}
    
    
    while stack:
        # print (stack)

        current, path = stack.pop()
        # path.append(current)
        visited.add(current)
      
        if current not in explored:
            explored.append(current)
        

        if current == goal_node: 
            # print(len(stack)) 

            #path[0][0] = path path[0][1] = cost  #expanded       # explored   
            return (reconstructPath(myMap, path),len(visited), len(explored),len(stack))
                
        if len(path) <= depth_limit:

            for neighbor in myMap.find_all_neighbors(current):
                    stack.append((neighbor, path+[neighbor]))
                    
                    # cameFrom[neighbor] = current
     
def DLS(myMap, start_node, goal_node):
    depth_limit=0
    explored=[]
    while True:
        path = iterative_DLS(myMap, start_node, goal_node, depth_limit, explored)
        if path:
            return path
        depth_limit+=1
    


def reconstructPath(myMap, path):
    totalCost = 0
    
    for i in range(0, len(path)-1 ):
        totalCost += myMap.find_edge_weight(path[i], path[i+1])
    return (path, totalCost)


