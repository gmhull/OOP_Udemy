"""
Title: Web Photo Sharer
Description: This app will
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia, requests

class MainApp(App):
    """docstring for MainApp."""
    def build(self):
        return RootWidget()

class RootWidget(ScreenManager):
    """docstring for RootWidget."""
    pass

class FirstScreen(Screen):
    """docstring for FirstScreen."""
    def search_image(self):
        # Get the user input from the text input
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first img url
        page = wikipedia.page(query)
        image_link = page.images[0]
        # download the image
        req = requests.get(image_link)
        file_path = 'files/image.jpg'
        with open(file_path, 'wb') as file:
            file.write(req.content)
        # Set the image in the image widget
        self.manager.current_screen.ids.img.source = file_path

class SecondScreen(Screen):
    """docstring for SecondScreen."""


if __name__ == "__main__":
    Builder.load_file('frontend.kv')
    MainApp().run()
