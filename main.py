import streamlit as st
from PIL import Image
import numpy as np
import cv2

# --- Page Configuration ---
st.set_page_config(
    layout="wide",
    page_title="Image Edge Detection",
    page_icon="✨"
)




# --- UI Configuration ---
st.title("✨ Image Edge Detection")
st.write(
    "Welcome! Upload an image and select an edge detection algorithm. "
    "Use the controls in the sidebar to fine-tune the algorithm parameters and see the results instantly."
)
st.sidebar.title("Controls & Settings")
st.sidebar.markdown("---")

# --- Main Application Logic ---
def process_image(image_file, algorithm, params, rotation_angle=0):
    """
    Loads an image, rotates it, converts it to grayscale, and applies the selected
    edge detection algorithm with specified parameters.
    """
    try:
        original_image = Image.open(image_file).convert('RGB')

        # Apply rotation if specified
        if rotation_angle != 0:
            original_image = original_image.rotate(rotation_angle, expand=True)

        img_array = np.array(original_image)
        gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        
        # Apply Gaussian blur for Canny
        if algorithm == "Canny":
            blur_kernel = params.get('blur_kernel', 5)
            # Ensure kernel size is odd
            if blur_kernel % 2 == 0:
                blur_kernel += 1
            gray_img = cv2.GaussianBlur(gray_img, (blur_kernel, blur_kernel), params.get('sigma', 0))

        processed_image = None
        if algorithm == "Canny":
            processed_image = cv2.Canny(
                gray_img,
                params.get('threshold1', 50),
                params.get('threshold2', 150),
                apertureSize=params.get('apertureSize', 3)
            )
        elif algorithm == "Sobel":
            ksize = params.get('ksize', 5)
            direction = params.get('direction', 'Both')
            
            sobel_x, sobel_y = None, None
            if direction in ['Both', 'X-axis']:
                sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=ksize)
            if direction in ['Both', 'Y-axis']:
                sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=ksize)

            if direction == 'X-axis':
                processed_image = np.uint8(np.absolute(sobel_x))
            elif direction == 'Y-axis':
                processed_image = np.uint8(np.absolute(sobel_y))
            else: # Both
                processed_image = cv2.bitwise_or(
                    np.uint8(np.absolute(sobel_x)),
                    np.uint8(np.absolute(sobel_y))
                )
        elif algorithm == "Laplacian":
            ksize = params.get('ksize', 3)
            laplacian = cv2.Laplacian(gray_img, cv2.CV_64F, ksize=ksize)
            processed_image = np.uint8(np.absolute(laplacian))

        return original_image, processed_image
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None, None

# --- Sidebar Controls ---
uploaded_file = st.sidebar.file_uploader(
    "Upload Your Image", type=["png", "jpg", "jpeg" , "bmp"]
)

rotation_angle = st.sidebar.selectbox(
    "Rotate Image (in degrees)",
    (270 , 0),
    help="Rotate the uploaded image before processing."
)

selected_algorithm = st.sidebar.selectbox(
    "Choose an Edge Detection Algorithm",
    ("Canny", "Sobel", "Laplacian")
)

params = {}
st.sidebar.markdown("---")
st.sidebar.subheader(f"{selected_algorithm} Parameters")

if selected_algorithm == "Canny":
    params['threshold1'] = st.sidebar.slider("Lower Threshold", 0, 500, 50, help="Lower boundary for edge detection.")
    params['threshold2'] = st.sidebar.slider("Upper Threshold", 0, 500, 150, help="Upper boundary for edge detection.")
    params['apertureSize'] = st.sidebar.selectbox("Kernel Size", [3, 5, 7], help="Aperture size for the Sobel operator.")
    st.sidebar.markdown("<h6>Gaussian Blur Settings</h6>", unsafe_allow_html=True)
    params['blur_kernel'] = st.sidebar.slider("Blur Kernel Size", 1, 21, 5, 2, help="Size of the Gaussian blur kernel (must be odd).")
    params['sigma'] = st.sidebar.slider("Sigma", 0.0, 10.0, 1.4, 0.1, help="Gaussian kernel standard deviation.")

elif selected_algorithm == "Sobel":
    params['ksize'] = st.sidebar.selectbox("Kernel Size", [1, 3, 5, 7], index=2, help="Size of the extended Sobel kernel.")
    params['direction'] = st.sidebar.radio("Gradient Direction", ('Both', 'X-axis', 'Y-axis'), help="The direction of the gradient to detect.")

elif selected_algorithm == "Laplacian":
    params['ksize'] = st.sidebar.selectbox("Kernel Size", [1, 3, 5, 7], index=1, help="Aperture size used to compute the second-derivative filters.")

st.sidebar.markdown("---")
st.sidebar.info("Adjust the controls above to see changes in the processed image.")

# --- Image Display ---
if uploaded_file is not None:
    col1, col2 = st.columns(2)
    original, processed = process_image(uploaded_file, selected_algorithm, params, rotation_angle)

    if original is not None and processed is not None:
        with col1:
            st.image(original, caption="Original Image", use_container_width=True)

        with col2:
            st.image(processed, caption=f"{selected_algorithm} Result", use_container_width=True, channels="GRAY" if processed.ndim == 2 else "RGB")
else:
    st.info("Please upload an image to get started!")
