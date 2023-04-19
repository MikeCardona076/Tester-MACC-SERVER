from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


######################################################


class TestServerAdd(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creamos los widgets de la siguiente pantalla
        label = Label(text="Agrega o elimina servidores: Copia tal cual la direccion de tu Servidor Https o Https", font_size=20, halign="center")
        self.server_input = TextInput(multiline=False, font_size=20, size_hint_y=None, height=50)
        add_button = Button(text="Agregar servidor", font_size=20, size_hint_y=None, height=50)
        
        serverloopbutton = Button(text="Test Server", font_size=20, size_hint_y=None, height=50)
        serverloopbutton.bind(on_press=self.switch_to_funserver)
        
        add_button.bind(on_press=self.add_server)
        self.servers_layout = BoxLayout(orientation="vertical", spacing=10)
        self.servers_list = ScrollView(size_hint=(1, None), height=300, do_scroll_x=False)
        self.servers_list.add_widget(self.servers_layout)


        
        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)
        layout.add_widget(label)
        layout.add_widget(self.server_input)
        layout.add_widget(add_button)
        layout.add_widget(serverloopbutton)
        layout.add_widget(self.servers_list)

        # Agregamos el layout a la siguiente pantalla
        self.add_widget(layout)

        # Creamos una lista vacía para almacenar los servidores agregados
        self.servers = []


    def switch_to_funserver(self, instance):
        screen_manager = self.manager
        screen_manager.current = "funserver"


    def add_server(self, instance):
        # Verificamos si ya hay 5 servidores en la lista
        if len(self.servers) >= 5:
            self.servers_list.text = "No se pueden agregar más servidores."
            return
        #Verificamos si esta vacio
        if self.server_input.text == "":
            self.servers_list.text = "No se pueden agregar campos vacios"
            return

        # Agregamos el servidor ingresado a la lista y actualizamos el widget de la lista
        server = self.server_input.text
        self.servers.append(server)
        self.servers_layout.add_widget(self.create_server_widget(server))
        self.server_input.text = ""

    def create_server_widget(self, server):
        # Creamos un layout horizontal para el servidor y el botón de eliminación
        server_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)

        # Creamos un label para el servidor
        server_label = Label(text=server, font_size=20)

        # Creamos un botón para eliminar el servidor
        remove_button = Button(text="Eliminar", font_size=20, size_hint_x=None, width=100)
        remove_button.bind(on_press=lambda instance: self.remove_server(server_layout, server))

        # Agregamos los widgets al layout del servidor
        server_layout.add_widget(server_label)
        server_layout.add_widget(remove_button)

        return server_layout

    def remove_server(self, server_layout, server):
        # Eliminamos el servidor de la lista y del layout de servidores
        self.servers.remove(server)
        self.servers_layout.remove_widget(server_layout)

