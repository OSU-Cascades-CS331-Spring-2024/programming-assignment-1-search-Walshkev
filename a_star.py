import math 




def a_star(myMap, start, goal):
   
    cameFrom = {}
    gscore = {}  
    gscore[start] = 0

   

    openSet = {start: 0}  
    visisted = 0 

    while openSet:
        current = min(openSet, key=openSet.get)
       

        if current == goal:
            return (reconstructPath(myMap,cameFrom, current) , visisted,len(openSet))
            # return "heck yes"
        del openSet[current]

        for neighbor in myMap.find_all_neighbors(current):
            tentative_gScore = gscore[current] + myMap.find_edge_weight(current, neighbor)
            if neighbor not in gscore or tentative_gScore < gscore[neighbor]:
                visisted+=1
                cameFrom[neighbor] = current
                gscore[neighbor] = tentative_gScore + heuristic(myMap, neighbor, goal)

                if neighbor not in openSet:
                    openSet[neighbor] = gscore[neighbor]  

    return 'failure'

def heuristic(myMap, Start, End):

    Start_lat_hour = int(myMap.map[Start]['coords'][0])
    Start_lat_min = int(myMap.map[Start]['coords'][1])
    Start_lat_sec = int(myMap.map[Start]['coords'][2])
    Start_cardinalNS = str(myMap.map[Start]['coords'][3])
    Start_long_hour = int(myMap.map[Start]['coords'][4])
    Start_long_min = int(myMap.map[Start]['coords'][5])
    Start_long_sec = int(myMap.map[Start]['coords'][6])
    Start_cardinalEW = str(myMap.map[Start]['coords'][7])
    
    End_lat_hour = int(myMap.map[End]['coords'][0])
    End_lat_min = int(myMap.map[End]['coords'][1])
    End_lat_sec = int(myMap.map[End]['coords'][2])
    End_cardinalNS = str(myMap.map[End]['coords'][3])
    End_long_hour = int(myMap.map[End]['coords'][4])
    End_long_min = int(myMap.map[End]['coords'][5])
    End_long_sec = int(myMap.map[End]['coords'][6])
    End_cardinalEW = str(myMap.map[End]['coords'][7])

    start_pos_lat = Start_lat_hour + Start_lat_min/60 + Start_lat_sec/3600
    if Start_cardinalNS == 'S':
                start_pos_lat *= -1      

    start_pos_lon = Start_long_hour + Start_long_min/60 + Start_long_sec/3600
    if Start_cardinalEW == 'W':
            start_pos_lon *= -1     

    End_pos_lat = End_lat_hour + End_lat_min/60 + End_lat_sec/3600
    if End_cardinalNS == 'S':
            End_pos_lat *= -1 

    End_pos_lon = End_long_hour + End_long_min/60 + End_long_sec/3600
    if End_cardinalEW == 'W':
            End_pos_lon *= -1   

    lat1 = int(myMap.map[Start]['coords'][0])
    lon1 = int(myMap.map[Start]['coords'][4])

    lat2 = int(myMap.map[End]['coords'][0])
    lon2 = int(myMap.map[End]['coords'][4])

    distance = math.acos((math.sin(math.radians(start_pos_lat)) * math.sin(math.radians(End_pos_lat))) + (math.cos(math.radians(start_pos_lat)) * math.cos(math.radians(End_pos_lat))) * (math.cos(math.radians(End_pos_lon) - math.radians(start_pos_lon)))) * 6371


    return distance


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



