import cv2
import torch
from PyQt6.QtCore import QThread, pyqtSignal
from numpy import ndarray
from ultralytics import YOLO
from ultralytics.yolo.engine.results import Results
import torch.cuda as cuda


class VideoThread(QThread):
    update_frame_signal = pyqtSignal(ndarray)
    update_screenshot_signal = pyqtSignal(ndarray)
    update_result_table = pyqtSignal(Results, dict)
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def run(self):
        model = YOLO('yolov8n.pt')
        names = model.names
        device = 0 if cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
        cap = cv2.VideoCapture(0)

        while cap.isOpened() and self.parent.video_status:
            success, frame = cap.read()
            if success:
                results = model(frame, conf=0.5, device=device)
                annotated_frame = results[0].plot()
                self.update_frame_signal.emit(annotated_frame)
                for res in results:
                    self.update_result_table.emit(res, names)
            else:
                self.finished.emit()
