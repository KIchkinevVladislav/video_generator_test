import os
import random

import cv2
import numpy as np


def create_video_ticker(message: str, filename: str, text_color: str, frame_color: str, size: int):
    width, height = size, size
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

    font_color = get_text_collor(text_color)

    frame_color = get_frame_color(frame_color)

    for i in range(72):
        frame.fill(frame_color)
        x -= int((width + text_size[0]) / 72)
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)

    out.release()
    return video_path


def get_text_collor(color: str) -> tuple:
    if color == 'white':
        return (255, 255, 255)
    if color == 'random':
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        return (0, 0, 0)


def get_frame_color(color: str) -> int:
    if color == 'white':
        return 255
    else: 
        return 0
