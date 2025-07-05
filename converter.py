import os
import xml.etree.ElementTree as ET

# Define class labels
CLASSES = ['prominence', 'sunspot', 'coronal_hole']

# Input and output directories
ANNOTATIONS_DIR = 'validation_annotation'           # Folder with XML files
OUTPUT_DIR = 'labels/val'               # Single output folder (already created)

def convert_bbox(size, box):
    """Convert VOC to YOLO format (normalized)."""
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x_center = (box[0] + box[1]) / 2.0
    y_center = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x_center * dw, y_center * dh, w * dw, h * dh)

# Process each XML file
for file in os.listdir(ANNOTATIONS_DIR):
    if not file.endswith('.xml'):
        continue

    xml_path = os.path.join(ANNOTATIONS_DIR, file)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    output_lines = []

    for obj in root.findall('object'):
        cls_name = obj.find('name').text.strip().lower()
        if cls_name not in CLASSES:
            print(f" Unknown class '{cls_name}' in {file}, skipping.")
            continue

        cls_id = CLASSES.index(cls_name)
        bbox = obj.find('bndbox')
        xmin = int(float(bbox.find('xmin').text))
        ymin = int(float(bbox.find('ymin').text))
        xmax = int(float(bbox.find('xmax').text))
        ymax = int(float(bbox.find('ymax').text))

        yolo_box = convert_bbox((width, height), (xmin, xmax, ymin, ymax))
        output_lines.append(f"{cls_id} {' '.join(f'{x:.6f}' for x in yolo_box)}")

    if output_lines:
        out_path = os.path.join(OUTPUT_DIR, file.replace('.xml', '.txt'))

        with open(out_path, 'w') as f:
            f.write('\n'.join(output_lines))

        print(f" {file} → {out_path}")
    else:
        print(f" Skipped {file} (no valid objects found)")
