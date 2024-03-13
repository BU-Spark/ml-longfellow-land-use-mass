# from modules import bigotry_dict, check_content, check_racial_content, read_text
from modules.racist_text_query import racist_text_query
from modules.bigotry_dict import bigotry_dict
from modules.OCR import tiff_to_ocr
from modules.racist_chatgpt_analysis import racist_chatgpt_analysis
from modules.locate import locate
import os
import pandas as pd

def racism_threshold(file_dir):
  data =[]
  for images in os.listdir(file_dir):
    if images.endswith(".tif") or images.endswith(".tiff"):
      text= tiff_to_ocr(images)

      result1 = racist_chatgpt_analysis(text)
      result2 = racist_text_query(text, bigotry_dict)

      if result1 or result2:
        a,b = locate(text)
        print(images,a,b)
        data.append([images,a[0], b[0]])
      else:
        print(images  + " : Not Racist")

      
  #print(data)
  df = pd.DataFrame(data, columns = ['File name', 'Page Number', 'Date'])
  df.index += 1
  df.to_csv('Racist Deeds.csv', index = True)
  #print(df)
        

racism_threshold('/Users/namannagaria/Desktop/new/dd4g-land-use-mass')