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
    def get_image_link(self):
        # Get the user input from the text input
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first img url
        page = wikipedia.page(query)
        image_link = page.images[0]

        return image_link

    def download_image(self):
        # download the image
        req = requests.get(self.get_image_link())
        image_path = 'files/image.jpg'
        with open(image_path, 'wb') as file:
            file.write(req.content)

        return image_path

    def set_image(self):
        # Set the image in the image widget
        self.manager.current_screen.ids.img.source = self.download_image()

class SecondScreen(Screen):
    """docstring for SecondScreen."""


if __name__ == "__main__":
    Builder.load_file('frontend.kv')
    MainApp().run()
