from PIL import Image,ExifTags
from pillow_heif import register_heif_opener
import os
import datetime

register_heif_opener()

#Global values
compression_folder="02_Images compressées"
image_folder="01_Images"

def main():
    folder_check(compression_folder)
    if not(folder_check(image_folder)):
        print("Création des dossiers....")
        return
    image_list = get_image_list(image_folder)
    output = get_output_name()
    i=1
    for image in image_list:
        image_compression(f"{image_folder}/{image}",f"{compression_folder}/{output}({i}).jpg",300)
        i+=1

def folder_check(path): #Creates folder or checks for it 
    if os.path.exists(path) :
        return True
    else :
        os.mkdir(path)

def image_compression(input_path,output_path,max_size_kb): #Compress image to a given size in kb
    quality=95
    with Image.open(input_path) as im:
        try:
        # Obtenir les tags EXIF (dont l’orientation)
            exif = im._getexif()
            if exif is not None:
                for tag, value in exif.items():
                    if ExifTags.TAGS.get(tag) == 'Orientation':
                        orientation = value

                        # Appliquer la rotation en fonction de l'orientation EXIF
                        if orientation == 3:
                            im = im.rotate(180, expand=True)
                        elif orientation == 6:
                            im = im.rotate(270, expand=True)
                        elif orientation == 8:
                            im = im.rotate(90, expand=True)
                        break
        except Exception as e:
            pass

        while True:
            im.save(output_path,quality=quality,optimize=True)
            if os.path.getsize(output_path)/1024<=max_size_kb :
                print(os.path.getsize(output_path))
                return True
            quality-= 5

def get_image_list(path):
    l = []
    for file in os.listdir(path):
        try :
            _,extension=os.path.splitext(file)
            if extension.lower() in [".jpg",".jpeg",".png",".heic"]:
                l.append(file)
            else :
                raise ValueError
        except IndexError:
            pass
        except ValueError:
            pass
    return l

def get_output_name():
    name=input("nom des images ? pour juste la date du jour ne rien rentrer")
    if name=="":
        return datetime.datetime.today().strftime('%Y-%m-%d')
    else :
        return name

if __name__=="__main__":
    main()