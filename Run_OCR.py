# Copyright 2024 Vishnu Parappulakkal
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
