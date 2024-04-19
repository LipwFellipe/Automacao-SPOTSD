import pytesseract
import cv2
caminho = "C:\Program Files\Tesseract-OCR"

imagemselecionada  = cv2.imread("img2.jpg")
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagemselecionada)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
print(texto)