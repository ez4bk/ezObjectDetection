import cv2
import torch
from PyQt6.QtCore import QThread, pyqtSignal
from numpy import ndarray
from ultralytics import YOLO
import torch.cuda as cuda


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(ndarray)
    output_img_signal = pyqtSignal(ndarray)
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def run(self):
        model = YOLO('yolov8.pt')
        names = model.names
        device = 0 if cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
        cap = cv2.VideoCapture(self.parent.video_path)
        b = True

        while cap.isOpened() and b:
            success, frame = cap.read()
            if success:
                results = model(frame, conf=0.05, iou=0.3, device=device)
                annotated_frame = results[0].plot()
                self.change_pixmap_signal.emit(annotated_frame)
                for res in results:
                    for cls in res.boxes.cls:
                        if names[int(cls)].strip() in []:
                            print("Abnormal behavior suspected: " + names[int(cls)].strip())
                            self.output_img_signal.emit(annotated_frame)
                            b = False
            else:
                self.finished.emit()
