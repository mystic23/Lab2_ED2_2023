import unicodedata 
import copy
# Taken from stackoverflow and Sydney(Bing)
def remove_accents(s):
    """
    takes each char after normalization form D NFD 
   of the string which decomposes accents from letters

   on the final string these accents are ignored
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
f = open("data/capitals.txt","r",encoding="utf-8") # open .txt with capitals

capitals =[] # list of capitals
for line in f:
    data = line.split(",")[1].lower()
    capitals.append(remove_accents(data))
f.close()
# save capitals in list 

check = {x:False for x in capitals}
# dict to determine which capitals are already checked

guide = {"santiago":"chile","london":"united kingdom","la paz":"bolivia",
         "kingston":"jamaica","buenos aires":"argentina","san juan":"puerto rico",
         "san jose":"costa rica"}
# corrects capital asignation for countries that have cities with capital names




# def llenar_grafo():
#     f = open("data/airports.csv","r",encoding="utf-8") # open airports database
#     from Grafo import Grafo 

#     grafo = Grafo()
#     for line in f:

#         data = line.split(",")
#         country = data[3].strip('"').lower()
#         city = data[2].lower()

#         if city in capitals and not check[city] and line.split(",")[4] !="\\N":
#             # take cities that are capitals we have not checked and that have IATA code
#             str = f"{data[1]},{data[2]},{data[3]},{data[4]},{data[6]},{data[7]}"
#             info = [x.strip('"') for x in str.split(",")]

#             if city.strip('"') in list(guide.keys()): # if city is special case
#                 #name,city,country,code,lat,long

#                 if country==guide[city.strip('"')]: # add if we have right country
#                     grafo.addAirport(info)
#                     check[city] = True
#             else:
#                 grafo.addAirport(info)
#                 check[city] = True
#                 #check city as added

#     f.close() 
#     return grafo 
# grafo = llenar_grafo()

f = open("data/airports.csv","r",encoding="utf-8") # open airports database
from Grafo import Grafo 

grafo = Grafo()

for line in f:

    data = line.split(",")
    country = data[3].strip('"').lower()
    city = data[2].lower()

    if city in capitals and not check[city] and line.split(",")[4] !="\\N":
        # take cities that are capitals we have not checked and that have IATA code
        str1 = f"{data[1]},{data[2]},{data[3]},{data[4]},{data[6]},{data[7]}"
        info = [x.strip('"') for x in str1.split(",")]

        if city.strip('"') in list(guide.keys()): # if city is special case
            #name,city,country,code,lat,long

            if country==guide[city.strip('"')]: # add if we have right country
                grafo.addAirport(info)
                check[city] = True
        else:
            grafo.addAirport(info)
            check[city] = True
            #check city as added

# Grafo temporal donde copiamos toda la información del grafo original
grafo_copy = copy.deepcopy(grafo)

# Reinicia el grafo
def restartGraph(grafo: Grafo, grafo_temp=grafo_copy):
    '''
        Reinicia el grafo

        Args:
            grafo     (Graph): [Donde queremos devolver toda la información]
            grafo_rep (Graph): [Donde se encuentra toda la información]
    '''
    grafo = grafo_temp
    return grafo


f.close() 

# # Tamaño antes de borrar
# print(len(list(grafo.vertices)))

# grafo.deleteAirport('colombia')
# grafo.deleteAirport('mexico')
# grafo.deleteAirport('venezuela')
# grafo.deleteAirport('france')

# # Tamaño despues de borrar
# print(len(list(grafo.vertices)))

# grafo = restartGraph(grafo)

# # Tamaño al reiniciar el grafo
# print(len(list(grafo.vertices)))

# print(grafo.dfs('colombia'))
print(grafo.vertices['colombia'].routes)