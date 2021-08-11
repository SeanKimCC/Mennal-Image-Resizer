import os
from os.path import join, isfile
from PIL import Image

BASE_PATH = '/Users/seankim/Developer/Mennal-Hairstyles/Upwork hairstyles'
NEW_FOLDER = '/resized-hairstyles'
SUBFOLDER = ''

def create_file_name(file, folder, width):
    if 'front' in file:
        return folder.split('/')[-1].replace(' ', '-').lower() +  '-front-' + str(width)
    else:
        return folder.split('/')[-1].replace(' ', '-').lower() +  '-side-' + str(width)

def resize_images(path, basewidth):
    try: 
        os.mkdir(os.path.join(BASE_PATH, NEW_FOLDER))
    except OSError as error: 
        print(error)
        
    for folder, subfolders, *_ in os.walk(BASE_PATH):
        full_path = join(BASE_PATH, folder)
        files = [f for f in os.listdir(full_path) if isfile(join(full_path, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        for f in files:
            newFileName = create_file_name(f, folder, basewidth)
            file_path = join(full_path, f)
            img = Image.open(file_path)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            new_file_path = BASE_PATH + NEW_FOLDER + '/' + newFileName + '.png'
            img.save(new_file_path)


resize_images(BASE_PATH, 320)
resize_images(BASE_PATH, 640)
resize_images(BASE_PATH, 1000)
