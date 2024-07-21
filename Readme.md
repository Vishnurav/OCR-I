# OCR to PDF Converter

![OCR to PDF Converter](https://github.com/Vishnurav/OCR-I/blob/main/Supportfiles/OCR%20ABSTRACT.jpg?raw=true)

## Overview

This project provides a Python application to convert images with text to searchable PDFs using Optical Character Recognition (OCR) technology. It is designed to enhance the efficiency of recreating scientific figures while ensuring compliance with publication standards.

## Author

- **Name:** Vishnu Parappulakkal
- **Website:** [vishnu.framer.media](https://vishnu.framer.media)

## Features

- **High Accuracy**: Uses advanced OCR models like pytesseract for precise text extraction.
- **Confidentiality**: Handles sensitive publication-related information with a focus on data privacy.
- **Offline Capability**: Operates locally without an internet connection, making it suitable for secure environments.
- **No Manual Font Handling**: Automatically processes text within images, eliminating the need for manual font adjustments.
- **PDF Generation**: Converts images and extracted text into well-formatted PDFs.
- **User-Friendly Interface**: Simple GUI for easy image selection and PDF saving.
- **Custom Font Handling**: Supports True Type fonts to replicate text styles accurately.
- **Time-Saving**: Reduces manual effort and accelerates the publication process.

## Installation

To run this application, ensure you have the following:

- Python 3.x
- Required Python packages (listed in `requirements.txt`)
- TESSDATA_PREFIX environment variable set to the correct path (refer to `ocr.py`)

## Usage
![Sample Image](https://github.com/Vishnurav/OCR-I/blob/main/Supportfiles/Sample%20Image.jpg?raw=true)

1. **Open the Application**: Launch the GUI.
2. **Open Image**: Click "Open Image" to select an image file (.png, .jpg, .jpeg).
3. **Save PDF**: Click "Save PDF" to convert the image to a searchable PDF.

## Processing Steps
![OCR to PDF Converter](https://github.com/Vishnurav/OCR-I/blob/main/Supportfiles/OCR.png?raw=true)

1. **Opening the Image**: Select an image file using the file dialog.
2. **Performing OCR**:
   - Extracts text and layout from the image.
   - Positions and formats the text based on OCR data.
3. **Saving the PDF**: The processed image and text are saved as a PDF.
![OCR to PDF Converter](https://github.com/Vishnurav/OCR-I/blob/main/Supportfiles/Pdf_file.png?raw=true)

## Why PDF?

PDF format is chosen for its compatibility and ease of use. Although EPS files would allow editable content, PDFs are more widely supported and interactive.

## Limitations

- **Multiple Text Boxes**: OCR may create multiple text boxes for single paragraphs, complicating editing.
- **Font Size Variation**: Inconsistent font sizes may occur.
- **Undetected Low-Resolution Text**: Poor quality images may result in inaccurate text detection.

## Suggested Solutions

- **Manual Adjustments**: Copy-paste text into a new layer in an editor for better alignment and formatting.
- **Image Upscaling**: Upscale images before processing for improved accuracy.
- **Image Segmentation**: Segment images to enhance text detection.

## Key Takeaways

- **Preprocessing**: Techniques like noise reduction and contrast adjustment are crucial for improving OCR accuracy.
- **Text Orientation**: Correcting text orientation helps in accurate text extraction.
- **Text Layout**: Managing text layout to address font size and alignment issues is essential.
- **Format Selection**: Choosing the right document format based on compatibility and usability needs.
- **Manual Editing**: Manual adjustments can refine the final document to closely match the original content.


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your proposed changes. Make sure to follow the contribution guidelines provided in the repository.

## Acknowledgments

- **pytesseract**: [GitHub Repository](https://github.com/madmaze/pytesseract)
- **Pillow**: [GitHub Repository](https://github.com/python-pillow/Pillow)

## License

Copyright [2024] Vishnu Parappulakkal. Licensed under the Apache License, Version 2.0. See [LICENSE](./LICENSE) for details.

## Contact

For further questions, feel free to contact me at [vishnu@vishnu.framer.media](vishnu.framer.media).

## Changelog

- **v1.0.0** - Initial release with core features.
