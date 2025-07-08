

# Solar Event Detection with YOLOv11

## Introduction

This project is inspired by the research paper:  
**Baek et al. (2021)** - *“Solar Event Detection Using Deep-Learning-Based Object Detection Methods”*  
The study focuses on detecting and localizing three types of solar phenomena: **prominence**, **sunspot**, and **coronal hole** using object detection models like SSD and Faster R-CNN.

In this implementation, I utilized **YOLOv11**, selected for its advanced architecture designed to improve multi-scale object detection performance. Unlike earlier YOLO versions, YOLOv11 integrates the **C3K2**, **SPPF**, and **C2PSA** modules, enhancing detection across varied object sizes and feature granularities (Rao, 2023).

## Implementation Overview

The project includes two implementations:  
- **Local Environment (PC)**
- **Google Colaboratory**  
Both follow the same dataset split and training structure.

Due to hardware limitations and the experimental nature of this work, the dataset was structured as follows:
- **Training**: 400 images per class
- **Validation**: 27 (prominence), 48 (sunspot), 25 (coronal hole)
- **Testing**: 30 images (combined)

Note: The traditional 4:1 train:test ratio was not strictly followed.

## Project Structure

- 📂 **Dev Branch**: Contains scripts, datasets, and documentation (subject to change).
- 🔗 **Google Colab Notebook & Resources**: [Access Here](https://drive.google.com/drive/folders/1qoTcQXuHaifFk7X4ffMJCjQRhSMsDpws?usp=sharing) *(request access required)*

## References

- Baek, J. H., Kim, S., Choi, S., et al. (2021). *Solar Event Detection Using Deep-Learning-Based Object Detection Methods*. Solar Physics, 296, 160. [https://doi.org/10.1007/s11207-021-01902-5](https://doi.org/10.1007/s11207-021-01902-5)

- Rao, N. (2023). *YOLOv11 Explained: Next-Level Object Detection with Enhanced Speed and Accuracy*. Medium. [https://medium.com/@nikhil-rao-20/yolov11-explained-next-level-object-detection-with-enhanced-speed-and-accuracy-2dbe2d376f71](https://medium.com/@nikhil-rao-20/yolov11-explained-next-level-object-detection-with-enhanced-speed-and-accuracy-2dbe2d376f71)

- Ultralytics. (2024). *Ultralytics YOLO*. GitHub Repository. [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
- Baek, J.-H., et al. Solar Event Detection Using Deep-Learning-Based Object Detection Methods, 2021.
Dataset used in this project is sourced from the SDO data provided (in part) by the Korea Data Center (KDC) for SDO, in cooperation with NASA, Stanford University (JSOC), and KISTI (KREONET), which is supported by the "Next Generation Space Weather Observation Network" project of the Korea Astronomy and Space Science Institute (KASI).
---


