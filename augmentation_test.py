import cv2
import numpy as np
from keras_preprocessing.image import ImageDataGenerator, load_img, img_to_array
import os

def genAugForImage(file_path, save_dir="augmented", variations=5):
    img = load_img(file_path)
    x = img_to_array(img) # color image (3, 1280,720)
    x = x.reshape((1,) + x.shape) # extra dim for keras - (1, 3, 1280, 720)
    datagen = ImageDataGenerator(
        rotation_range=10, width_shift_range=0.2, 
        height_shift_range=0.2, shear_range=0.3, 
        zoom_range=0.1, channel_shift_range = 10, horizontal_flip=False
        )
    # datagen.fit(x)
    save_dir = f"{os.path.split(file_path)[0]}/{save_dir}"
    i = 0
    for batch in datagen.flow(
        x,
        save_to_dir=save_dir,
        save_format='jpeg',
        batch_size=10
    ):            
        i+=1
        if i >= variations: break
    return i


def genAugForDirectory(start_dir, save_dir="augmented"):
    datagen = ImageDataGenerator(
        rotation_range=10, width_shift_range=0.2, 
        height_shift_range=0.2, shear_range=0.3, 
        zoom_range=0.1, channel_shift_range = 10, horizontal_flip=False
        )
    save_dir = f"{start_dir}/{save_dir}"
    print(start_dir, save_dir)
    imageIter = datagen.flow_from_directory(
        start_dir,
        save_to_dir=save_dir,
        save_format='jpeg',
        batch_size=10
        )
    imageIter.next()



def displayImg(img, title="Original"):
    cv2.imshow(title, img)
    if cv2.waitKey(0) & 0xFF == ord('s'):
        cv2.imwrite(f"test_{title}.jpg", img)
    else:
        pass

def processAll():
    _src = "/Users/valera/Documents/venprojs/alpr/imgs/contrasted/"
    _ext = ".jpg"
    _dest = "/Users/valera/Documents/venprojs/alpr/imgs/contrasted/"
    for i, filename in enumerate(os.listdir(_src)):
        if filename.endswith(_ext):
            base, ext = os.path.splitext(filename)
            genAugForImage(_src + filename)
            print(f"processed {i}")

processAll()
filename = "/Users/valera/Documents/venprojs/alpr/imgs/contrasted/0003.jpg"
dir_name = "/Users/valera/Documents/venprojs/alpr/imgs/contrasted/augmented"
# genAugForImage(filename)
# genAugForDirectory(dir_name)
