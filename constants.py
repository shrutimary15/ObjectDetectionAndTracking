RESIZE = (1024, 720)
MODEL = 'yolov8n.onnx'
SOURCE = 'Artifacts\cut.mp4'
AREA1 = [(88,380),(90,261),(287,320),(283,442)]   #white
AREA2 = [(80,208),(302,281),(316,272),(95,206)]   #green
LOG_DIR = "logs"