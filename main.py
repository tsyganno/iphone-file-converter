import os
import moviepy.editor as moviepy
import pillow_heif
from PIL import Image

path_proba = 'C:/Users/tsyga/OneDrive/Изображения/1'
SourceFolder = "C:/Users/tsyga/OneDrive/Изображения/original"
TargetFolder = "D:/DataBase from iphone/Download 05-11-2023"

pillow_heif.register_heif_opener()


for file in os.listdir(SourceFolder):
    print('NEW!!!', file)
    if 'MP4' in file.split('.')[-1] or 'mp4' in file.split('.')[-1] or 'MP4' in file.split('.')[-1]:
        clip = moviepy.VideoFileClip(f'C:/Users/tsyga/OneDrive/Изображения/original/{file}')
        if clip.rotation == 90:
            clip = clip.resize(clip.size[::-1])
            clip.rotation = 0
            clip.write_videofile(f'D:/DataBase from iphone/Download 05-11-2023/{file.split(".")[0]}.mp4')
        else:
            clip.write_videofile(f'D:/DataBase from iphone/Download 05-11-2023/{file.split(".")[0]}.mp4')
    elif 'HEIC' in file.split('.')[-1]:
        img = Image.open(f'C:/Users/tsyga/OneDrive/Изображения/original/{file}')
        img.save(f'D:/DataBase from iphone/Download 05-11-2023/{file.split(".")[0]}.jpeg', format('jpeg'))
    elif 'MOV' in file.split('.')[-1]:
        clip = moviepy.VideoFileClip(f'C:/Users/tsyga/OneDrive/Изображения/original/{file}')
        if clip.rotation == 90:
            clip = clip.resize(clip.size[::-1])
            clip.rotation = 0
            clip.write_videofile(f'D:/DataBase from iphone/Download 05-11-2023/{file.split(".")[0]}.mp4')
        else:
            clip.write_videofile(f'D:/DataBase from iphone/Download 05-11-2023/{file.split(".")[0]}.mp4')
    elif 'jpg' in file.split('.')[-1] or 'JPG' in file.split('.')[-1] or 'png' in file.split('.')[-1] or 'PNG' in file.split('.')[-1]:
        try:
            img = Image.open(f'C:/Users/tsyga/OneDrive/Изображения/original/{file}')
            img.save(f'D:/DataBase from iphone/Download 05-11-2023/{file}')
        except:
            print('FUCK jpg', file)
    else:
        print('No! No! No!', file)

