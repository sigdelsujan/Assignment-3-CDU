import tkinter as tk
from tkinter import filedialog, simpledialog
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
        img = self.processor.grayscale()
        self.gui.display_image(img)

    def edges(self):
        img = self.processor.edge_detect()
        self.gui.display_image(img)

    def blur(self, value):
        k = int(value)
        if k % 2 == 0:
            k += 1
        img = self.processor.apply_blur(k)
        self.gui.display_image(img)

    def brightness(self, value):
        img = self.processor.apply_brightness(int(value))
        self.gui.display_image(img)

    def contrast(self, value):
        img = self.processor.apply_contrast(float(value))
        self.gui.display_image(img)

    def rotate(self, angle):
        img = self.processor.rotate(angle)
        self.gui.display_image(img)

    def flip(self, mode):
        img = self.processor.flip(mode)
        self.gui.display_image(img)

    def resize_image(self):
        width = simpledialog.askinteger("Resize", "Enter new width:")
        height = simpledialog.askinteger("Resize", "Enter new height:")
        if width and height:
            img = self.processor.resize(width, height)
            self.gui.display_image(img)

    def undo(self):
        img = self.processor.reset()
        self.gui.display_image(img)

if __name__ == "__main__":
    root = tk.Tk()
    AppController(root)
    root.mainloop()
