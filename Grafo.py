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
    
class Airport:
    def __init__(self,line:list) -> None:
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