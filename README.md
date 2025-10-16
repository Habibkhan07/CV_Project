✨ Image Edge Detection Web App

This is a web application built with Python and Streamlit that allows users to perform real-time edge detection on images. It provides a user-friendly web interface to upload an image, select from various edge detection algorithms (Canny, Sobel, Laplacian), and fine-tune their parameters with interactive controls.

Features

Interactive Web UI: A clean and modern user interface built with Streamlit.

Multiple Algorithms: Choose between Canny, Sobel, and Laplacian edge detection.

Real-time Parameter Tuning: Adjust algorithm-specific parameters like thresholds, kernel sizes, and gradient directions using sliders and dropdowns and see the results instantly.

Image Manipulation: Rotate the uploaded image for better orientation.

Side-by-Side View: Compare the original and the processed image in a clear, side-by-side layout.

Requirements

Python 3.6+

Streamlit

OpenCV

NumPy

Pillow

Installation

Clone the repository:

git clone (https://github.com/Habibkhan07/CV_Project.git)
cd CV_Project


Install the required packages:
It's recommended to use a virtual environment.

pip install -r requirements.txt


Usage

To run the application, execute the following command from your terminal (assuming your script is saved as app.py):

streamlit run main.py


This will launch the web application in your default browser, where you can upload an image and begin experimenting with the edge detection controls.
