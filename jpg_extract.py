import os
from PIL import Image

def extract_images(input_image_path, output_dir):
    with open(input_image_path, 'rb') as f:
        content = f.read()

    offset = 0
    while offset != -1:
        offset = content.find(b'\xFF\xD8', offset + 1)
        end = content.find(b'\xFF\xD9', offset + 1)

        if offset != -1 and end != -1:
            with open(f'{output_dir}/image_{offset}.jpg', 'wb') as img_f:
                img_f.write(content[offset:end+2])

extract_images('<original_file>.jpg', 'output')
