import tkinter as tk
from tkinter import filedialog
import cv2
from image_processor import ImageProcessor
from gui import ImageEditorGUI

class AppController:
    def __init__(self, root):
        self.processor = ImageProcessor()
        self.gui = ImageEditorGUI(root, self)
        self.filepath = ""

    def open_image(self):
        self.filepath = filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.png *.bmp")]
        )
        if self.filepath:
            img = self.processor.load_image(self.filepath)
            self.gui.display_image(img, self.filepath)

    def save_image(self):
        if self.filepath:
            cv2.imwrite(self.filepath, self.processor.image)

    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            cv2.imwrite(path, self.processor.image)

    def grayscale(self):
        self.gui.display_image(self.processor.grayscale())

    def blur(self, value):
        k = int(value)
        if k % 2 == 0:
            k += 1
        self.gui.display_image(self.processor.blur(k))

    def edges(self):
        self.gui.display_image(self.processor.edge_detect())

    def brightness(self, value):
        self.gui.display_image(self.processor.adjust_brightness(int(value)))

    def rotate(self, angle):
        self.gui.display_image(self.processor.rotate(angle))

    def flip(self, mode):
        self.gui.display_image(self.processor.flip(mode))

    def undo(self):
        self.gui.display_image(self.processor.reset())

    def redo(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    AppController(root)
    root.mainloop()
