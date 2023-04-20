from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from servermacc import TestServerAdd
from callservertest import *
import threading
import requests
import time 
from emailconf import send_email


class FunServer(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creamos los widgets de la pantalla
        self.label = Label(text="¡Esta es la pantalla de Test Server!", font_size=24, halign="center")
        self.status_button = Button(text="Inactivo", font_size=20, size_hint_y=None, height=50)
        self.status_button.bind(on_press=self.change_status)
        self.status = "inactivo"


        self.button_atras = Button(text="Volver", font_size=20, size_hint_y=None, height=50)
        self.button_atras.bind(on_press=self.switch_to_funserver)

        # Creamos una instancia de AsyncImage con la imagen del espiral
        self.spiral = Image(source="server_icon_197663.png")

        # Creamos un layout vertical para los widgets
        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)
        layout.add_widget(self.label)

        layout.add_widget(self.status_button)
        layout.add_widget(self.button_atras)

        layout.add_widget(self.spiral)

        # Agregamos el layout a la pantalla
        self.add_widget(layout)


    def switch_to_funserver(self, instance):
        screen_manager = self.manager
        self.status_button.text = "Inactivo"
        screen_manager.current = "next_screen"
        stop_thread_execution()



    def on_enter(self):
        # Buscamos el objeto TestServerAdd en la lista de pantallas de la aplicación
        for screen in self.manager.screens:
            if isinstance(screen, TestServerAdd):
                self.test_server_add = screen
                break

    def change_status(self, instance):

        stop_event.clear()

        # Cambiamos el estado y actualizamos el texto del botón
        if self.status == "inactivo":
            self.status = "activo"
            self.status_button.text = "Activo"
            self.label.text = "Probando Conexion con los Servidores"
            self.spiral.opacity = 1  # Ocultamos el espiral
            if self.test_server_add: 
                if self.status_button.text == "Activo":
                    t = threading.Thread(target=testServerCAll, args=(self.test_server_add.servers,))
                    t.start()


        else:
            self.status = "inactivo"
            self.status_button.text = "Inactivo"
            self.label.text = "Se ha detenido Conexion con los Servidores"
            self.spiral.opacity = 0  # Mostramos el espiral
            stop_thread_execution()

#####################################################################################



stop_event = threading.Event()

def testServerCAll(getlist):
        while True:
            for url in getlist:
                start_time = time.time()
            
                try:
                    response = requests.head(url, verify=False, timeout=10)
                    if response.status_code == 200:
                        pass
                    else:
                        end_time = time.time()
                        result = f"Fallo de solicitud a {url}. Código de estado: {response.status_code}\nLa solicitud tardó: {end_time - start_time} segundos en completarse\n\n"
                        send_email(result)
                except requests.exceptions.Timeout:
                    result = f"Timeout de conexión con {url}\n\n"
                    send_email(result)
                except requests.exceptions.RequestException as e:
                    result = f"Error de conexión con {url}: {e}\n\n"
                
                    send_email(result)

            if stop_event.is_set():
                break

def stop_thread_execution():
    stop_event.set()
    
