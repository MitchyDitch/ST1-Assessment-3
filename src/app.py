import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import joblib
from PIL import Image, ImageTk


class MacroApp(tk.Tk):
    """Desktop GUI for macroinvertebrate image prediction."""

    def __init__(self, preprocessor, model_path: Path) -> None:
        super().__init__()
        self.title("Macroinvertebrate Image Analysis System")
        self.geometry("900x600")

        self.preprocessor = preprocessor
        self.model = joblib.load(model_path)
        self.selected_file = None

        self.image_label = tk.Label(self, text="No image selected")
        self.image_label.pack(pady=10)

        tk.Button(self, text="Select Image", command=self.select_image).pack(pady=5)

    def select_image(self) -> None:
        """Open a file dialog and preview the selected image."""

        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")],
        )
        if not file_path:
            messagebox.showwarning("No file selected", "Please select an image file.")
            return

        self.selected_file = file_path
        image = Image.open(file_path)
        image.thumbnail((350, 350))
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo, text="")
        self.image_label.image = photo
