
import cv2
import numpy as np
from config import SCALES


def croppedFromShot(fileName, box_from, box_from, crop_ratio=[0, 1, 0, 1]):
    image = cv2.imread(fileName)
    # remove fully black area
    image[np.where(image == 0)] = 1
    # transformaton matrix
    TM = cv2.getPerspectiveTransform(box_from, box_to)
    warped = cv2.warpPerspective(image, TM, (image.shape[1],image.shape[0]))
    # substitute blak areas from previous image
    warped[np.where(warped == 0)] = image[np.where(warped == 0)]
    height = warped.shape[0]
    width = warped.shape[1]
    cropped = warped[
            int(height*crop_ratio[0]):int(height*crop_ratio[1]), 
            int(width*crop_ratio[2]):int(width*crop_ratio[3])
        ]
    return cropped