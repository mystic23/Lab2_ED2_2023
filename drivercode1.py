#import collections

from processing import grafo 
# do processing first to get graph without routes

g = open("data/routes.csv","r",encoding="utf-8") # route to verify which are useful

codes = []
for code in grafo.vertices.keys():
    codes.append(code)
# store all codes and countries from graph

for line in g: 
    data = line.split(",")
    code1 = data[2]
    code2 = data[4]
    # add route between airports if both are capitals
    if code1 in codes and code2 in codes:
        grafo.addRoute(code1,code2)
g.close() 

# using data extracted from Airlabs API (see README)
with open("data/syria_routes.txt","r") as f:
    for line in f:
        try:
            grafo.addRoute("DAM",line[:3])
            # slice to ignore "\n"
        except:
            pass 
# add updated routes for Qatar
with open("data/guiana_routes.txt","r") as f:
    for line in f:
        try:
            grafo.addRoute("CAY",line[:3])
        except:
            pass
# add updated routes for French Guyana

for code,airport in list(grafo.vertices.items()):
    if len(airport.routes) ==0:
        grafo.vertices.pop(code)
        del grafo.guide[airport.country.lower()]
#Delete airports without routes from graph

print(grafo.getByCountry("colombia").routes)
