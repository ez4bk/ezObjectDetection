import cv2
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QPixmap
from numpy import ndarray
from ultralytics.yolo.engine.results import Results

from src.detection_view import Ui_objectdetectionWindow
from src.video_thread import VideoThread


class DetectionControl(QtWidgets.QMainWindow, Ui_objectdetectionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._init_buttons()

        self.video_thread = None
        self.video_status = False
        self.screenshot = None

    def _init_buttons(self):
        self.stopButton.setEnabled(False)
        self.screenshotButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.saveToButton.setEnabled(False)

        self.startButton.clicked.connect(self._on_startButton)
        self.stopButton.clicked.connect(self._on_stopButton)

    def _on_stopButton(self):
        self.video_status = False
        self.video_thread = None

        self.startButton.setEnabled(True)
        if not self.screenshot:
            self.screenshotButton.setEnabled(False)
            self.saveButton.setEnabled(False)
            self.saveToButton.setEnabled(False)

    def _on_startButton(self):
        self.video_status = True

        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.screenshotButton.setEnabled(True)

        self.video_thread = VideoThread(self)
        self.video_thread.update_frame_signal.connect(self._update_frame)
        self.video_thread.update_screenshot_signal.connect(self._update_screenshot)
        self.video_thread.update_result_table.connect(self._update_result_table)
        self.video_thread.finished.connect(self._thread_finished)
        self.video_thread.start()

    @pyqtSlot(ndarray)
    def _update_frame(self, img_arr):
        self.videoView.setPixmap(self.convert_cv_qt(img_arr).scaled(self.videoView.width(), self.videoView.height()))

    @pyqtSlot(ndarray)
    def _update_screenshot(self, img_arr):
        self.screenshot = img_arr

        self.saveButton.setEnabled(True)
        self.saveToButton.setEnabled(True)
        self.screenshotView.setPixmap(self.convert_cv_qt(img_arr).scaled(self.screenshotView.width(), self.screenshotView.height()))

    @pyqtSlot(Results, dict)
    def _update_result_table(self, res, names):
        # for cls in res.boxes.cls:
        #     print(names[int(cls)].strip())
        # for conf in res.boxes.conf:
        #     print(float(conf))
        for output in zip(res.boxes.cls, res.boxes.conf):
            print(names[int(output[0])].strip(), float(output[1]))

    def _thread_finished(self):
        self.video_thread = None
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        if not self.screenshot:
            self.screenshotButton.setEnabled(False)
            self.saveButton.setEnabled(False)
            self.saveToButton.setEnabled(False)

    @staticmethod
    def convert_cv_qt(cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        # p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(convert_to_Qt_format)