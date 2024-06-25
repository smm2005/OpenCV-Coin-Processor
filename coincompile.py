from coinconfig import transform, cointable # From the coinconfig python file, the transform function and cointable will be required
import cv2 as cv # Import the OpenCV module as 'cv'
import numpy as np # Import the numpy module as 'np'

file_form = "img/coins{}.jpg" # Standard file format to access images with
prefix = "feed image " # Prefix for the terminal line program
ansi_red = "\033[31m" # ANSI colour code for red
ansi_green = "\033[32m" # ANSI colour code for green
ansi_reset = "\033[0m" # ANSI colour code to reset
testtable = {1: 3.40, 2: 4.90, 3: 6.00, 4: 6.00, 5: 6.50, 6: 2.25, 7: 10.00, 8: 0.40, 9: 1.40, 10: 3.75, 11: 1.0, 12: 1.0, 13: 3, 14: 3.05, 15: 0} # Test table to confirm test amounts are the same as calculated amounts

while True:
    ipt = input(">> ") # Input provided after '>> '. This is where the commands for the coin processing tool are entered.

    if ipt == "quit" or ipt == "q": 
        break 
    # If the user types 'quit' or 'q' then the program will stop executing

    try:
        ipt = ipt.lstrip() # Get rid of any excess spaces from the left side
        ipt = ipt.rstrip() # Get rid of any excess spaces from the right side
        lst = ipt.split(" ") # Split the input into a list (i.e. feed image 4 = ["feed", "image", "4"])
        integer = int(lst[-1]) # Integer that denotes the test image number
        if ipt.startswith(prefix): # If the input has the prefix process the test image
            if integer in range(1, 16): # If the integer is in the range of [1, 15] then a valid image exists.
                amount = 0 # Starting amount
                filename = file_form.format(integer) # Filename formatted based on the integer
                capture = cv.imread(filename) # Capture of the file processed into a MatLike for use by the OpenCV module
                copy = transform(capture) # Transformation function conducted onto the capture
                contours, hierarchy = cv.findContours(copy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # Extracting the contours of the thresholded image (copy)
                for count in contours: # Iterating over each contour
                    (x, y), radius = cv.minEnclosingCircle(count) # Centre and radius of the enclosed circle returned after minimum enclosing circle of each contour is found
                    centre = (int(x), int(y)) # Conversion of centre coordinates to integer
                    radius = int(radius) # Conversion of radius to integer
                    for k, v in cointable.items(): # Iterating over the cointable 
                        if radius in v: # If the radius is in one of the radii ranges then increment the amount by the corresponding "key" (the coin denomination)
                            amount += k
                print("Coins " + str(integer) + " Amount: " + str(round(amount, 2)))
                print("EXPECTED AMOUNT: " + str(testtable.get(integer)))
                if abs(amount - testtable[integer]) <= 0.001: # If the difference in the actual and expected values is less than 0.001, the processed coin amount matches the expected amount
                    print(ansi_green + "*** TEST PASSED ***" + ansi_reset)
                else:
                    print(ansi_red + "** TEST FAILED **" + ansi_reset)
                cv.imshow("Image " + str(integer), capture) # Image displayed on a different window
                cv.waitKey(5000) # Image displayed for 5 seconds: no benefit exists for this
                cv.destroyAllWindows() # After the image has been displayed, the corresponding window closes until another command to open a window has been made 
            else:
                print(ansi_red + "ERROR: Integer not in the range of 1 to 15. Make sure the integer is between 1 to 15" + ansi_reset) # Error where the integer is not between [1, 15]
        else:
            print(ansi_red + "ERROR: Use the prefix \"feed image\" to input an image into the computer vision model" + ansi_reset)
    except:
        print(ansi_red + "ERROR: IMAGE PATH INVALID OR CORRUPTED" + ansi_reset)






