#import collections

from processing import grafo
# do processing first to get graph without routes

g = open("data/routes.csv","r",encoding="utf-8") # route to verify which are useful

codes = {}
for key,airport in grafo.vertices.items():
    codes.update({airport.code:key})
# have reference of code with country

codigos = list(codes.keys())
# only codes
for line in g: 
    data = line.split(",")
    code1 = data[2]
    code2 = data[4]
    # add route between airports if both are capitals
    # using country reference from codes
    if code1 in codigos and code2 in codigos:
        grafo.addRoute(codes[code1],codes[code2])
g.close() 

# After checking empty routes that need correction
# we use data extracted from Airlabs API (see README.md)
with open("data/syria_routes.txt","r") as f:
    for line in f:
        try:
            grafo.addRoute("syria",codes[line[:3]])
            # slice to ignore "\n"
        except:
            pass 

# add updated routes for Syria
with open("data/guiana_routes.txt","r") as f:
    for line in f:
        try:
            grafo.addRoute("french guiana",codes[line[:3]])
        except:
            pass
# add updated routes for French Guyana

for country,airport in list(grafo.vertices.items()):
    if len(airport.routes) ==0:
        grafo.vertices.pop(country)
#Delete airports without routes from graph


# dist,path = grafo.minDistance("colombia","french guiana")
