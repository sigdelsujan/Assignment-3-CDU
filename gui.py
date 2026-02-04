import tkinter as tk
from PIL import Image, ImageTk
import cv2

class ImageEditorGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Image Editor – Group Assignment 3")
        self.root.geometry("1000x600")

        self.create_menu()
        self.create_layout()

        self.status_text = tk.StringVar()
        self.status_bar = tk.Label(root, textvariable=self.status_text,
                                   relief=tk.SUNKEN, anchor="w")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_menu(self):
        menu = tk.Menu(self.root)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.controller.open_image)
        file_menu.add_command(label="Save", command=self.controller.save_image)
        file_menu.add_command(label="Save As", command=self.controller.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.controller.undo)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menu)

    def create_layout(self):
        self.canvas = tk.Label(self.root)
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        panel = tk.Frame(self.root)
        panel.pack(side=tk.RIGHT, fill=tk.Y, padx=15)

        tk.Label(panel, text="Basic Effects", font=("Arial", 10, "bold")).pack(pady=5)
        tk.Button(panel, text="Grayscale",
                  command=self.controller.grayscale).pack(fill=tk.X)
        tk.Button(panel, text="Edge Detection",
                  command=self.controller.edges).pack(fill=tk.X)

        tk.Label(panel, text="Adjustments", font=("Arial", 10, "bold")).pack(pady=10)

        tk.Label(panel, text="Blur").pack()
        self.blur_slider = tk.Scale(panel, from_=1, to=21,
                                    orient=tk.HORIZONTAL,
                                    command=self.controller.blur)
        self.blur_slider.pack(fill=tk.X)

        tk.Label(panel, text="Brightness").pack()
        self.brightness_slider = tk.Scale(panel, from_=-100, to=100,
                                          orient=tk.HORIZONTAL,
                                          command=self.controller.brightness)
        self.brightness_slider.pack(fill=tk.X)

        tk.Label(panel, text="Contrast").pack()
        self.contrast_slider = tk.Scale(panel, from_=0.5, to=3.0,
                                        resolution=0.1,
                                        orient=tk.HORIZONTAL,
                                        command=self.controller.contrast)
        self.contrast_slider.pack(fill=tk.X)

        tk.Label(panel, text="Transform", font=("Arial", 10, "bold")).pack(pady=10)

        tk.Button(panel, text="Rotate 90°",
                  command=lambda: self.controller.rotate(90)).pack(fill=tk.X)
        tk.Button(panel, text="Rotate 180°",
                  command=lambda: self.controller.rotate(180)).pack(fill=tk.X)
        tk.Button(panel, text="Flip Horizontal",
                  command=lambda: self.controller.flip("horizontal")).pack(fill=tk.X)
        tk.Button(panel, text="Resize",
                  command=self.controller.resize_image).pack(fill=tk.X)

    def display_image(self, img, filename=""):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        self.canvas.config(image=img_tk)
        self.canvas.image = img_tk

        h, w, _ = img.shape
        self.status_text.set(f"{filename} | {w} x {h}")
