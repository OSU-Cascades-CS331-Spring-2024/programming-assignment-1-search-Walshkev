class Map:
    def __init__(self, file):
        self.map = self.open_file(file)
    
    def open_file(self, file):
        with open(file, 'r') as file:
            map = {}
            for line in file:
                words = line.split()
                arrow_index = words.index('-->')
                city = words[:arrow_index]
                
                neighbors = {}
                for i in range(arrow_index+1, len(words), 2):
                    neighbor = str(words[i].replace('va-', ''))
                    weight = int(words[i+1])
                    
                    neighbors[neighbor] = weight
            
                map[city[0]] = {"neighbors": neighbors , "coords": city[1:]}
        return map
    
    def find_edge_weight(self, start_city, neighbor_city):
        return self.map[start_city]["neighbors"][neighbor_city]
        
    def find_all_neighbors(self, city):
        return self.map[city]['neighbors'].keys()
    
    def get_lat_and_long(self, city):
        lat_hour = self.map[city]['coords'][0]
        lat_min = self.map[city]['coords'][1]
        lat_sec = self.map[city]['coords'][2]
        cardinalNS = self.map[city]['coords'][3]
        long_hour = self.map[city]['coords'][4]
        long_min = self.map[city]['coords'][5]
        long_sec = self.map[city]['coords'][6]
        cardinalEW = self.map[city]['coords'][7]
        return (lat_hour, lat_min, lat_sec, cardinalNS, long_hour, long_min, long_sec, cardinalEW)
