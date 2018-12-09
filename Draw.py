#importing libraries
import cv2
import numpy as np

#global variables
drawing = False # true if mouse is pressed
mode = '' # to toggle between line, circle, rectangle, eraser
ix,iy = -1,-1

#function for callback of trackbar
def nothing(x):
    pass

#calculating radius of circle
def dist(x1,y1,x2,y2):   
    return int(np.sqrt((np.sum((x2-x1)**2)+np.sum((y2-y1)**2))/4))

# mouse callback function
def draw(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        if mode == 's':
            img[:] = [b,g,r] 
    
    elif event == cv2.EVENT_MOUSEMOVE:
         if drawing == True:
             if mode == 'e':
                 cv2.circle(img,(x,y),20,[0,0,0],-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        iix,iiy = x,y
        if mode == 'r':
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),1)
        elif mode == 'c':
            cv2.circle(img,(int((iix+ix)/2),int((iiy+iy)/2)),dist(ix,iy,iix,iiy),(b,g,r),1)
        elif mode == 'e':
            cv2.circle(img,(x,y),20,(0,0,0),-1)
        elif mode == 'l':
            cv2.line(img,(ix,iy),(iix,iiy),(b,g,r),1)
        else:
            nothing
            
#creating a paint window         
img = np.zeros((600,800,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'):
        mode = 'r'
    elif k == ord('c'):
        mode = 'c'
    elif k == ord('e'):
        mode = 'e'
    elif k == ord('l'):
        mode = 'l'
    elif k ==ord('s'):
        mode = 's'
    elif k == 27:
        break
    
    # get current positions of trackbars
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    
    #bgr display
    img[-40:-15,-40:-15] = [0,0,r]
    img[-40:-15,-80:-55] = [0,g,0]
    img[-40:-15,-120:-95] = [b,0,0]
    
    #all texts
    cv2.putText(img,'Paint with OpenCV',(260,40),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
    cv2.putText(img,'B',(685,545),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,cv2.LINE_AA)
    cv2.putText(img,'G',(725,545),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),0,cv2.LINE_AA)
    cv2.putText(img,'R',(765,545),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),0,cv2.LINE_AA)

    
cv2.destroyAllWindows()