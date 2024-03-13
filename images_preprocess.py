from PIL import Image
import os

IMG_SIZE = (160, 100)


def resize_images():
    data_path = "data/"
    species = os.listdir(data_path)
    for mushroom in species:
        data_path = "data/" + mushroom + "/"
        images = os.listdir(data_path)
        for image in images:
            data_path = "data/" + mushroom + "/" + image
            try:
                Image.open(data_path).resize(IMG_SIZE).save(data_path)
                print(f"Image `{data_path}` resized successfully...")
            except (FileNotFoundError, OSError) as e:
                print(f"[ERR] Failed to resize image `{data_path}` :")
                print(e)
                exit()
            except:
                print(f"[ERR] Failed to resize image `{data_path}`.")
                exit()

resize_images()