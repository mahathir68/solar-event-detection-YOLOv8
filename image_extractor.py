import os
import shutil

# 📂 Source directory containing .jpg files
SOURCE_DIR = 'validation_annotation'  # Replace with your actual folder name containing all images

# 📁 Destination directory
DEST_DIR = os.path.join('images', 'val')

# 🚨 Make sure destination exists (you will create it manually)
if not os.path.isdir(DEST_DIR):
    print(f"❌ Destination folder '{DEST_DIR}' not found. Please create it first.")
    exit()

# 🔁 Move all .jpg files
moved = 0
for file in os.listdir(SOURCE_DIR):
    if file.lower().endswith('.jpg'):
        src_path = os.path.join(SOURCE_DIR, file)
        dst_path = os.path.join(DEST_DIR, file)
        shutil.move(src_path, dst_path)
        moved += 1
        print(f"✅ Moved: {file}")

print(f"\n🎉 Done. Total images moved: {moved}")
