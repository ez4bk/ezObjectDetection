# EZ Real-time Object Detection
EZ-RTOD is able to capture the video source on your decision and
labeling objects appeared in the video using the Yolov8 model. At the mean
time, number of frames of each object appeared will be recorded and shown.
Users can choose to export the records to a csv file or an Excel file.

This is a simple demonstration of utilizing Yolov8 model and OpenCV to 
perform real-time object detection.

The Yolov8 model is directly by importing the 
[Ultralytics](https://github.com/ultralytics/ultralytics) 
PyPI package. And the included weights file 
[yolov8n.pt](https://github.com/ez4bk/ezObjectDetection/blob/main/yolov8n.pt) 
is also the default one downloaded from the Ultralytics website.

The UI is made up by PyQt6. Shout out to 
[qtbox](https://github.com/la-vie-est-belle/qtbox)@la-vie-est-belle and 
@[Silverfox_j](https://space.bilibili.com/9989/) 
for the inspiration of the qss stylesheet and the overall ui design.

## Recent TODOs
- [ ] Add a progress bar for the video processing
- [ ] Export the records to file
- [ ] Settings to tweak the parameters of Yolo
- [ ] Settings to choose the source of the video.
- [ ] Export the screenshot.

## Set up
The development environment is Python 3.9.1 on macOS Big Sur 11.2.3 (M1 Pro).
But it should be fine on Windows as well.
### Install dependencies
```shell
pip install -r requirements.txt
```
And you should be all set to go.

In case the requirements.txt is not working,
```shell
pip install opencv-python, torch, PyQt6, numpy, ultralytics
```
PyQt5 is only available on X86_64 Macs, Rosetta is required to install PyQt5 
on Apple Silicons. To avoid complexity, PyQt6 is used as it works perfectly 
fine on both Windows and macOS, as well as Apple Silicons.

Linux's availability is not tested yet.

## Open Source
This project is entirely open source, and you are free to use it or fork it in any way.

## Contact
If you have any questions, or if you want to cooperate in the project, 
feel free to contact me at [ycwei328@gmail.com](mailto:ycwei328@gmail.com).