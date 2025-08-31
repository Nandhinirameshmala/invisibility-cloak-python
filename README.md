# Invisibility Cloak Project 🪄

This is my first **OpenCV** project where I recreated Harry Potter’s *invisibility cloak* using **Python**. The program captures live video from a webcam and makes a red-colored object “invisible” by replacing it with the background in real time.

---

## Features

- Real-time webcam video processing
- Detects a specific red-colored object using **HSV color space**
- Applies **masking and morphological operations** to refine detection
- Replaces the detected area with the background to create the invisibility effect
- Saves the output video (optional)

---

## Libraries Used

- **OpenCV (`cv2`)** – For video capture, color detection, masking, and image processing  
- **NumPy (`numpy`)** – For array manipulations and image flipping  
- **time** – To add delays for capturing a clean background  

---

## How It Works

1. Captures the background when no object is in the frame  
2. Reads live frames from the webcam  
3. Converts frames to **HSV color space** for accurate color detection  
4. Detects the red-colored cloak and creates a mask  
5. Applies **morphological operations** and **blur** to remove noise  
6. Segments the cloak and replaces it with the background  
7. Displays the final output and optionally saves it as a video  

---


