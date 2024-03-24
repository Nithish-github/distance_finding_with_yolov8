import cv2
import math
import argparse
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

# Load YOLO model
model = YOLO("yolov8s.pt")

# Define constants
pixel_per_meter = 10
txt_color, txt_background, bbox_clr = ((0, 0, 0), (255, 255, 255), (255, 0, 255))

# Creating the named window
cv2.namedWindow("Cobot-Distance-Calculation", cv2.WINDOW_NORMAL)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Cobot Distance Calculation")
parser.add_argument("--image", required=True, help="Path to the input image file")
args = parser.parse_args()

# Read input image
im0 = cv2.imread(args.image)
if im0 is None:
    print("Error: Unable to read the image file.")
    exit(1)

# Get image dimensions
w, h, c = im0.shape
center_point = (0, h)

# Initialize annotator
annotator = Annotator(im0, line_width=2)

# Track objects in the image
results = model.track(im0, persist=True, conf=0.2)
boxes = results[0].boxes.xyxy.cpu()

# Process tracked objects
if results[0].boxes.id is not None:
    track_ids = results[0].boxes.id.int().cpu().tolist()

    for box, track_id in zip(boxes, track_ids):
        annotator.box_label(box, label=str(track_id), color=bbox_clr)
        annotator.visioneye(box, center_point)

        x1, y1 = int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)  # Bounding box centroid

        # Calculate distance
        distance = (math.sqrt((x1 - center_point[0]) ** 2 + (y1 - center_point[1]) ** 2)) / pixel_per_meter

        # Draw distance information on the image
        text_size, _ = cv2.getTextSize(f"Distance: {distance:.2f} m", cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)
        cv2.rectangle(im0, (x1, y1 - text_size[1] - 10), (x1 + text_size[0] + 10, y1), txt_background, -1)
        cv2.putText(im0, f"Distance: {distance:.2f} m", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.2, txt_color, 3)

# Display the annotated image
cv2.imshow("Cobot-Distance-Calculation", im0)
cv2.waitKey(0)
cv2.destroyAllWindows()
