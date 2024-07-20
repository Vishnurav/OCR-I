import tkinter as tk
from tkinter import filedialog, messagebox

class OCRApp:
    def __init__(self, root, ocr_processor, pdf_creator):
        self.root = root
        self.root.title("OCR to PDF Converter")
        self.ocr_processor = ocr_processor
        self.pdf_creator = pdf_creator

        self.btn_open = tk.Button(root, text="Open Image", command=self.open_image)
        self.btn_open.pack(pady=10)

        self.btn_save = tk.Button(root, text="Save PDF", command=self.save_pdf, state=tk.DISABLED)
        self.btn_save.pack(pady=10)

        self.image_path = None

    def open_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            messagebox.showinfo("Image Selected", f"Image selected: {self.image_path}")
            self.btn_save.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("No Image Selected", "Please select an image file.")

    def save_pdf(self):
        if not self.image_path:
            messagebox.showwarning("No Image Selected", "Please select an image file.")
            return

        try:
            data = self.ocr_processor.perform_ocr(self.image_path)
            self.pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if not self.pdf_path:
                return

            self.pdf_creator.create_pdf(self.image_path, data, self.pdf_path)
            messagebox.showinfo("Process Complete", f"PDF file saved at: {self.pdf_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
