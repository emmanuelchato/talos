from PIL import Image
import pytesseract
import itertools

def ocr():
    (pytesseract.image_to_string(Image.open('vlc2e.png'), lang='eng',config='--psm 6 oem 1 nobacht digits'))
    return (pytesseract.image_to_string(Image.open('vlc2e.png'), lang='eng',config='--psm 6 oem 1 nobacht digits'))  
archivo=open("resultados_ocr.txt", "w")
archivo.write(ocr().encode('utf-8'))
archivo.close()
print ocr()
ocr()    