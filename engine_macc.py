from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from servermacc import TestServerAdd
from testserver import FunServer


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creamos los widgets de la pantalla de bienvenida
        welcome_label = Label(text="Bienvenido al TEST MACC SERVER", font_size=24, halign="center")
        start_button = Button(text="Comenzar", font_size=20, size_hint_y=None, height=50)
        start_button.bind(on_press=self.change_screen)

        # Creamos un layout vertical para los widgets
        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)
        layout.add_widget(welcome_label)
        layout.add_widget(start_button)

        # Agregamos el layout a la pantalla de bienvenida
        self.add_widget(layout)

    def change_screen(self, instance):
        # Cambiamos a la pantalla de la siguiente ventana
        self.manager.current = "next_screen"


class TestMaccServerApp(App):
    def build(self):
        # Creamos el administrador de pantallas y agregamos las pantallas
        screen_manager = ScreenManager()
        screen_manager.add_widget(WelcomeScreen(name="welcome_screen"))
        screen_manager.add_widget(TestServerAdd(name="next_screen"))
        screen_manager.add_widget(FunServer(name="funserver"))
        return screen_manager

if __name__ == '__main__':
    TestMaccServerApp().run()


