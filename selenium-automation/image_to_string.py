import pytesseract

from PIL import Image
import pyautogui as ps



        
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


text_from_image = pytesseract.image_to_string(Image.open(r'C:\Users\Amol\Downloads\Capture.png'))
print(text_from_image)

