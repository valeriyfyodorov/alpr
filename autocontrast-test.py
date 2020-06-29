import cv2
import numpy as np
from config import SCALES
import os

def recontrastFileImg(file_test):
    # file_test = "/Users/valera/Documents/venprojs/alpr/imgs/0003.jpg"
    # file_test = "/Users/valera/Documents/venprojs/alpr/imgs/0001.jpg"

    image = cv2.imread(file_test)
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(2,2))
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    corrected = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    return corrected

def displayImg(img, title="Original"):
    cv2.imshow(title, img)
    if cv2.waitKey(0) & 0xFF == ord('s'):
        cv2.imwrite(f"test_{title}.jpg", img)
    else:
        pass

def processAll():
    _src = "/Users/valera/Documents/venprojs/alpr/imgs/"
    _ext = ".jpg"
    _dest = "/Users/valera/Documents/venprojs/alpr/imgs/contrasted/"
    for i, filename in enumerate(os.listdir(_src)):
        if filename.endswith(_ext):
            base, ext = os.path.splitext(filename)
            cv2.imwrite(_dest + base + ext, recontrastFileImg(_src + filename))

processAll()
# filename = "/Users/valera/Documents/venprojs/alpr/imgs/0003.jpg"
# base, ext = os.path.splitext(filename)
# print(os.path.split(filename)[0] + base + "_procssd" + ext)
# filename = "/Users/valera/Documents/venprojs/alpr/imgs/0076.jpg"
# displayImg(recontrastFileImg(filename))

cv2.destroyAllWindows()