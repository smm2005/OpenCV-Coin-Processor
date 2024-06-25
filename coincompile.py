from coinconfig import transform, cointable
import cv2 as cv
import numpy as np

file_form = "img/coins{}.jpg"
prefix = "feed image "
ansi_red = "\033[31m"
ansi_green = "\033[32m"
ansi_reset = "\033[0m"
testtable = {1: 3.40, 2: 4.90, 3: 6.00, 4: 6.00, 5: 6.50, 6: 2.25, 7: 10.00, 8: 0.40, 9: 1.40, 10: 3.75, 11: 1.0, 12: 1.0, 13: 3, 14: 3.05, 15: 0}

while True:
    ipt = input(">> ")

    try:
        ipt = ipt.lstrip()
        ipt = ipt.rstrip()
        lst = ipt.split(" ")
        integer = int(lst[-1])
        if ipt.startswith("feed image "):
            if integer in range(1, 16):
                amount = 0
                filename = file_form.format(integer)
                capture = cv.imread(filename)
                copy = transform(capture)
                contours, hierarchy = cv.findContours(copy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                for count in contours:
                    (x, y), radius = cv.minEnclosingCircle(count)
                    centre = (int(x), int(y))
                    radius = int(radius)
                    for k, v in cointable.items():
                        if radius in v:
                            amount += k
                print("Coins " + str(integer) + " Amount: " + str(round(amount, 2)))
                print("EXPECTED AMOUNT: " + str(testtable.get(integer)))
                if amount == testtable[integer]:
                    print(ansi_green + "*** TEST PASSED ***" + ansi_reset)
                else:
                    print(ansi_red + "** TEST FAILED **" + ansi_reset)
                cv.imshow("Image " + str(integer), capture)
                cv.waitKey(5000)
                cv.destroyAllWindows()
            else:
                print(ansi_red + "ERROR: Integer not in the range of 1 to 15. Make sure the integer is between 1 to 15")
        else:
            print(ansi_red + "ERROR: Use the prefix \"feed image\" to input an image into the computer vision model" + ansi_reset)
        if ipt == "q" or ipt == "quit":
            break
    except:
        print(ansi_red + "ERROR: IMAGE PATH INVALID OR CORRUPTED" + ansi_reset)






