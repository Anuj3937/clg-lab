from PIL import Image
import pytesseract

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image
im = Image.open("samp2.jpeg")

# Perform OCR
text = pytesseract.image_to_string(im, lang='eng')

# Print the extracted text
print(text)