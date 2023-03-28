#import collections

from processing import grafo 
# do first processing to get graph without routes

g = open("data/routes.csv","r",encoding="utf-8") # route to verify which are useful

codes = []
for code,data in grafo.vertices.items():
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

# using files from using Airlabs API (check Airlabs.py)
with open("data/syria_routes.txt","r") as f:
    for line in f:
        try:
            grafo.addRoute("DAM",line[:3])
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

print(grafo.getByCountry("Colombia").routes)