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
   
2. Clone this repository:
   
   ````bash
   git clone https://github.com/yourusername/cobot-distance-calculation.git

4. Navigate to the cloned directory:

   ````bash
   cd cobot-distance-calculation

5. Run the script with the input image path provided using --image argument:
   
   ````bash
   python distance_calculation.py --image path/to/your/image.jpg
   Replace path/to/your/image.jpg with the path to your desired image file.

The script will display the input image with annotated distances to the specified point.


## Customization

 You can modify the pixel_per_meter variable in the script to adjust the scale of distance calculation based on your setup.
 For different YOLO models or weights, modify the model = YOLO("yolov8s.pt") line in the script accordingly.


