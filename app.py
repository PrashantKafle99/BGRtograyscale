import cv2 as cv 
import os

#image conversion project into grayscale
def extract_directory_path(file_path):
    return os.path.dirname(file_path)



path=input("Enter the path of the image:--   ")
print( "This is the path that you have entered===",path)
save_directory_path= extract_directory_path(path)
final_save = os.path.join(save_directory_path, "output111.png")
print("save path is", final_save)
print('''Please Enter s (small  to "save" the output on same directory)''')

imgs=cv.imread(path,0)
imgs=cv.resize(imgs, (400,400))
cv.imshow("converted image is ===", imgs)

k=cv.waitKey(0)
if k==115:
   cv.imwrite(final_save,imgs)
else:
    cv.destroyAllWindows()
cv.destroyAllWindows()
