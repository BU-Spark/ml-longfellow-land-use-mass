from modules.racist_text_query import racist_text_query
from modules.bigotry_dict import bigotry_dict
from modules.OCR import tiff_to_ocr
from modules.racist_chatgpt_analysis import racist_chatgpt_analysis
from modules.locate import locate
from modules.pagenum import crop_image
import os
import pandas as pd

def racism_threshold(file_dir):
    # Create the new folder for cropped images
    cropped_images_dir = os.path.join(file_dir, 'deed page number')
    if not os.path.exists(cropped_images_dir):
        os.makedirs(cropped_images_dir)

    data = []
    for images in os.listdir(file_dir):
        if images.endswith(".tif") or images.endswith(".tiff"):
            image_path = os.path.join(file_dir, images)

            # run ocr on images
            text = tiff_to_ocr(image_path)

            result1 = racist_chatgpt_analysis(text)
            result2 = racist_text_query(text, bigotry_dict)

            a, b, c = locate(text)
            
            # Define the output path for the cropped image in the new folder
            cropped_image_name = "cropped_" + images
            cropped_image_path = os.path.join(cropped_images_dir, cropped_image_name)
            
            # Crop the image and save it to the new folder
            crop_image(image_path, cropped_image_path)
            
            image_path_formatted = cropped_image_path
            #.replace(' ', '%20')
            hyperlink_formula = f'file://{image_path_formatted}'
            
            # fail safe page number detection 
            page = tiff_to_ocr(cropped_image_path)
            fail_safe_page = []
            result = page.split("\n")
            for word in result:
              # checks for possible page numbers
              if word.isdigit() == True:
                fail_safe_page.append(word)
            
            
            if result1 or result2:
                print(images, a, b, c)
                if len(fail_safe_page) != 0:
                    a.append(fail_safe_page)
                data.append([images, a, b[0], c[0], hyperlink_formula])
            else:
                print(images + " : Not Racist")
                # data.append([images, a, b[0], c[0], hyperlink_formula])

    # Include the hyperlink in the DataFrame columns
    df = pd.DataFrame(data, columns=['File Name', 'Probable Page Number', 'Date', 'Book Number', "Page Link"])
    df.index += 1
    df.to_csv(os.path.join(file_dir, 'Racist Deeds.csv'), index=True)
    df.to_excel(os.path.join(file_dir, 'Racist Deeds.xlsx'), index=True)

racism_threshold('folderpath')
