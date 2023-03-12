from ultralytics import YOLO
import cv2

model = YOLO("../yolo-weights/yolov8n.pt")
result = model("Images/1.png", show=True)          # source of the images
cv2.waitKey(0)




