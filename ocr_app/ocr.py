# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:22:07 2024

@author: parap
"""

from PIL import Image
import pytesseract
import os

# Set the TESSDATA_PREFIX environment variable to the correct path
os.environ['TESSDATA_PREFIX'] = r'D:\Programs\Anaconda\share\tessdata'

class OCRProcessor:
    def perform_ocr(self, image_path):
        image = Image.open(image_path)
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        return data
