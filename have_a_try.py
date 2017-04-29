import cv2 as cv
from cv2 import imshow, imread, waitKey
import util


title='An Awesome Image'
def show_image(img):
    imshow(title, img)
    waitKey(0)

img=imread('images/sample7-1.bmp')
show_image(img)
img_sketch=util.sketch_cvt(img)
show_image(img_sketch)



