import cv2 as cv    # Importing the OpenCV python module as 'cv'
import numpy as np  # Importing the numpy python module as 'np'

coins = [2, 1, 0.25, 0.05, 0.1] # Coin denominations ranked in order of decreasing COIN SIZE
cointable = {}  # Dictionary to store radii range of coin table.
capture = cv.imread("img/coinconfig.jpg") # Image to configurate the coins used in the specific environment

# Transform function for basic thresholding and image mutation
def transform(matlike):
    converted = cv.cvtColor(matlike, cv.COLOR_BGR2GRAY) # Image is converted to grayscale
    blurred = cv.GaussianBlur(converted, (17, 17), 0) # Convolution (gaussian blurring the image) applied to the converted grayscale image. This reduces noise present in the image
    thres = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2) # Adaptive thresholding applied to the blurred image
    kernel = np.ones((5, 5), np.uint8) 
    closing = cv.morphologyEx(thres, cv.MORPH_CLOSE, kernel, iterations=3) # Morphological transformation of contours closing in on the coin thresholds.
    new = closing.copy() # Copy of transformed image is created and then returned.
    return new

copy = transform(capture) # Copy of transformed image assigned a variable
contours, hierarchy = cv.findContours(copy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # Contours looked for in the transformed image
for count in contours: 
    (x, y), radius = cv.minEnclosingCircle(count) # Centre and radius of the enclosed circle returned after minimum enclosing circle of each contour is found
    centre = (int(x), int(y)) # Conversion of centre coordinates to integer
    radius = int(radius) # Conversion of radius to integer
    curr = coins.pop() # Pop the last element. Every last value in coins attributed to every coin smallest in size than the next one.
    cointable.update({curr: list(range(radius-2, radius+3))}) # Cointable updated with the coin denomination referring it's respective radii range.
    cv.circle(capture, centre, radius, (0, 255, 0), 3) # Circle drawn over each coin in the coinconfig file.
        
