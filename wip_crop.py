import cv2
import numpy as np

def crop_im(im):
    """
    Takes cv2 image, im, and padding % as a float, padding,
    and returns cropped image.
    """
    bw = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    rows, cols = bw.shape

    non_empty_columns = np.where(bw.min(axis=1)>0)[0]
    non_empty_rows = np.where(bw.min(axis=0)>0)[0]

    print(cols)
    print(rows)

    padding = cols//rows
    print(padding)
    cropBox = (min(non_empty_rows) * (1 + padding),
                min(max(non_empty_rows) * (1 + padding), rows),
                min(non_empty_columns) * (1 + padding),
                min(max(non_empty_columns) * (1 + padding), cols))
    #(min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

    cropped = im[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 ]
          #      [cropBox[0]: cropBox[1] + 1, cropBox[2]: cropBox[3] + 1,:]

    return cropped

im = cv2.imread('data/ROI_3.png')
cropped1 = crop_im(im)
cv2.imshow('', cropped1)
cv2.waitKey(0)
cv2.destroyAllWindows()
