import cv2


def dodge(image, mask):
    return cv2.divide(image, 255-mask, scale=256)


def burn(image, mask):
    return 255 - cv2.divide(255-image, 255-mask, scale=256)


def show_cv_image(image, title = "Picture"):
    if image is not None:
        cv2.imshow(title, image)
        cv2.waitKey(0)
    else:
        print 'Which image do you want to convert?'


def sketch_cvt(img_rgb, kernel_size=(21, 21)):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_gray_inv, kernel_size, sigmaX=0, sigmaY=0)
    img_blend = dodge(img_gray, img_blur)
    img_blend = burn(img_blend, img_blur)
    return img_blend


def resize_cv_image(image, x=0.5, y=0.5):
    return cv2.resize(image, (0, 0), fx=x, fy=y)