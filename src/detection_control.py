from PyQt6 import QtWidgets

from detection_view import Ui_objectdetectionWindow


class DetectionControl(QtWidgets.QMainWindow, Ui_objectdetectionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._init_buttons()

        self.video_thread = None


    def _init_buttons(self):
        self.pushButton.clicked.connect(self._on_button_clicked)
