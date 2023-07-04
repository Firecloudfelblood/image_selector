import cv2
from matplotlib import pyplot as pltd

class searchObject:
    def compare(images, expected):

        xml_data = cv2.CascadeClassifier('../Haars/XML-data.xml')

        img_gray = cv2.cvtColor(expected, cv2.COLOR_BGR2GRAY)
        imaging_rgb = cv2.cvtColor(expected, cv2.COLOR_BGR2RGB)

        pltd.subplot(1,1,1)
        pltd.imshow(imaging_rgb)
        pltd.show()
        found = xml_data.detectMultiScale(img_gray, minSize=(30, 30))
        print('hello')

