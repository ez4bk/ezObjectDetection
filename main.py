from PyQt6 import QtWidgets
import sys

from src.detection_control import DetectionControl

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DetectionControl()
    window.show()
    sys.exit(app.exec())
