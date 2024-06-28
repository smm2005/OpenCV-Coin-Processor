**DESCRIPTION**

This project is a coin processor coded solely with the Python programming language that uses the NumPy and, most importantly, OpenCV. The interface of this project solely utilizes the command line interface (i.e. no proper GUI).
The project consists of a configuration image to denote the range of radii each coin possesses and 15 test images to extract coins based
on whether their radius was within a specific range of radii for each respective coin denomination.

The coin denominations present in the Canadian currency are:
- Toonie: $2
- Loonie: $1
- Quarter: $0.25
- Dime: $0.10
- Nickel: $0.05

And no two coins are the same size, a key fact when it comes to identifying the coins present in the test images.

This project was **NOT** made with user interaction in mind however users are free to try out the coin processor themselves just as long as
the following requirements are met

- Users have "OpenCV" and "NumPy" installed. If not, users can do this with `pip install numpy` and `pip install opencv-contrib-python`
- **NO** test image **NOR** the configuration image in this repository is manipulated in any way.

--------------------------------------------------------------------------------------------------------------

**FEEDING IMAGES INTO THE PROCESSOR**

To feed test images into the coin processor, right click on the folder where the python files resides and then select `Open in Terminal`. Once you are on the terminal, type the following command

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/6ae5e89b-57b8-484b-97b5-fff519742615)

**IMPORTANT: DO NOT TYPE `python coinconfig.py` because there will be no opportunity to feed test images as all the functionalities to feed test images are on the `coincompile.py` file**

Next, there will be an input prompt that starts off with `>> `. You are expected to type `feed image ` as a prefix followed by a number between 1-15 inclusive. There are errors that exist if you type something that does
not start with `feed image`, if you enter a number beyond the range of 1-15 inclusive or if you type an unprocessable command.

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/68943f79-b0dd-4775-80c3-5b8684ca515f)

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/84cf4e84-7706-46de-a9c9-9c5bbc1396c1)

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/625362cf-a8b5-4098-b36f-7af66053f89f)

Once you type a real command like `feed image 4`, the terminal will output the amount processed in the image followed by the expected amount. If the expected amount equals the processed amount then, in green, there will be
a display that says `**TEST PASSED**`. Otherwise, there will be a display that says `**TEST FAILED**`.

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/881a02d0-1233-4f4e-84ac-6fddb5f3123e)

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/f4346985-f824-4bad-8d39-3e3596523040)

In addition to the output from the terminal, there will also be an output of the test image which will be up for display for 5 seconds. There is no inherent benefit to this feature but it's nice if users want to confirm for themselves if the test amounts match the processed amounts.

--------------------------------------------------------------------------------------------------------------
**PROCESS**

The extraction and assignment of coins from the test images to their specified coin denominations occured in the following steps:

- Gaussian blur (convolution) to reduce the presence of noise in the image
- Adaptive thresholding for edge detection
- Morphological transformation that closes the circular shape. This too also reduces the presence of noise in the thresholded image.
- Contouring to identify viable outlines present in the thresholded image
- Determining the minimum enclosing circle that surrounds the contours

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/45b0d847-da16-4c74-a001-732856915534)

![image](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/a042182c-e0f7-473e-88b3-6705492b72f4)


--------------------------------------------------------------------------------------------------------------

**ENVIRONMENT SETUP**

For my coin processor to work, the camera had to be in it's exact position so as to have the radii of the coins in the test images match up with the radii of the coins in the configuration image. Additionally, the backdrop for the coins has to comprise of solely one colour, so I decided to lay the coins on a white poster board. Ultimately, the environment for the coin processor looked like this...

![20240625_110836](https://github.com/smm2005/OpenCV-Coin-Processor/assets/70491113/9f1d5042-5a27-4191-bf8f-3ada3c0676c5)

The paper is there to prevent any reflection from the drawer since the reflection will produce false results for the coin processor.

