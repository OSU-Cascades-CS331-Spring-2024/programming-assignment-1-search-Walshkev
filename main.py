import argparse
import BFS
import map
import dls
import a_star
import ucs







city_pairs = [
    ('brest', 'nice'),
    ('montpellier', 'calais'),
    ('strasbourg', 'bordeaux'),
    ('paris', 'grenoble'),
    ('grenoble', 'paris'),
    ('brest', 'grenoble'),
    ('grenoble', 'brest'),
    ('nice', 'nantes'),
    ('caen', 'strasbourg')
]

all_searches = ['BFS', 'DLS', 'UCS', "AStar"]


def search(myMap, start_city, goal_city, method):
  
    if method == 'BFS':
        path=  BFS.BFS(myMap, start_city, goal_city)
       
        return path
    elif method == 'DLS':
        path=  dls.DLS(myMap, start_city, goal_city)
       
        return path 
    elif method == 'AStar':
        path=  a_star.a_star(myMap, start_city, goal_city)
      
        return path 
    elif method == 'UCS':
        return ucs.ucs(myMap, start_city, goal_city)
      
        return path 


parser = argparse.ArgumentParser()
parser.add_argument('--start_city', '-A', type=str, help='Start city')
parser.add_argument('--goal_city', '-B', type=str, help='Goal city')
parser.add_argument('--search', '-S', type=str, default='BFS', help='Search method')
parser.add_argument('--map_file', '-M', type=str, help='Map file')
args = parser.parse_args()

myMap = map.Map(args.map_file)


city_pairs = [
    ('brest', 'nice'),
    ('montpellier', 'calais'),
    ('strasbourg', 'bordeaux'),
    ('paris', 'grenoble'),
    ('grenoble', 'paris'),
    ('brest', 'grenoble'),
    ('grenoble', 'brest'),
    ('nice', 'nantes'),
    ('caen', 'strasbourg')
]







total_visited_dls = 0 
total_visited_a_star = 0 
total_visited_ucs = 0 
total_visited_BFS = 0 

AStar_wins=0
DLS_wins=0 
UCS_wins = 0 
BFS_wins=0 

AStar_frontier =0 
DLS_frontier =0 
UCS_frontier =0
BFS_frontier=0 

AStar_expanded =0 
DLS_expanded =0 
UCS_expanded  =0
BFS_expanded =0 

AStar_total_frontier= 0
DLS_total_frontier=0
UCS_total_frontier=0
BFS_total_frontier=0




if args.start_city and args.goal_city:
    path = search(myMap, args.start_city, args.goal_city, args.search)
    print("the path it took is:", path[0][0])
    print("the cost is:", path[0][1])
    print("the amount places explored is:", path[1])
else:
    with open('solutions.txt', 'w') as f:
        for start_city, goal_city in city_pairs:
            temp_cost_BFS  =0
            temp_cost_dls  =0
            temp_cost_a_star =0
            temp_cost_ucs =0
            min=1000000000
            for each_search in all_searches:
                path = search(myMap, start_city, goal_city, each_search)
               
                constructed_path = path[0][0]
                cost = path[0][1]
                num_visited = path[1]
                frontier = path[2]
                
                #print(path[1])

                expanded= path[:1]
                if( each_search=="BFS"):
                    
                    temp_cost_BFS=path[0][1]
                    total_visited_BFS+=path[1]
                    BFS_frontier=path[2]
                    BFS_total_frontier+= BFS_frontier

          
                elif (each_search == 'DLS'):
                    
                    temp_cost_dls = path[0][1]
                    total_visited_dls+=path[1]
                    DLS_frontier= path[3]
                    DLS_total_frontier += DLS_frontier
                    
                   
                elif each_search == 'AStar':
                   
                    temp_cost_a_star = path[0][1]
                    total_visited_a_star+=path[1]
                    AStar_frontier= path[2]
                    AStar_total_frontier+= AStar_frontier
                    
                    
                elif each_search== 'UCS':
                    
                   
                    temp_cost_ucs= path[0][1]
                    total_visited_ucs+=path[1]
                    UCS_frontier=path[2]
                    UCS_total_frontier+= UCS_frontier
                    
                    
          
                
               
                   



                f.write(f"search type {each_search}\n")
                f.write(f"Start city: {start_city}\n")
                f.write(f"Goal city: {goal_city}\n")
                f.write(f"Path: {constructed_path}\n")
                f.write(f"Cost: {cost}\n")
                f.write(f"Number of nodes visited: {num_visited}\n")
                f.write(f"Number of frontier nodes : {frontier}\n")
                f.write(f"Number of expanded nodes : {num_visited-frontier}\n")
                f.write("\n")



            if min>=temp_cost_ucs:
                        min= temp_cost_ucs
            if min>=temp_cost_a_star:
                    min= temp_cost_a_star
            
            if min>=temp_cost_dls:
                        min= total_visited_dls
            if min>=temp_cost_BFS:
                        min= temp_cost_BFS


            #print(min)
            if min== temp_cost_a_star:
                AStar_wins+=1
            if min== temp_cost_BFS:
                BFS_wins +=1
            if min ==temp_cost_dls:
                DLS_wins+=1
            if min ==temp_cost_ucs:
                UCS_wins+=1


        BFS_expanded = total_visited_BFS - BFS_total_frontier   
        UCS_expanded = total_visited_ucs - UCS_total_frontier   
        AStar_expanded= total_visited_a_star - AStar_total_frontier   
        DLS_expanded = total_visited_dls - DLS_total_frontier        
      
    with open('README.md', 'w') as d:

        d.write(f"times BFS was most optimal: {BFS_wins}\n")
        d.write(f"times DLS was most optimal: {DLS_wins}\n")
        d.write(f"times UCS was most optimal: {UCS_wins}\n")
        d.write(f"times AStar was most optimal: {AStar_wins}\n")
        d.write("\n")

        d.write(f"average visited for BFS:{total_visited_BFS/len(city_pairs)}\n")
        d.write(f"average visited for DLS:{total_visited_dls/len(city_pairs)}\n")

        d.write(f"average visited for UCS:{total_visited_ucs/len(city_pairs)}\n")
        d.write(f"average visited for A STAR:{total_visited_a_star/len(city_pairs)}\n")

        d.write("\n")
        
        d.write(f"average expanded nodes for BFS:{BFS_expanded/len(city_pairs)}\n")
        d.write(f"average expanded nodes for DLS:{DLS_expanded/len(city_pairs)}\n")
        d.write(f"average expanded nodes for UCS:{UCS_expanded/len(city_pairs)}\n")
        d.write(f"average expanded nodes for A Star:{AStar_expanded/len(city_pairs)}\n")

        d.write("\n")  

        d.write(f"average frontier nodes for BFS:{BFS_total_frontier/len(city_pairs)}\n")
        d.write(f"average frontier nodes for DLS:{DLS_total_frontier/len(city_pairs)}\n")
        d.write(f"average frontier nodes for UCS:{UCS_total_frontier/len(city_pairs)}\n")
        d.write(f"average frontier nodes for A STAR:{AStar_total_frontier/len(city_pairs)}\n")
        d.write("\n")

        d.write(f"obviously these are not perfect i would expect the BFS and DLS to have a larger frontier than A Star and UCS\n")
        d.write(f"from the way i codded it i think the space complexity for BFS to be the highest since it has to explore more nodes before it finds the goal \n")
        d.write(f"UCS and A STAR would have the best space complexity since it is expanding in an optimized  way. \n")

        d.write(f"i think A star has a slight advantage when it comes to space and time complexity compared to UCS but it is not always give the most optimized answer\n")
        d.write(f"i am not happy with the work i did on this assignment but unfortunately i ran out of time to optimize the main file and make sure the numbers i was \n")
        d.write(f"generating in the future i will try and get to this point by monday so i can get important feed back during office hours \n")











# 1. The average number of nodes explored or entered (i.e., the number of nodes removed
# from the frontier)
# 2. The average number of nodes expanded (i.e., the total number of successors)
# 3. The average number of nodes maintained (i.e., stored in the frontier)
# 4. The number of times it found the optimal solution (optimal here is measured as “found
# the best solution out of the four search algorithms