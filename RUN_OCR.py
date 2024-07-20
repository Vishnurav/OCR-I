# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:23:20 2024

@author: parap
"""

import sys
import os
import tkinter as tk

# Add the directory containing ocr_app to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from ocr_app.gui import OCRApp
from ocr_app.ocr import OCRProcessor
from ocr_app.pdf import PDFCreator

if __name__ == "__main__":
    root = tk.Tk()
    ocr_processor = OCRProcessor()
    pdf_creator = PDFCreator()
    app = OCRApp(root, ocr_processor, pdf_creator)
    root.mainloop()
