# Cobot Distance Calculation

This script utilizes the YOLO object detection model to detect objects in an image and calculates the distance from the detected objects to a specified point, which could be useful for guiding a cobot (collaborative robot) in performing pick-up operations.

## Features

- Object detection using YOLOv8 model.
- Calculation of distance from detected objects to a specified point.
- Annotated visualization of distances on the input image.
- Easy integration into your cobot system for pick-up operations.

## Requirements

- Python 3.x
- OpenCV
- Ultralytics YOLO (Install with `pip install ultralytics`)
- Pre-trained YOLOv8 model weights (e.g., `yolov8s.pt`)
- Input images for detection and distance calculation

## Usage

1. Install the required dependencies:

   ```bash
   pip install opencv-python-headless ultralytics

