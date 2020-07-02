import cv2
import numpy as np
import os


def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    classes = ["Number plate"]
    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
    label = str(classes[class_id])
    color = COLORS[class_id]
    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    image=img[y:y_plus_h,x:x_plus_w]
    cv2.imshow('cropped',image)
    cv2.imwrite("trying.jpg",image)


def findPlateBox(
    file_path, 
    yolo_cfg="", 
    yolo_weights="",
    conf_threshold=0.1,
    nms_threshold = 0.4,
    min_confidence=0.1
    ):
    if len(yolo_cfg) == 0 :
        yolo_cfg = "/Users/valera/Documents/venprojs/alpr/yolov3/yolo.cfg"
    if len(yolo_weights) == 0 :
        yolo_weights = "/Users/valera/Documents/venprojs/alpr/yolov3/yolo.weights"
    image = cv2.imread(file_path)
    width = image.shape[1]
    height = image.shape[0]
    scale = 0.00392 #1/255
    net = cv2.dnn.readNet(yolo_weights, yolo_cfg)
    blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(get_output_layers(net))
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > min_confidence:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        draw_prediction(
            image, 
            class_ids[i], 
            confidences[i], 
            round(x), round(y), round(x+w), round(y+h)
            )
    return image
        

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
            print(f"processed {i}")

# processAll()
filename = "/Users/valera/Documents/venprojs/alpr/imgs/contrasted/0003.jpg"
filename = "/Users/valera/Documents/venprojs/alpr/imgs/perspective/test.jpg"
displayImg(findPlateBox(filename))

cv2.destroyAllWindows()