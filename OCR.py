import pytesseract
from PIL import Image

# Open the image file
img = Image.open('image/1.png')

# Perform OCR using pytesseract
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
