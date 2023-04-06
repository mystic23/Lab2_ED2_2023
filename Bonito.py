

import customtkinter
from tkintermapview import TkinterMapView
import sys
import tkinter
from drivercode1 import grafo
from processing import *
from processing import restartGraph


customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
  
    APP_NAME = "- CityScape Odyssey -"
    WIDTH = 1200
    HEIGHT = 700
    markers_dict = {}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(7, weight=0)

        # self.button_1 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Set Marker",
        #                                         command=self.set_marker_event)
        # self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)
        

        # self.button_2 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Clear Markers",
        #                                         command=self.clear_marker_event)
        # self.button_2.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)
        
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
        
        self.button_9 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Restart Airport",
                                                command=self.restart_airport)
        self.button_9.grid(pady=(20, 0), padx=(20, 20), row=3, column=0)
        

        self.map_label = customtkinter.CTkLabel(self.frame_left, text="Tile Server:", anchor="w")
        self.map_label.grid(row=4, column=0, padx=(20, 20), pady=(20, 0))
        
        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google normal", "Google satellite"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(row=5, column=0, padx=(20, 20), pady=(10, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=(20, 20), pady=(20, 0))
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=6 , column=0, padx=(20, 20), pady=(20, 0))

        # ============ frame_right ============

        # self.frame_right.grid_rowconfigure(1, weight=1)
        # self.frame_right.grid_rowconfigure(0, weight=0)
        # self.frame_right.grid_columnconfigure(0, weight=1)
        # self.frame_right.grid_columnconfigure(1, weight=0)
        # self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(width=1200, height=600, corner_radius=0)
        self.map_widget.grid(row=0, rowspan=1, column=1,  columnspan=4,sticky="nsew", padx=(30, 30), pady=(75, 30))
        

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(20, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)
        
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
                                                text="Min Rout",
                                                width=90,
                                                command=self.min_route)
        self.button_8.grid(row=0, column=4, sticky="w", padx=(5, 0), pady=12)
        
     
        

        # Set default values
        self.map_widget.set_address("Colombia")
        self.map_option_menu.set("OpenStreetMap")
        self.appearance_mode_optionemenu.set("Dark")
     
        self.marker_path = None
        self.search_in_progress = False
        
    ##conecta los puntos que coloque del mapa
    def connect_marker(self):
        print(self.marker_list)
        position_list = []

        for marker in self.marker_list:
            position_list.append(marker.position)

        if self.marker_path is not None:
            self.map_widget.delete(self.marker_path)

        if len(position_list) > 0:
            self.marker_path = self.map_widget.set_path(position_list)
   
    ##busca el punto especifico
    #pero lo que no sé es como vincularlo al csv       
    def search_event(self, event=None):
        country = self.entry.get()
        self.map_widget.set_address(grafo[country].name, marker=False)
        
    
    def search_event2(self, event=None):
        country = self.entry2.get()
        self.map_widget.set_address(grafo[country].name, marker=False)
        

    # def set_marker_event(self):
    #     current_text = self.entry.get() #aqui esta el texto
    #     self.name_cities.append(current_text)
        
    #     current_position = self.map_widget.get_position()
    #     self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()
            self.name_cities=[]

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
        llenar_grafo()
        for airport in grafo.vertices.values():
            x = self.map_widget.set_marker(float(airport.coords[0]),float(airport.coords[1]),text=airport.country)
            self.markers_dict.update({airport.country:x})
        # set a position marker (also with a custom color and command on click)
    
     
    def min_route(self):
        """
        Shows minium route between two 
        country airports
        """
        try:
            
            address = self.entry.get()
            destino = self.entry2.get()
            # get origin and destination
            dist,path = grafo.minDistance(address,destino)
            # do dijktra
            if path: # if a path was found
                # self.consola.config(text=f"Distance:{dist}km  Path:{path}")
                for i in range(len(path)-1):
                    a = path[i]
                    b = path[i+1]
                    x = grafo[a]
                    self.map_widget.set_path([x.coords,grafo[b].coords],color="green",width=10)
                    # draw path to destination
            else:
                # self.consola.config(text=f"No hay camino")
                print("No hay camino")
        except:
            # self.consola.config(text=
            print("Inserte en los dos campos") 
    
                     
    def delete_airport(self):
        """
        deletes an airport from
        map and graph
        """
        try:
            address = self.entry0.get()
            
            grafo.deleteAirport(address)
            self.markers_dict[address].delete()
            self.map_widget.delete_all_path()
        except:
            print("Escriba pais en mapa")
            
            

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.restart_airport()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
    