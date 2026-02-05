import cv2

class ImageProcessor:
    def __init__(self):
        self.original = None   # original loaded image
        self.image = None      # current image that we are using
        self.undo_stack = []   # stack to savee all the undo states
        self.redo_stack = []

    def load_image(self, path):
        self.original = cv2.imread(path)
        self.image = self.original.copy()
        self.undo_stack = []
        self.redo_stack = []
        return self.image

    def save_state(self):
        self.undo_stack.append(self.image.copy())
        self.redo_stack = []  

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.image.copy())  # save current for redo
            self.image = self.undo_stack.pop()
        return self.image

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.image.copy())  # save current for undo
            self.image = self.redo_stack.pop()
        return self.image

    def apply_blur(self, ksize):
        self.save_state()  # saves the state that it is currently in before applying
        temp = self.image.copy() 
        if ksize > 1:
            temp = cv2.GaussianBlur(temp, (ksize, ksize), 0)
        self.image = temp
        return self.image

    def apply_brightness(self, value):
        self.save_state()  
        self.image = cv2.convertScaleAbs(self.image, alpha=1, beta=value)
        return self.image

    def apply_contrast(self, value):
        self.save_state()
        self.image = cv2.convertScaleAbs(self.image, alpha=value, beta=0)
        return self.image

    def grayscale(self):
        self.save_state()
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        return self.image

    def edge_detect(self):
        self.save_state()
        edges = cv2.Canny(self.image, 100, 200)
        self.image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return self.image

    def rotate(self, angle):
        self.save_state()
        if angle == 90:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            self.image = cv2.rotate(self.image, cv2.ROTATE_180)
        elif angle == 270:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return self.image

    def flip(self, mode):
        self.save_state() 
        self.image = cv2.flip(self.image, 1 if mode == "horizontal" else 0)
        return self.image

    def resize(self, width, height):
        self.save_state()
        self.image = cv2.resize(self.image, (width, height))
        return self.image

