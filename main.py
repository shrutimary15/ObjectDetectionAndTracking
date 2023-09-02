import cv2
from ultralytics import YOLO
import supervision as sv
import numpy as np
import cvzone
import logging
import os
import sys

from constants import *
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



