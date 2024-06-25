import cv2 as cv
import numpy as np

coins = [2, 1, 0.25, 0.05, 0.1]
cointable = {}
capture = cv.imread("img/coinconfig.jpg")

def transform(matlike):
    converted = cv.cvtColor(matlike, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(converted, (17, 17), 0)
    thres = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
    kernel = np.ones((5, 5), np.uint8)
    closing = cv.morphologyEx(thres, cv.MORPH_CLOSE, kernel, iterations=3)
    new = closing.copy()
    return new

copy = transform(capture)
contours, hierarchy = cv.findContours(copy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for count in contours:
    (x, y), radius = cv.minEnclosingCircle(count)
    centre = (int(x), int(y))
    radius = int(radius)
    curr = coins.pop()
    cointable.update({curr: list(range(radius-2, radius+3))})
    cv.circle(capture, centre, radius, (0, 255, 0), 3)
        
