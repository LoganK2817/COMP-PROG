import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import barcode
from barcode.writer import ImageWriter

def generate_barcode():
    code = entry_code.get().strip()
    filename = entry_filename.get().strip()

    if not code:
        messagebox.showerror("Error", "Please enter a code.")
        return
    if not filename:
        messagebox.showerror("Error", "Please enter a filename.")
        return

    # Remove extension if user adds '.png'
    if filename.lower().endswith('.png'):
        filename = filename[:-4]

    try:
        code39 = barcode.get_barcode_class('code39')
        barcode_obj = code39(code, writer=ImageWriter(), add_checksum=True)
        full_filename = barcode_obj.save(filename)

        load_and_display_image(full_filename)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_and_display_image(path):
    try:
        img = Image.open(path)
        img = img.resize((300, 100), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        barcode_label.configure(image=img_tk)
        barcode_label.image = img_tk  # keep reference
    except Exception as e:
        messagebox.showerror("Image Error", f"Could not load image: {e}")

# GUI setup
root = tk.Tk()
root.title("Code39 Barcode Generator")
root.geometry("400x320")

label_code = tk.Label(root, text="Code39 Input (A–Z, 0–9, - . space):")
label_code.pack(pady=5)
entry_code = tk.Entry(root)
entry_code.pack(pady=5)

label_filename = tk.Label(root, text="Output filename (no extension):")
label_filename.pack(pady=5)
entry_filename = tk.Entry(root)
entry_filename.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Barcode", command=generate_barcode)
generate_btn.pack(pady=10)

barcode_label = tk.Label(root)
barcode_label.pack(pady=10)

root.mainloop()
