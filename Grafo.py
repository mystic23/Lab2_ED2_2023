from geopy.distance import distance

def distance_between2(one,two):
        """
        Gets distance in km between 
        2 sets of coordinates

        Args:
            one(tuple):[lat,long of first place]
            two(tuple):[lat,long of second place]
        """
        #calls geodesic calculus
        return distance(one,two).km 

class Grafo:
    """
    Graph with airports of capitals
    """
    def __init__(self) -> None:
        self.vertices = {} # capital airports

    def addAirport(self,line):
        """
        Adds an airport

        Args:
            line(list):[contains info to create airport]
        """
        self.vertices.update({line[2].lower():Airport(line)})
        # add airport to dict
        
    def addRoute(self,country1,country2):
        """
        Adds an edge representing
        a route between 2 airports

        Args:
            country1(str)[country of first airport]
            country2(str)[country of second airport]
        """
        coords1 = self[country1].coords
        coords2 = self[country2].coords
        # save coordinates of each airport

        dist = distance_between2(coords1,coords2)
        # calculate distance

        self[country1].routes.update({country2:dist})
        self[country2].routes.update({country1:dist})
        # place target country and distance on each vertix

    def deleteAirport(self,country):
        """
        Deletes an aiport from graph
        and all routes to that country
        
        Args:
            country(str):[country of airport to delete]
        """
        adyacents = [country for country in self[country].routes.keys()]
        # register all countries with routes to country to delete
        del self.vertices[country] # delete vertix/airport

        for ady in adyacents: 
            del self[ady].routes[country]
        # delete flights/edges

    def __getitem__(self,index):
        """
        dunder method to retrieve a vertex
        """
        return self.vertices[index]

    def minDistance(self, travel_from: str, to: str):
        """
        Compute the minimal distance bewtwen two cities

        Args:   
            travel_from (str) : [name of the first city]
            to          (str) : [name of the second city]

        Return:
            (str) : returns a string with the information we wanted
        """
        # We say all the distances will be infinite except for the beginning
        distances = {vertice: float('inf') for vertice in self.vertices}
        distances[travel_from] = 0
        # A list with visited cities
        visited = set()
        parents = {}

        # We will visit all the cities in the graph
        while len(visited) < len(self.vertices):
            current_vertex = None
            current_distance = float('inf')

            # City with the minimal distance
            for vertex, distance in distances.items():
                if vertex not in visited and distance < current_distance:
                    current_vertex = vertex 
                    current_distance = distance
            
            # Just if we can't find the city we was looking for
            if current_vertex is None:
                break

            visited.add(current_vertex)

            # Update the distances (remind we initialized in infinity all of those distances)
            for neighbor, weight in self.vertices[current_vertex].routes.items():
                distance_two = distances[current_vertex] + weight

                if distance_two < distances[neighbor]:
                    distances[neighbor] = distance_two
                    parents[neighbor] = current_vertex


        # We build a distance if we found a path
        if to not in parents:
            return float('inf'), []

        path = [to]
        father = parents[to]

        while father != travel_from:
            path.insert(0, father)
            father = parents[father]

        path.insert(0, travel_from)
        # We capitalize all the names
        path = [path.title() for path in path]
        titulo = '''
        
██████╗ ██╗   ██╗████████╗ █████╗      ██████╗ ██████╗ ████████╗██╗███╗   ███╗ █████╗     ██████╗ ███████╗    ██╗   ██╗██╗ █████╗      ██╗███████╗
██╔══██╗██║   ██║╚══██╔══╝██╔══██╗    ██╔═══██╗██╔══██╗╚══██╔══╝██║████╗ ████║██╔══██╗    ██╔══██╗██╔════╝    ██║   ██║██║██╔══██╗     ██║██╔════╝
██████╔╝██║   ██║   ██║   ███████║    ██║   ██║██████╔╝   ██║   ██║██╔████╔██║███████║    ██║  ██║█████╗      ██║   ██║██║███████║     ██║█████╗  
██╔══██╗██║   ██║   ██║   ██╔══██║    ██║   ██║██╔═══╝    ██║   ██║██║╚██╔╝██║██╔══██║    ██║  ██║██╔══╝      ╚██╗ ██╔╝██║██╔══██║██   ██║██╔══╝  
██║  ██║╚██████╔╝   ██║   ██║  ██║    ╚██████╔╝██║        ██║   ██║██║ ╚═╝ ██║██║  ██║    ██████╔╝███████╗     ╚████╔╝ ██║██║  ██║╚█████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚═╝        ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝      ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚══════╝
                                                                                                                                                  
        '''
        agregar_bonito = '\n\t[+] '.join(path)
        print(titulo)
        return f'La distancia minima para ir de {travel_from} hasta {to} es de {round(distances[to], 2)}km con la siguiente ruta: \n\t[+] {agregar_bonito}'
    
class Airport:
    def __init__(self, line:list) -> None:
        self.name = line[0]
        self.city = line[1]
        self.country = line[2].lower()
        self.code = line[3] # IATA code
        self.coords = (line[4],line[5])
        self.routes = {}

    def __repr__(self) -> str:
        return f"{self.name} in {self.city},{self.country}"
    
if __name__ =="__main__":
    pass