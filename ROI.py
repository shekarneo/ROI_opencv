import cv2

image = cv2.imread('D:\PDF2IMG\ROI.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(gray, (5,5), 0)
#thresh = cv2.threshold(blur,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 5)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
cnts = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

ROI_number = 0
for c in cnts:
    area = cv2.contourArea(c, True)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx) == 4 and (area > 1000) and (area < 80000):
        ROI = image[y:y+h, x:x+w]
        cv2.imwrite('D:\PDF2IMG\ROI_{}.png'.format(ROI_number), ROI)
        ROI_number += 1

#cv2.imshow('thresh', thresh)
#cv2.imshow('opening', opening)
cv2.waitKey()
cv2.destroyAllWindows()
