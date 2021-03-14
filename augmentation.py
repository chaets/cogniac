import cv2
import numpy as np

class Augmentation:
    """docstring for Augmentation."""

    # def __init__(self):
    #     pass
        # super(Augmentation, self).__init__()
        # self.arg = arg

    def get_resize(image, lengthScale, breadthScale):
        src = cv2.imread(image , cv2.IMREAD_UNCHANGED)
            #calculate the scale percent of original dimensions
        width = int(src.shape[1] * breadthScale / 100)
        length = int(src.shape[0] * lengthScale / 100)
        # dsize
        dsize = (width, length)
        # resize image
        output = cv2.resize(src, dsize)
        return(output)


    def get_crop(image, dim):
        ima = cv2.imread(image)
        if dim == None:
            print(ima.shape[1])
            x = int(ima.shape[0]/2)
            y = int(ima.shape[1]/2)
            cropped = ima[0:x, 0:y]
        else:
            cropped = ima[dim[0]:dim[1], dim[2]:dim[3]]
        return(cropped)

    def get_rotate(image, angle):
        src = cv2.imread(image , cv2.IMREAD_UNCHANGED)
        image_center = tuple(np.array(src.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(src, rot_mat, src.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result
