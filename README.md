 Image Edge Detection
 
Description

This  designed for interactive image processing, specifically focusing on edge detection.

The app allows users to upload their own images and apply various popular edge detection algorithms, including Canny, Sobel, and Laplacian. A dedicated sidebar provides dynamic controls to fine-tune the parameters for the selected algorithm (e.g., Canny thresholds, Sobel kernel size, image rotation), allowing for real-time visual analysis of the results.

Key Features:
* Multiple Algorithms Choose between Canny, Sobel, and Laplacian.
* Real-time Parameter Tuning Instantly adjust algorithm-specific settings via the sidebar controls.
* Image Rotation Pre-process the image by rotating it by 0° or 270°.
* Side-by-Side Comparison: View the original image and the processed, edge-detected image concurrently.

 Setup and Installation

To run this application locally, you need to have Python installed on your system.

Prerequisites
* Python 3.7+

 Installation Steps

Install the required libraries:
    The application uses streamlit, Pillow (PIL), numpy, and opencv-python (cv2).

    
    pip install streamlit pillow numpy opencv-python
   

## ▶️ How to Run the Application

1.  Save the provided Python code into a file named main.py.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved main.py.
4.  Run the application using the Streamlit command:

  
    streamlit run app.py


5.  Streamlit will automatically open the application in your default web browser (usually at http://localhost:8501).

 Application Interface and Output

The interface is divided into a main display area and a control sidebar. The main area shows the input and output images, while the sidebar hosts all configuration settings.

Screenshot 1: Canny Edge Detection with Controls


<img width="1781" height="877" alt="Canny" src="https://github.com/user-attachments/assets/693330a6-4678-45f2-8590-c94612d79606" />


 Screenshot 2: Sobel Edge Detection Configuration

<img width="1788" height="813" alt="Sobel" src="https://github.com/user-attachments/assets/54e48c4e-27b5-455a-9c62-1092e8947bbc" />

 Screenshot 3: laplacian Edge Detection Configuration


<img width="1787" height="852" alt="laplacian" src="https://github.com/user-attachments/assets/b66d39e6-e8e0-4b64-957f-cda015a98193" />





 
