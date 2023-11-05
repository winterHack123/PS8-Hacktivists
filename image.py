from PIL import Image
import pytesseract
import time

Lines = []      #Will store text

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"   #Or wherever your tesseract exe is stored

image  = Image.open('OIP.jpeg')
string  = pytesseract.image_to_string(image)

print(string)