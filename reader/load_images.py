import cv2
import glob


class getImages:
    images = [cv2.imread(file) for file in glob.glob('./Images/*.jpg')]
    expected = cv2.imread('./desired/orange.jpg')
