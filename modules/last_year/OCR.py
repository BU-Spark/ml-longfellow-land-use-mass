from PIL import Image
from io import BytesIO
import pytesseract

def tiff_to_ocr(path):
    img = Image.open(path)
    TempIO = BytesIO()
    img.save(TempIO,format="JPEG")
    img = Image.open(BytesIO(TempIO.getvalue()))

    return pytesseract.image_to_string(img)