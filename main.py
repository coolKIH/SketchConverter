import cv2
import util
import os

dir_path = "images"
try:
    for filename in os.listdir(dir_path):
        if filename.endswith("jpg") | filename.endswith("png") | filename.endswith("bmp"):
            img_path = os.path.join(dir_path, filename)
            img = cv2.imread(img_path)
            height, width, channels = img.shape
            print height, width, channels
            img = util.resize_cv_image(img,1,1)
            img = util.sketch_cvt(img, kernel_size=(23,23))
            util.show_cv_image(img)
except:
    print 'Unexpected error'
