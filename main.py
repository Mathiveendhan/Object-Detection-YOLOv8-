import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

from ultralytics import YOLO

model = YOLO('yolov8m.pt')

results = model.track(source='traffic.mp4', show=True, tracker=" bytetrack.yaml")