import os
import moviepy.editor as moviepy
import pillow_heif
from PIL import Image


SourceFolder = "C:/Users/tsyga/OneDrive/Изображения/original"
TargetFolder = "C:/Users/tsyga/OneDrive/Изображения/final"

pillow_heif.register_heif_opener()


for file in os.listdir(SourceFolder):
    if 'HEIC' in file:
        img = Image.open(f'C:/Users/tsyga/OneDrive/Изображения/original/{file}')
        img.save(f'C:/Users/tsyga/OneDrive/Изображения/final/{file.split(".")[0]}.jpeg', format('jpeg'))
    elif 'MOV' in file:
        clip = moviepy.VideoFileClip(f'C:/Users/tsyga/OneDrive/Изображения/original/{file}')
        if clip.rotation == 90:
            clip = clip.resize(clip.size[::-1])
            clip.rotation = 0
            clip.write_videofile(f'C:/Users/tsyga/OneDrive/Изображения/final/{file.split(".")[0]}.mp4')
        else:
            clip.write_videofile(f'C:/Users/tsyga/OneDrive/Изображения/final/{file.split(".")[0]}.mp4')
    else:
        print(file)

