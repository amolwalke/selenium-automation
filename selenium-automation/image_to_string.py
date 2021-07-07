import pytesseract

from PIL import Image



        
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text_from_image = pytesseract.image_to_string(Image.open(r'C:\Users\Amol\Downloads\createCaptcha.png'))
print(text_from_image)

