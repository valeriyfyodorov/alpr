MAC_OS = True
MAC_TEST_LOCATION = '/Users/Valera/Documents/venprojs/alpr/html/'

VIDEO_CAPTURE_DEVICE = -1 # ls /dev/video* first for right camera device here, minus 1 means first working
WEBCAM_BUFFER_SIZE = 5
WEBCAM_COLD_START = False
global video_capture

IMAGES_DIRECTORY = '/var/www/html/'
if MAC_OS:
    IMAGES_DIRECTORY = MAC_TEST_LOCATION

SCALES_NAME_FOR_ID = {"0": "north", "1": "south"}
SCALES = {
    "north":
    {
        "id": 0,
        "cam_front": 
        {
            "url": "rtsp://192.168.21.113:554/video2",
            "crop_ratio": [0.61, 0.97, 0.255, 0.99],
            "warp_from": [[879,539], [879,576], [1018,570], [1019,537]],
            "warp_to": [[879,539], [879,576], [1049,576], [1049,539]],
        },
        "cam_rear": 
        {
            "url": "rtsp://192.168.21.114:554/video2",
            "crop_ratio": [0.39, 0.81, 0.35, 0.8],
            "warp_from": [[528,332], [528,355], [631,354], [631,332]],
            "warp_to": [[528,332], [528,354], [631,354], [631,332]],
        },
        "modbus": 
        {
            "host": "192.168.21.124",
            "port": 504,
        },
    },
    "south":
    {
        "id": 1,
        "cam_front": 
        {
            "url": "rtsp://192.168.21.113:554/video2",
            "crop_ratio": [0.5, 0.9, 0.1, 0.7],
            "warp_from": [[684,398], [685,425], [807,425], [804,398]],
            "warp_to": [[684,398], [685,427], [820,427], [820,398]],
        },
        "cam_rear": 
        {
            "url": "rtsp://192.168.21.114:554/video2",
            "crop_ratio": [0.5, 0.9, 0.1, 0.7],
            "warp_from": [[430,458], [430,562], [750,580], [750,466]],
            "warp_to": [[430,466], [430,580], [750,580], [750,466]],
        },
        "modbus": 
        {
            "host": "192.168.21.124",
            "port": 504,
        },
    },
}

class PlatesSet:
    def __init__(self, front="", rear=""):
        self.front = front
        self.rear = rear
        self.full = f"{{front}}/{{rear}}"
    
    def __str__(self): 
        return f"front: {self.front} rear: {self.rear}"
