import unicodedata 

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
# save capitals in list and sort list

check = {x:False for x in capitals}
# to determine which capitals are already checked

guide = {"santiago":"chile","london":"united kingdom","la paz":"bolivia",
         "kingston":"jamaica","buenos aires":"argentina","san juan":"puerto rico",
         "san jose":"costa rica"}
# corrects capital asignation for countries that have cities with capital names


f = open("data/airports.csv","r",encoding="utf-8") # open airports database
from Grafo import Grafo

grafo = Grafo()

for line in f:

    data = line.split(",")
    country = data[3].strip('"').lower()
    city = data[2].lower()

    if city in capitals and not check[city] and line.split(",")[4] !="\\N":
        # take cities that are capitals we have not checked and that have IATA code
        str = f"{data[1]},{data[2]},{data[3]},{data[4]},{data[6]},{data[7]}"
        info = [x.strip('"') for x in str.split(",")]

        if city.strip('"') in list(guide.keys()): # if city is special case
            #name,city,country,code,lat,long

            if country==guide[city.strip('"')]: # add if we have right country
                grafo.addAirport(info)
                check[city] = True
        else:
            grafo.addAirport(info)
            check[city] = True
f.close() 

ls = [] #unused capitals
for k,i in check.items():
    if i is False:
        ls.append(k)


