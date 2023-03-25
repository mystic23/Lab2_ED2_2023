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
        self.guide = {} # links country to code

    def addAirport(self,line):
        """
        Adds an airport

        Args:
            line(list):[contains info to create airport]
        """
        self.vertices.update({line[3]:Airport(line)})
        # add airport to dict
        self.guide.update({line[2]:line[3]})
        # add reference to guide
        
    def addRoute(self,code1,code2):
        """
        Adds an edge representing
        a route between 2 airports

        Args:
            code1(str)[code of first airport]
            code2(str)[code of second airport]
        """
        coords1 = self[code1].coords
        coords2 = self[code2].coords
        # save coordinates of each airport

        country1 = self[code1].country
        country2 = self[code2].country
        # save country of each airport

        dist = distance_between2(coords1,coords2)
        # calculate distance

        self[code1].routes.update({country2:dist})
        self[code2].routes.update({country1:dist})
        # place target country and distance on each vertix

    def getByCountry(self,country):
        """
        gets the Airport object with 
        the country name using guide
        """
        #guide returns the code used by getitem
        return self[self.guide[country]]
    
    def __getitem__(self,index):
        """
        dunder method to retrieve a vertex
        """
        return self.vertices[index]
    
class Airport:
    def __init__(self,line:list) -> None:
        self.name = line[0]
        self.city = line[1]
        self.country = line[2]
        self.IATA = line[3]
        self.coords = (line[4],line[5])
        self.routes = {}

    def __repr__(self) -> str:
        return f"{self.name} in {self.city},{self.country}"
    
if __name__ =="__main__":
    pass