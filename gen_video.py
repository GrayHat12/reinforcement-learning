import cv2
import os


def make_video():
    # windows:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Linux:
    #fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    out = cv2.VideoWriter('videos/qlearn-10000.avi', fourcc, 30.0, (1200, 900))

    for i in range(0, 10000, 10):
        img_path = f"qtable_charts/q-10000/{i}.png"
        print(img_path)
        frame = cv2.imread(img_path)
        out.write(frame)

    out.release()


make_video()