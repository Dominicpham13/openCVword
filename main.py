import cv2
import pytesseract
from PIL import Image



img_file= "C:\Users\Dominic Pham\Desktop\Python work etc\data\page_01.jpg"
img = cv2.imread(img_file)


ocr_result = pytesseract.image_to_string(img)

print(ocr_result)
