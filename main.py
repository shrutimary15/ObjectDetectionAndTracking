import cv2
from ultralytics import YOLO
import supervision as sv
import numpy as np
import cvzone
import logging
import os
import sys
import time

from constants import *
from tracker import update_counters

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_filepath = os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

model = YOLO(MODEL)
logging.info("Model downloaded {}".format(MODEL))

cap = cv2.VideoCapture(SOURCE)

people_enter = {}
counter1 = set() 
counter2 = set()  
people_exit= {}


last_positions1={}
last_positions2={}

logging.info("Tracking video")


while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    if success:
        frame = cv2.resize(frame, (1024, 720))
        results = model.track(frame, persist=True)
        boxes = results[0].boxes
        id = boxes.id
        classes = boxes.cls
        #logging.info(id)
        for i, box in enumerate(boxes.xyxy):
            if int(classes[i]) ==0:
                x3, y3, x4, y4 = map(int, box)
                t = int(id[i])
                cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),1)
                #cv2.circle(frame,(x4,int(y4/2)),4,(0,255,0),-1)
                #cvzone.putTextRect(frame,f'{t}',(x3,y3),1,2)
                print(t, x4, y4)
                
                results = cv2.pointPolygonTest(np.array(AREA1, np.int32), ((x4,y4)),False)
                results1 = cv2.pointPolygonTest(np.array(AREA2, np.int32), ((x4,y4)),False)

                if results>=0:
                    last_positions1[t] = (x4, y4)
                    cv2.circle(frame,(x4,y4),4,(0,0,0),-1)
                    
                elif results1>=0:
                    last_positions2[t] = (x4, y4)
                    cv2.circle(frame,(x4,y4),4,(0,0,0),-1)
             
      
        counter1, counter2, people_enter, people_exit = update_counters(last_positions1, last_positions2, counter1, counter2, people_enter, people_exit)
        enter =  len(counter2)
        exit = len(counter1)
        #logging.info("people entered {}, people exit {}".format(people_enter, people_exit))
        #logging.info("{}, {}".format(counter1, counter2))
        cvzone.putTextRect(frame,f'Enter : {enter}',(50,50),1,2)
        cvzone.putTextRect(frame,f'Exit : {exit}',(50,100),1,2)  

        cv2.polylines(frame,[np.array(AREA1,np.int32)],True,(255,255,255),1)
        cv2.polylines(frame,[np.array(AREA2,np.int32)],True,(0,255,0),1)
        cv2.imshow("YOLOv8 Tracking", frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

logging.info("Completed tracking")
logging.info("people entered {}, people exit {}".format(enter, exit))
