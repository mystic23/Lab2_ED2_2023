from geopy.distance import distance
import requests 

def get_coords(name_city: str, key: str) -> tuple:
    '''
    Llama a la API para conocer las coordenadas geograficas de determinada ciudad

    Args:
        name_city (str) : [Nombre de la ciudad de la cual queremos saber las coordenadsa geograficas]
        key       (str) : [key personal para la validacion de la peticion a la API]

    Returns:
        tuple : Retorna una tupla con la latitud y longitud de la determinada ciudad que hayamos pasado por parametro
    '''
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": name_city,
        "key": key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if len(data["results"]) > 0:
            latitude = data["results"][0]["geometry"]["lat"]
            length = data["results"][0]["geometry"]["lng"]

        return (latitude, length)
    print(f"Ocurrio un error al hacer la solicitud HTTP: {response.text}")

def distance_between(name_one: str, name_two: str, key: str) -> float:
    '''
    Calcula la distancia en km entre dos ciudades

    Args:
        name_one (str) : [Nombre de la primera ciudad]
        name_two (str) : [Nombre de la segunda ciudad]

    Returns:
        float : Retorna el valor flotante de la distancia en km entre las dos ciudades
    '''
    city1_coords = get_coords(name_one, key)
    city2_coords = get_coords(name_two, key)
    return distance(city1_coords, city2_coords).km

# Ahí puse mi key en la pagina de la API que estoy usando
print('La distancia entre Bogotá y Washington es {} km'.format(distance_between('Bogotá', 'Washington', '4efc072c937e49bdbe3d00f2d10f4573')))