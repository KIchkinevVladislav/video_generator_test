import os

import cv2
import numpy as np


def create_video_ticker(message: str, filename: str):
    width, height = 100, 100
    if not os.path.exists('video'):
        os.makedirs('video')
    video_path = os.path.join('video', filename)

    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))

    frame = np.zeros((height, width, 3), dtype=np.uint8)
    text_size = cv2.getTextSize(message, cv2.FONT_HERSHEY_COMPLEX, 1, 2)[0]
    x, y = width, (height + text_size[1]) // 2

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    for i in range(72):
        frame.fill(0)
        x -= int((width + text_size[0]) / 72)
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)

    out.release()
    return video_path
