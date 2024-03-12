# from modules import bigotry_dict, check_content, check_racial_content, read_text
from modules.racist_text_query import racist_text_query
from modules.bigotry_dict import bigotry_dict
from modules.OCR import tiff_to_ocr
from modules.racist_chatgpt_analysis import racist_chatgpt_analysis
from modules.locate import locate
import os

def racism_threshold(file_dir):
  for images in os.listdir(file_dir):
    if images.endswith(".tif"):
      text= tiff_to_ocr(images)

      result1 = racist_chatgpt_analysis(text)
      result2 = racist_text_query(text, bigotry_dict)

      if result1 or result2:
        a,b = locate(text)
        print(a,b)
      else:
        a,b = locate(text)
        print(a,b)

racism_threshold('/Users/vijayfisch/Desktop/DD4G 2024 Land Use')