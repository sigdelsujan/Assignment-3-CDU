import cv2
import numpy as np

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.original = None

    def load_image(self, path):
        self.image = cv2.imread(path)
        self.original = self.image.copy()
        return self.image

    def reset(self):
        self.image = self.original.copy()
        return self.image

    def grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
        return self.image

    def blur(self, ksize):
        self.image = cv2.GaussianBlur(self.image, (ksize, ksize), 0)
        return self.image

    def edge_detect(self):
        edges = cv2.Canny(self.image, 100, 200)
        self.image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return self.image

    def adjust_brightness(self, value):
        self.image = cv2.convertScaleAbs(self.image, alpha=1, beta=value)
        return self.image

    def adjust_contrast(self, value):
        self.image = cv2.convertScaleAbs(self.image, alpha=value, beta=0)
        return self.image

    def rotate(self, angle):
        if angle == 90:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            self.image = cv2.rotate(self.image, cv2.ROTATE_180)
        elif angle == 270:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return self.image

    def flip(self, mode):
        self.image = cv2.flip(self.image, 1 if mode == "horizontal" else 0)
        return self.image

    def resize(self, width, height):
        self.image = cv2.resize(self.image, (width, height))
        return self.image
