"""
@Harsha
Simple bar code detector based on the concept that the barcodes generally
have larger gradients in xdir than in ydir.
"""

import cv2
import numpy as np

VIDEO_PATH = ""
IMG_PATH = "./barcode_01.jpg"


def show_image(image, image_name):
    """"
    Utility fn used during debugging for intermediate img displays
    """
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)


def detect_barcode(frame):
    """
    Args :
        frame : Image frame
    Returns:
    """
    gradX = cv2.Sobel(frame, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(frame, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    show_image(gradient, "gradient")

    blurred = cv2.blur(gradient, (9, 9))
    show_image(blurred, "blur")

    (_, thresh) = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)
    show_image(thresh, "thresh")
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    closed_gray = cv2.cvtColor(closed, cv2.COLOR_BGR2GRAY)
    show_image(closed_gray, "gray_closed")
    (img2, cnts, _) = cv2.findContours(closed_gray.copy(), cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)


if __name__ == "__main__":
    ret = True
    if VIDEO_PATH:  # check if not empty and valid path
        while ret:
            vid = cv2.videoCapture(VIDEO_PATH)
            ret, frame = vid.read()
            detect_barcode(frame)
    elif IMG_PATH:
        frame = cv2.imread(IMG_PATH, 1)
        detect_barcode(frame)
    else:
        print("Image and video path not valid")
