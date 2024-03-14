from PIL import Image

def crop_image(input_path, output_path):
    image = Image.open(input_path)

    width, height = image.size
    left_width = width * 0.1575
    right_start = width * 0.88
    top_height = height * 0.07

    left_crop = image.crop((0, 0, left_width, top_height))

    right_crop = image.crop((right_start, 0, width, top_height))

    result_width = int(left_width + (width - right_start))
    result_image = Image.new('RGB', (result_width, int(top_height)))

    result_image.paste(left_crop, (0, 0))
    result_image.paste(right_crop, (int(left_width), 0))

    result_image.save(output_path, format='TIFF')
    return result_image