# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:22:34 2024

@author: parap
"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PIL import Image

class PDFCreator:
    def create_pdf(self, image_path, data, pdf_path):
        image = Image.open(image_path)
        image_width, image_height = image.size

        c = canvas.Canvas(pdf_path, pagesize=(image_width, image_height))
        pdfmetrics.registerFont(TTFont('Arial-Regular', 'arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))

        c.drawImage(image_path, 0, 0, width=image_width, height=image_height)

        for i in range(len(data['text'])):
            text = data['text'][i]
            if text.strip():
                x = data['left'][i]
                y = image_height - (data['top'][i] + data['height'][i])
                font_size = data['height'][i]
                font_style = 'Arial-Regular'
                if 'bold' in text.lower():
                    font_style = 'Arial-Bold'

                c.setFont(font_style, font_size if font_size > 0 else 12)
                rotation = data['rotate'][i] if 'rotate' in data and data['rotate'][i] else 0
                c.saveState()
                c.translate(x + font_size / 2, y + font_size / 2)
                c.rotate(rotation)
                c.translate(-x - font_size / 2, -y - font_size / 2)
                c.drawString(x, y, text)
                c.restoreState()

        c.save()
