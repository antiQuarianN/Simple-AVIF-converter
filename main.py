import os
from PIL import Image
import av

def convert_avif_to_png(avif_path, png_path):
    # Open AVIF file with pyav
    container = av.open(avif_path)
    for frame in container.decode(video=0):
        # Convert frame to numpy array
        img = frame.to_image()
        img.save(png_path, format='PNG')
        break

def batch_convert_avif_to_png(source_dir):
    # Create a target directory next to the source directory
    target_dir = os.path.join(source_dir, 'converted_png')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Run through all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.avif'):
            avif_path = os.path.join(source_dir, filename)
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(target_dir, png_filename)
            
            try:
                convert_avif_to_png(avif_path, png_path)
                print(f'Converted {filename} to {png_filename}')
            except Exception as e:
                print(f'Failed to convert {filename}: {e}')

# Запрос пути к директории с AVIF изображениями у пользователя
source_dir = input('Enter the path to the folder with the AVIF images: ')
batch_convert_avif_to_png(source_dir)