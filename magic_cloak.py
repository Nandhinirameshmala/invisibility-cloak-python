import cv2
import numpy as np
import time

video_output = "output.avi"
fps = 20

COLOR_RANGES = [
    ([0, 120, 70], [10, 255, 255]),
    ([170, 120, 70], [180, 255, 255])
]

cap = cv2.VideoCapture(0)
time.sleep(3)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_output, fourcc, fps, (frame_width, frame_height))

background = None
for i in range(60):
    ret, frame = cap.read()
    if ret:
        background = frame
if background is None:
    cap.release()
    out.release()
    exit()
background = np.flip(background, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = None
    for lower, upper in COLOR_RANGES:
        lower_np = np.array(lower)
        upper_np = np.array(upper)
        temp_mask = cv2.inRange(hsv, lower_np, upper_np)
        mask = temp_mask if mask is None else mask + temp_mask

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7,7), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((7,7), np.uint8))
    mask = cv2.GaussianBlur(mask, (7,7), 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask_filtered = np.zeros_like(mask)
    for cnt in contours:
        if cv2.contourArea(cnt) > 1000:
            cv2.drawContours(mask_filtered, [cnt], -1, 255, -1)
    mask = mask_filtered

    mask_inv = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    res2 = cv2.bitwise_and(background, background, mask=mask)
    final = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Red Disappear Magic", final)
    out.write(final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
