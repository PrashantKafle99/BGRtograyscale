
#image conversion project into grayscale

import cv2 as cv

path=input("Enter the path of the image")
print( "This is the path that you have entered===",path)

imgs1=cv.imread(path,0)
imgs1=cv.resize(imgs1, (400,400))
cv.imshow("converted image is ===", imgs1)
cv.waitKey(0)
cv.destroyAllWindows()