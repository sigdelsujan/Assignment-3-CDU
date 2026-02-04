import cv2

class ImageProcessor:
    def __init__(self):
        self.original = None
        self.image = None

    def load_image(self, path):
        self.original = cv2.imread(path)
        self.image = self.original.copy()
        return self.image

    def reset(self):
        self.image = self.original.copy()
        return self.image


    def apply_blur(self, ksize):
        temp = self.original.copy()
        if ksize > 1:
            temp = cv2.GaussianBlur(temp, (ksize, ksize), 0)
        self.image = temp
        return self.image

    def apply_brightness(self, value):
        temp = self.original.copy()
        temp = cv2.convertScaleAbs(temp, alpha=1, beta=value)
        self.image = temp
        return self.image

    def apply_contrast(self, value):
        temp = self.original.copy()
        temp = cv2.convertScaleAbs(temp, alpha=value, beta=0)
        self.image = temp
        return self.image


    def grayscale(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        self.original = self.image.copy()
        return self.image

    def edge_detect(self):
        edges = cv2.Canny(self.image, 100, 200)
        self.image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        self.original = self.image.copy()
        return self.image

    def rotate(self, angle):
        if angle == 90:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            self.image = cv2.rotate(self.image, cv2.ROTATE_180)
        elif angle == 270:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.original = self.image.copy()
        return self.image

    def flip(self, mode):
        self.image = cv2.flip(self.image, 1 if mode == "horizontal" else 0)
        self.original = self.image.copy()
        return self.image

    def resize(self, width, height):
        self.image = cv2.resize(self.image, (width, height))
        self.original = self.image.copy()
        return self.image
