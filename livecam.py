import cv2
import sys
from PIL import Image

def catch_video(window_name, cam_idx):
    # cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(window_name, 400, 300)
    video = cv2.VideoCapture(cam_idx)
    while video.isOpened():
        ok, frame = video.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (200, 150))
        cv2.imshow("", frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
          break
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    catch_video("livecam", 0)
