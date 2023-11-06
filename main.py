from PIL import Image
import pillow_heif
import os

SourceFolder = "C:/Users/tsyga/OneDrive/Изображения/original"
TargetFolder = "C:/Users/tsyga/OneDrive/Изображения/final"

pillow_heif.register_heif_opener()


for file in os.listdir(SourceFolder):
    img = Image.open(f'C:/Users/tsyga/OneDrive/Изображения/original/{file}')
    img.save(f'C:/Users/tsyga/OneDrive/Изображения/final/{file.split(".")[0]}.jpeg', format('jpeg'))

