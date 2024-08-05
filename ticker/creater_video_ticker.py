import os
import random

import cv2
import numpy as np


def create_video_ticker(message: str, filename: str, text_color: str, frame_color: str, size: int):
    width, height = size, size
    duration_in_seconds = 3
    fps = 24
    num_frames = duration_in_seconds * fps

    if not os.path.exists("video"):
        os.makedirs("video")
    video_path = os.path.join("video", filename)

    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    frame = np.zeros((height, width, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2

    text_size = cv2.getTextSize(message, font, font_scale, font_thickness)[0]
    
    initial_x = width
    y =  (height + text_size[1]) // 2

    total_displacement = width + text_size[0]
    displacement_per_frame = total_displacement / num_frames

    font_color = get_text_collor(text_color)

    frame_color = get_frame_color(frame_color)

    for i in range(num_frames):
        frame.fill(frame_color)
        x = initial_x - int(displacement_per_frame * i)
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)

    out.release()
    return video_path


def get_text_collor(color: str) -> tuple:
    if color == "white":
        return (255, 255, 255)
    if color == "random":
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        return (0, 0, 0)


def get_frame_color(color: str) -> int:
    if color == "white":
        return 255
    else: 
        return 0
