import tkinter
import tkintermapview
from drivercode1 import grafo

# first version of GUI

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1200}x{700}+{250}+{50}")
root_tk.iconbitmap("img/icon.ico")
root_tk.title("CityScape Odyssey.py")
root_tk.resizable(False,False)

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1400, height=600, corner_radius=20)


# create input boxes
input_frame = tkinter.Frame(root_tk)
input_frame.pack(fill="x")

input_label = tkinter.Label(input_frame, text="ingrese país:")
input_label.pack(side="left")

address_box = tkinter.Entry(input_frame, width=30)
address_box.pack(side="left", padx=5)

input_label2 = tkinter.Label(input_frame, text="nivel de zoom:")
input_label2.pack(side="left", padx=10)

zoom_box = tkinter.Entry(input_frame, width=10)
zoom_box.pack(side="left")

def on_button_click():
    # get address and zoom level from input boxes
    try:
        address = address_box.get()
        zoom = int(zoom_box.get())
        
        # set the address and zoom level on the map widget
        map_widget.set_address(address, marker=False)
        map_widget.set_zoom(zoom)
    except:
        consola.config(text="Ingrese sitio y zoom")

def delete_airport():
    """
    deletes an airport from
    map and graph
    """
    try:
        address = address_box.get()
        grafo.deleteAirport(address)
        markers_dict[address].delete()
        map_widget.delete_all_path()
    except:
        consola.config(text="Escriba pais en mapa")

# create button
button = tkinter.Button(input_frame, text="Buscar sitio", command=on_button_click)
button.pack(side="left", padx=10)

def show_routes():
    """
    Shows all routes from airport
    country in address
    """
    try:
        map_widget.delete_all_path()
        address = address_box.get()
        airport = grafo[address]
        for ady in airport.routes.keys():
            path = map_widget.set_path([airport.coords,grafo[ady].coords],color="blue",width=4)
    except:
        consola.config(text="introduzca pais con marcador")

routes = tkinter.Button(input_frame, text="Mostrar rutas", command=show_routes)
routes.pack(side="left", padx=15)

delete = tkinter.Button(input_frame, text="Borrar", command=delete_airport)
delete.pack(side="left", padx=15)

destino_box = tkinter.Entry(input_frame, width=10)
destino_box.pack(side="left")

def min_route():
        """
        Shows minium route between two 
        country airports
        """
        map_widget.delete_all_path()
        try:
            address = address_box.get()
            destino = destino_box.get()
            # get origin and destination
            dist,path = grafo.minDistance(address,destino)
            # do dijktra
            if path: # if a path was found
                consola.config(text=f"Distance:{dist}km  Path:{path}")
                for i in range(len(path)-1):
                    a = path[i]
                    b = path[i+1]
                    x = grafo[a]
                    map_widget.set_path([x.coords,grafo[b].coords],color="green",width=10)
                    # draw path to destination
            else:
                consola.config(text=f"No hay camino")
        except:
            consola.config(text="Inserte en los dos campos")


min = tkinter.Button(input_frame, text="ruta minima a:", command=min_route)
min.pack(side="left", padx=15)

#set initial view worldwide
map_widget.set_zoom(2)

def add_marker_event(coords):
    print("Add marker:", coords)
    address = address_box.get()
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")
    

map_widget.add_right_click_menu_command(label="Añadir Marcador",
                                        command=add_marker_event,
                                        pass_coords=True)

consola = tkinter.Label(root_tk, text="Bienvenido a CityScape Odyssey",font=("Helvetica",20))
consola.pack(side="bottom")

markers_dict = {}
for airport in grafo.vertices.values():
    x = map_widget.set_marker(float(airport.coords[0]),float(airport.coords[1]),text=airport.country)
    markers_dict.update({airport.country:x})
# set a position marker (also with a custom color and command on click)



# show the map and the line
map_widget.pack(fill="both", expand=True)
root_tk.mainloop()




