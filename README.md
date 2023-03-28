# Lab2_ED2_2023
## Integrantes :books::
+ David Hernandez
+ María Solá
+ Jesus Zuluaga

## Diagrama de clases
![Example image](example.png "Example title")

## Algoritmos anteriores de procesamiento
Algunos algortimos usados para facilitar el acceso a los datos y su comprensión no son necesarios ejecutar para usar el proyecto, se muestran por su relevancia en crear el grafo final usado.
### **Conteo de paises repetidos**
```python
countries = []
for code,data in grafo.vertices.items():
    countries.append(data.country)
# store all codes and countries from graph

print([item for item, count in collections.Counter(countries).items() if count > 1])
```
### **Registro de aeropuertos sin rutas**
```python
empty = []
for code,airport in grafo.vertices.items():
    if len(airport.routes) ==0:
        empty.append([airport.country,airport.city,code,len(airport.routes)])
# recorremos grafo guardando información de aeropuertos sin adyacentes

debug = open("data/empty_routes.txt","w",encoding="utf-8")
for x in empty:
    debug.write(f"{str(x)}\n")
debug.close()
# escribimos en archivo la informacipon de la lista
```

### **Obtención de rutas adicionales por Airlabs API**
```python
import requests

params = {
  'api_key': 'KEY',
  'dep_iata': 'IATA_CODE'
}
method = 'ping'
api_base = 'http://airlabs.co/api/v9/routes?'
# usando rutas de parametro de búsqueda
api_result = requests.get(api_base+method, params)
api_response = api_result.json()["response"]
# se hace el llamado a la API y accede a la respuesta

with open("country_routes.txt","w") as f:
    for x in api_response:
        y = x["arr_iata"]
        f.write(f"{y}\n")
# se guarda el codigo del aeropuerto de llegada en un archivo para el país
```

## **Referencias**
M. ChatGPT, "How to count repeated elements in dictionary," [Online]. Available: https://stackoverflow.com/questions/9432393/how-to-count-repeated-elements-in-the-dictionary-in-python.

AirLabs, "AirLabs Routes API documentation," [Online]. Available: https://airlabs.co/docs/routes.