import cv2 as cv
import numpy as np

def morph_find(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
    finished = False
    size = np.size(binary)
    skeleton = np.zeros(binary.shape, np.uint8)
    while (not finished):
        eroded = cv.erode(binary, kernel)
        temp = cv.dilate(eroded, kernel)
        temp = cv.subtract(binary, temp)
        skeleton = cv.bitwise_or(skeleton, temp)
        binary = eroded.copy()

        zeros = size - cv.countNonZero(binary)
        if zeros == size:
            finished = True

    contours, hireachy = cv.findContours(skeleton, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0, 0, 255), 1, 8)
    cv.imshow("skeleton", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def thin_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    thinned = cv.ximgproc.thinning(binary)
    contours, hireachy = cv.findContours(thinned, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0, 0, 255), 1, 8)
    cv.imshow("thin", image)
    cv.waitKey(0)
    cv.destroyAllWindows()