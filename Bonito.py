import customtkinter
from tkintermapview import TkinterMapView
from drivercode1 import grafo

customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
  
    APP_NAME = "- CityScape Odyssey -"
    WIDTH = 1500
    HEIGHT = 700
    # dimensions
    markers_dict = {}
    # allows access to markers added related to a country

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # sets grid dimensions to space
        # each grid sets a sistem of coordinates in row/column for easier placements

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(8, weight=0)

        
        self.entry0 = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Delete airport")
        self.entry0.grid(row=0, column=0,sticky="nsw", padx=(16, 0), pady=(20, 0))
        
        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Delete",
                                                command=self.delete_airport)
        self.button_3.grid(pady=(5, 0), padx=(20, 20), row=1, column=0)
        
        
        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Show Routes",
                                                command=self.show_routes)
        self.button_4.grid(pady=(20, 0), padx=(20, 20), row=2, column=0)
        
        self.button_10 = customtkinter.CTkButton(master=self.frame_left,
                                                text=" BFS ",
                                                command=self.bfs_airport)
        self.button_10.grid(pady=(20, 0), padx=(20, 20), row=4, column=0)
        self.button_11 = customtkinter.CTkButton(master=self.frame_left,
                                                text=" DFS ",
                                                command=self.dfs_airport)
        self.button_11.grid(pady=(20, 0), padx=(20, 20), row=5, column=0)
        

        self.map_label = customtkinter.CTkLabel(self.frame_left, text="Tile Server:", anchor="w")
        self.map_label.grid(row=9, column=0, padx=(20, 20), pady=(20, 0))
        
        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=10, column=0, padx=(20, 20), pady=(10, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=11, column=0, padx=(20, 20), pady=(20, 0))
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=12 , column=0, padx=(20, 20), pady=(20, 0))
        
        self.add = customtkinter.CTkButton(master=self.frame_left,
                                                text=" Add Airport ",
                                                command=self.add_airport)
        self.add.grid(pady=(20, 0), padx=(20, 20), row=6, column=0)


        self.newcoords = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Enter coords")
        self.newcoords.grid(row=7, column=0,sticky="nsw", padx=(16, 0), pady=(20, 0))

        self.namecode = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Enter name,code,city")
        self.namecode.grid(row=8, column=0,sticky="nsw", padx=(16, 0), pady=(20, 0))

        self.map_widget = TkinterMapView(width=1200, height=600, corner_radius=0)
        self.map_widget.grid(row=0, rowspan=1, column=1,  columnspan=4,sticky="nsew", padx=(30, 30), pady=(75, 30))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type origin/new country")
        self.entry.grid(row=0, column=0, sticky="we", padx=(20, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)
        # returns allows to use enter to trigger event

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(5, 0), pady=12)



        self.entry2 = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type destination")
        self.entry2.grid(row=0, column=2, sticky="we", padx=(20, 0), pady=12)
        self.entry2.bind("<Return>", self.search_event2)
        
        self.button_6 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event2)
        self.button_6.grid(row=0, column=3, sticky="w", padx=(5, 0), pady=12)


        self.button_8 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Min Route",
                                                width=90,
                                                command=self.min_route)
        self.button_8.grid(row=0, column=4, sticky="w", padx=(5, 0), pady=12)



        self.button_12 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Add route",
                                                width=90,
                                                command=self.add_route)
        self.button_12.grid(row=0, column=5, sticky="w", padx=(5, 0), pady=12)
        
        self.consola = customtkinter.CTkLabel(self.frame_right, text="Bienvenido a CityScape Odyssey", width=20, height=5)
        self.consola.grid(row=0, column=6, padx=(5, 0), pady=12 )
        # Consola is main label for events and error statements to user
    
        # Set default values
        self.map_widget.set_address("Colombia")
        self.map_option_menu.set("OpenStreetMap")
        self.appearance_mode_optionemenu.set("Dark")
     
        self.marker_path = None
        self.search_marker = None
        self.search_in_progress = False
        
    ##conecta los puntos que coloque del mapa
    def add_airport(self,event=None):
        """
        Adds to graph a new aiport
        in a new country
        """
        try:
            country = self.entry.get()
            coords = self.newcoords.get()
            lat = coords.split(" ")[0]
            long = coords.split(" ")[1]
            name_code = self.namecode.get()
            name = name_code.split(",")[0]
            code = name_code.split(",")[1]
            city = name_code.split(",")[2]

            # get data from boxes and do necessary splits
            try:
                print(grafo[country].coords)
                self.consola.configure(text="ya está el pais") 
                # if found in graph cannot add country
            except:
                grafo.addAirport([name,city,country,code,lat,long])
                self.consola.configure(text="se ha añadido un aeropuerto") 
                # else add airport and marker

                x = self.map_widget.set_marker(float(lat),float(long),text=country)
                self.markers_dict.update({country:x})
    
        except:
            self.consola.configure(text="Faltan datos")  

    def dfs_airport(self):
        """
        gets start point and saves 
        dfs path
        """
        try:
            start = self.entry.get()
            self.vertices = grafo.dfs(start)
            self.show_dfs()
        except:
            self.consola.configure(text="Ingrese pais de inicio")
    def show_dfs(self):
        """
        shows with delay each vertix in dfs
        """
        if len(self.vertices)!=0:
            current_word = self.vertices.pop(0) # get first 
            self.consola.configure(text=current_word) # show
            self.after(750, self.show_dfs) # repeat after delay

    def bfs_airport(self):
        """
        gets start point and saves BFS
        """
        try:
            start = self.entry.get()
            self.vertices = grafo.bfs(start)
            self.show_bfs()
        except:
            self.consola.configure(text="Ingrese pais de inicio")

    def show_bfs(self):
        """
        shows with delay each vertix in bfs
        """
        if len(self.vertices)!=0:
            current_word = self.vertices.pop(0)
            self.consola.configure(text=current_word)
            self.after(750, self.show_dfs)

    def add_route(self):
        try:
            a = self.entry.get()
            b = self.entry2.get()

            grafo.addRoute(a,b)
            self.consola.configure(text=f"ruta creada de distancia {grafo[a].routes[b]} ")
            self.show_routes()
        except:
            self.consola.configure(text="Error en paises")
    """ def set_marker_event(self):
        
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1])) """
          
    def search_event(self, event=None):
        """
        Allows map to move into position
        of searched country
        """
        try:
            country = self.entry.get()
            # get country name
            x = grafo[country].coords[0]
            y = grafo[country].coords[1]
            # get coords from graph
            address = f"{x} {y}"
            self.map_widget.set_address(address, marker=False)
            #set address of map to the coords
            self.consola.configure(text=f"{grafo[country].name} ({grafo[country].code})")
            # show name and code
        except:
            self.consola.configure(text="País no valido/espacio vacío")
    
    def search_event2(self, event=None):
        """
        as search_event but for another entry
        """
        try:
            country = self.entry2.get()
            x = grafo[country].coords[0]
            y = grafo[country].coords[1]
            address = f"{x} {y}"
            self.map_widget.set_address(address, marker=False)
            self.consola.configure(text=f"{grafo[country].name} {grafo[country].code}")
        except:
            self.consola.configure(text="País no valido/espacio vacío")

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def show_routes(self):
        """
        Shows all routes from airport
        country in address
        """
        self.map_widget.delete_all_path()
        address =self.entry.get()
        airport = grafo[address]
        for ady in airport.routes.keys():
            path = self.map_widget.set_path([airport.coords,grafo[ady].coords],color="blue",width=4)
      
    def restart_airport(self):
        pass
        # restartGraph(grafo)
        # self.start()
    
     
    def min_route(self):
        """
        Shows minium route between two 
        country airports
        """
        self.map_widget.delete_all_path()
        try:
            
            address = self.entry.get()
            destino = self.entry2.get()
            # get origin and destination
            dist,path = grafo.minDistance(address,destino)
            # do dijktra
            if path: # if a path was found
                self.consola.configure(text=f"Distance:{dist}km  Path:{path}")
                for i in range(len(path)-1):
                    a = path[i]
                    b = path[i+1]
                    x = grafo[a]
                    self.map_widget.set_path([x.coords,grafo[b].coords],color="green",width=10)
                    # draw path to destination
            else:
                self.consola.configure(text=f"No hay camino")
        except:
            self.consola.configure(text="Inserte en los dos campos") 
    
                     
    def delete_airport(self):
        """
        deletes an airport from
        map and graph
        """
        try:
            address = self.entry0.get() # get string from entry box
            grafo.deleteAirport(address) # calls graph method
            self.markers_dict[address].delete() # deletes from record
            self.map_widget.delete_all_path() # deletes paths shown
        except:
            self.consola.configure(text="Escriba país en mapa") 
            
            

    def change_map(self, new_map: str):
        """
        Changes how map is shown 
        uses standard methods of
        tkintermapview
        """
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def on_closing(self, event=0):
        """
        event of closing the app
        """
        self.destroy()

    def start(self):
        """
        adds markers for all airports
        in graph
        """
        for airport in grafo.vertices.values():
            x = self.map_widget.set_marker(float(airport.coords[0]),float(airport.coords[1]),text=airport.country)
            self.markers_dict.update({airport.country:x})
        # set a position marker and add to dict
        self.mainloop()
        # continuously happens

if __name__ == "__main__":
    app = App()
    app.start()