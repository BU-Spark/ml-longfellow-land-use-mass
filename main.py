# from modules import bigotry_dict, check_content, check_racial_content, read_text
from modules.racist_text_query import racist_text_query
from modules.bigotry_dict import bigotry_dict
from modules.OCR import tiff_to_ocr
from modules.racist_chatgpt_analysis import racist_chatgpt_analysis
from modules.locate import locate
import os

def make_csv(file_dir):
  for images in os.listdir(file_dir):
    if images.endswith(".tif"):
      text= tiff_to_ocr(images)

      result1 = racist_chatgpt_analysis(text)
      result2 = racist_text_query(text, bigotry_dict)

      if result1 or result2:
        page,date = locate(text)
        print(page,date)



make_csv('/Users/vijayfisch/Desktop/DD4G 2024 Land Use/dd4g-land-use-mass')