#%%
from PIL import Image
import os

#%%
input_folder = './source_images'
output_folder = './images'

os.makedirs(output_folder, exist_ok=True)

target_size = (1280, 720)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                resized_img.save(output_path)
                print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
#%%