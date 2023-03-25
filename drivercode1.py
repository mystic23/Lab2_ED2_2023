#import collections

from new_processing import grafo 
# do first processing to get graph without routes

g = open("data/routes.csv","r",encoding="utf-8") # route to verify which are useful

codes = []
countries = []
for code,data in grafo.vertices.items():
    codes.append(code)
    countries.append(data.country)

# store all codes and countries from graph

#print([item for item, count in collections.Counter(countries).items() if count > 1])
# was used to get repeated countries

for line in g: 
    data = line.split(",")
    code1 = data[2]
    code2 = data[4]
    # add route between airports if both are capitals
    if code1 in codes and code2 in codes:
        grafo.addRoute(code1,code2)
g.close() 

empty = []
for code,airport in grafo.vertices.items():
    if len(airport.routes) ==0:
        empty.append([airport.country,airport.city,code,len(airport.routes)])
# save aiports without routes

debug = open("data/empty_routes.txt","w",encoding="utf-8")
for x in empty:
    debug.write(f"{str(x)}\n")
debug.close()
# add them to a txt and make changes to files to correct 

print(grafo.getByCountry("Colombia").routes)
