"""
Title: Web Photo Sharer
Description: This app will show the live video feed of the computer webcam.  The
user can capture an image of the live feed and generate a shareable link so that
others can see the image.  You are able to copy the link or open it in browser.
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from filesharer import FileSharer
import time, os, webbrowser

class MainApp(App):
    """docstring for MainApp."""
    def build(self):
        return RootWidget()

class RootWidget(ScreenManager):
    """docstring for RootWidget."""
    pass

class CameraScreen(Screen):
    """docstring for FirstScreen."""
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filename = 'files/%s.png' % current_time
        self.ids.camera.export_to_png(self.filename)

        self.manager.current = 'image_screen'

        self.manager.current_screen.ids.img.source = self.filename

class ImageScreen(Screen):
    link_message = "Create a link first"
    def create_link(self):
        """Create a link so that the user can share the image with others over
        the internet"""
        file_path = App.get_running_app().root.ids.camera_screen.filename
        filesharer = FileSharer(filepath = file_path)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = link_message


if __name__ == "__main__":
    Builder.load_file('frontend.kv')
    MainApp().run()
