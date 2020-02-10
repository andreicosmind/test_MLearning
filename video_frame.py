import cv2
import tqdm

def video_frame(path_to_video):
    vid = cv2.VideoCapture(path_to_video)

    while vid.isOpened():
        rest, frame = vid.read()