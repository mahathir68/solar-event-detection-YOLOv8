from ultralytics import YOLO
import time
import psutil
import torch
from tqdm import tqdm

# Logging setup
LOG_PATH = "training_performance_log_cpu.txt"
with open(LOG_PATH, "w") as log:
    log.write("epoch,time(s),cpu(%),ram(%),fps\n")



# Load a YOLO11n model to train from scratch
model = YOLO("yolo11m.yaml")

# Train the model on the COCO8 dataset for 100 epochs
train_results = model.train(
    data="config.yaml",  # Path to dataset configuration file
    epochs=3,  # Number of training epochs
    imgsz=512,  # Image size for training
    device= "cpu"  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
)

# Evaluate the model's performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("20100902_000032_SDO_AIA_304_512.jpg")  # Predict on an image
results[0].show()  # Display results

# Export the model to ONNX format for deployment
path = model.export(format="onnx")  # Returns the path to the exported model



def log_resources(epoch, duration, frame_count):
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    fps = frame_count / duration if duration > 0 else 0

    with open(LOG_PATH, "a") as log:
        log.write(f"{epoch},{duration:.2f},{cpu_usage},{ram_usage},{fps:.2f}\n")

def get_model_size(model):
    param_size = sum(p.numel() for p in model.parameters())
    mb_size = sum(p.element_size() * p.numel() for p in model.parameters()) / 1024**2
    return param_size, mb_size