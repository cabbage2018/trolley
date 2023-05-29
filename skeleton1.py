##pip install opencv-contrib-python
##pip install skimage
##
from skimage import morphology
import numpy as np
import cv2 as cv

def skeleton_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    binary[binary == 255] = 1
    skeleton0 = morphology.skeletonize(binary)
    skeleton = skeleton0.astype(np.uint8) * 255
    cv.imshow("skeleton", skeleton)
    cv.waitKey(0)
    cv.destroyAllWindows()


def medial_axis_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    binary[binary == 255] = 1
    skel, distance = morphology.medial_axis(binary, return_distance=True)
    dist_on_skel = distance * skel
    skel_img = dist_on_skel.astype(np.uint8)*255
    contours, hireachy = cv.findContours(skel_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0, 0, 255), 1, 8)

    cv.imshow("result", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
