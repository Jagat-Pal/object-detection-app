# object-detection-app
Object detection app create by streamlit and deployment on heroku
Object Detection and Tracking in real-time video is a crucial area of computer vision that has numerous applications in various fields like surveillance, automotive, and robotics.

The demand for real-time object detection and tracking in video frames is increasing every day due to the need for automated systems that can recognize and track objects, identify their position and classify them in real-time.

In this project, we have developed an application that uses the YOLOv8 object detection and tracking algorithm to detect and track objects in real-time video streams. The application is built using the Streamlit framework, which provides an intuitive and interactive user interface for the end-users to interact with the system.
![object_detection_image](https://github.com/Jagat-Pal/object-detection-app/assets/100485263/c793b4e7-b2f9-4c02-9b68-c3042c43c90b)
#Object Detection Object detection is the process of identifying and localizing objects in an image or video frame.
Object detection algorithms typically employ deep learning models, such as YOLO, Faster R-CNN, and SSD, to detect objects in images or video frames. These models use convolutional neural networks (CNNs) to extract features from the input data and then use these features to classify and localize objects. #Real-time Detection in Video Frames Real-time object detection and tracking in video frames is a challenging task due to the need for high processing speeds and accuracy.

The YOLOv8 algorithm used in this project provides real-time object detection and tracking capabilities, making it ideal for applications that require fast and accurate object detection in real-time video streams. #Why YOLOv8 is a Good Choice for Object Detection and Tracking YOLOv8 (You Only Look Once version 8) is an object detection model that uses deep neural networks to detect objects in images or videos. YOLOv8 is one of the latest versions of the YOLO series, and it offers improved accuracy and faster detection speeds.

YOLOv8 is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. YOLOv8 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection and tracking, instance segmentation, image classification and pose estimation tasks.

It uses a single neural network to divide an input image or video into a grid of cells, and each cell is responsible for detecting objects in that region. The network also predicts bounding boxes, confidence scores, and class probabilities for each object detected. The bounding boxes are used to localize the object in the image, and the confidence scores indicate the accuracy of the detection. The class probabilities determine the type of object detected, such as a car or a person. #Why Streamlit is a Good Choice for Building a Real-Time App Streamlit makes it easy to build web-based user interfaces for machine learning applications, enabling data scientists and developers to share their work with non-technical stakeholders.

Streamlit is an open-source framework that simplifies the process of building web applications in Python. In this project, Streamlit is used to create a web application that displays the processed video stream, allowing users to adjust various ML Model parameters such as the detection threshold confidence and the tracking algorithm. #Project Setup: Installing Dependencies and Creating Required Files and Directories Before diving into the project, make sure you have the following dependencies installed on your system.

The project requires Python 3.10 or higher and several Python packages such as NumPy, OpenCV, PyTorch, and Streamlit. We can install these packages using pip into a separate virtual environment. Creating Virtual Environment When working on a Python project, it’s important to keep your dependencies separate from your global Python environment to prevent conflicts between different projects.

One way to achieve this is by creating a virtual environment, which is an isolated Python environment that can be used to install and manage project-specific dependencies.

This ensures that your project runs smoothly and consistently, even if different versions of the same package are required for different projects. #Installing Required Packages After this, you are ready to install yolov8 (Ultralytics), Streamlit and Pafy packages. #Downloading Pre-trained Yolov8 Weights The YOLOv8 model is a deep neural network that has been trained on a large dataset to detect objects in images and videos. To use this model for object detection and tracking, we need to download the pre-trained YOLOv8 weights.

In this section, we will explain how to download the pre-trained YOLOv8 weights and use them in our project.

Use this link to download yolov8n.pt weight file. The yolov8n weight file is the smallest of the YOLOv8 models, making it faster and more efficient than the other variants. With its high accuracy and ability to detect objects in real-time, this model has become a popular choice for many computer vision applications. #Creating Images Directory Create another directory named ‘images’ to store all the images you want to detect objects upon.

#Creating Required Python files We will create the following Python files for our project:

#settings.py This file contains all the constants and configuration settings required for the project. It defines the path to the YOLOv8 model, the confidence threshold, the non-maximum suppression threshold, and the names of the objects to detect. It also contains settings related to the Streamlit app, such as the default image and video URLs.

#app.py This is the project's main file, which contains the Streamlit app. It defines the layout of the app, which includes a file uploader, a video player, a confidence threshold slider, and an object selection dropdown. It also defines the logic of the app, which includes loading the YOLOv8 model, detecting objects in the uploaded image or video frames, and displaying the detected objects.

#helper.py This file contains helper functions used in the project. It includes functions to load the YOLOv8 model, preprocess the input image or video frames, and post-process the output bounding boxes and class labels. #Your project folder should look like this.
![Screenshot 2023-08-05 134258](https://github.com/Jagat-Pal/object-detection-app/assets/100485263/a8939aeb-73eb-4281-8593-d4aa4a25ff73)
