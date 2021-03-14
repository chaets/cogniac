# import cv2
class Augmentation():
    """docstring for Augmentation."""

    def __init__(self, arg):
        pass
        # super(Augmentation, self).__init__()
        # self.arg = arg

    def get_resize(image, outputpath, lengthScale, breadthScale ):
        src = cv2.imread(image , cv2.IMREAD_UNCHANGED)
        if lengthScale = None and breadthScale = None:
            #percent by which the image is resized
            scale_percent = 50

            #calculate the 50 percent of original dimensions
            width = int(src.shape[1] * scale_percent / 100)
            height = int(src.shape[0] * scale_percent / 100)
        else:
            #percent by which the image is resized
            scale_percent = 50

            #calculate the 50 percent of original dimensions
            width = int(src.shape[1] * breadthScale / 100)
            height = int(src.shape[0] * lengthScale / 100)


        # dsize
        dsize = (width, height)

        # resize image
        output = cv2.resize(src, dsize)
        # D:/cv2-resize-image-50.png

        cv2.imwrite('outputpath',output)

        pass

    def get_crop():
        pass

    def get_rotate():
        pass
