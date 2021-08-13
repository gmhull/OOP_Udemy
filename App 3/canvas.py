import numpy as np
from PIL import Image

class Canvas(object):
    """Create the main canvas to paint the geometry onto."""

    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

        # Initialize the canvas image
        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def create(self, filename):
        img = Image.fromarray(self.data, 'RGB')
        img.save('files/'+filename)
