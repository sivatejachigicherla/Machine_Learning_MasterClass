#importing the opencv module  
#import cv2
import cv2

# using imread('path') and 0 denotes read as  grayscale image  
img = cv2.imread(r'C:\Users\shiva teja\Desktop\opencv.jpeg',-1) 
print(img) 
  
#This is using for display the image  
cv2.imshow('image',img)  
  
#cv2.waitKey(5000) # This is necessary to be required so that the image doesn't close immediately.  
k = cv2.waitKey(0)
if k == 27:                   # 27 is the code for esc key 
    cv2.destroyAllWindows() 
elif k == ord('a'):
    cv2.imwrite(r'C:\Users\shiva teja\Desktop\copy.jpeg',img)

