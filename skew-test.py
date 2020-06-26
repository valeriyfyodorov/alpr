import cv2
import numpy as np
from config import SCALES

il_0_front = "/Users/valera/Documents/venprojs/alpr/imgs/perspective/00_front_115_520.jpg"
il_0_rear = "/Users/valera/Documents/venprojs/alpr/imgs/perspective/00_rear_115_520.jpg"
il_1_front = "/Users/valera/Documents/venprojs/alpr/imgs/perspective/01_front_115_520.jpg"
il_1_rear = "/Users/valera/Documents/venprojs/alpr/imgs/perspective/01_rear_115_520.jpg"

image = cv2.imread(il_1_rear)
# remove fully black area
image[np.where(image == 0)] = 1

# cv2.imshow("Image", image)
# if cv2.waitKey(0) & 0xFF == ord('s'):
#     cv2.imwrite("test_cropped_1_f.jpg", cropped)
# else:
#     pass

# cam = SCALES["north"]["cam_front"]
cam = SCALES["south"]["cam_rear"]
box_from = np.float32(cam["warp_from"])
box_to = np.float32(cam["warp_to"])
# transformaton matrix
TM = cv2.getPerspectiveTransform(box_from, box_to)
warped = cv2.warpPerspective(image, TM, (image.shape[1],image.shape[0]))

# cv2.imshow("Warped", warped)
# if cv2.waitKey(0) & 0xFF == ord('s'):
#     cv2.imwrite("test_cropped_1_f.jpg", cropped)
# else:
#     pass

# substitute blak areas from previous image
warped[np.where(warped == 0)] = image[np.where(warped == 0)]

# cv2.imshow("Warped", warped)
# if cv2.waitKey(0) & 0xFF == ord('s'):
#     cv2.imwrite("test_cropped_1_f.jpg", cropped)
# else:
#     pass

# relative cropping
height = warped.shape[0]
width = warped.shape[1]
crop_ratio=cam["crop_ratio"]
cropped = warped[
        int(height*crop_ratio[0]):int(height*crop_ratio[1]), 
        int(width*crop_ratio[2]):int(width*crop_ratio[3])
    ]
cv2.imshow("Cropped", cropped)
if cv2.waitKey(0) & 0xFF == ord('s'):
    cv2.imwrite("test_cropped_1_r.jpg", cropped)
else:
    pass
cv2.destroyAllWindows()