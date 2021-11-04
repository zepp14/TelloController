import time, cv2
from threading import Thread
from djitellopy import Tello
import sys

tello = Tello()

tello.connect()


keepRecording = True
tello.streamon()


frame_read = tello.get_frame_read()
time.sleep(3)

tracker = cv2.TrackerCSRT_create()



bbox = (287, 23, 86, 320)
frame = frame_read.frame
bbox = cv2.selectROI(frame, False)
ok = tracker.init(frame, bbox)

while(1):s
    # Capture frame-by-frame
    frame = frame_read.frame
    try:
        ok, bbox = tracker.update(frame)
        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    except:
        pass
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
