import cv2
# THIS IS MY WEBCAM
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read() #HERE IS SIMPLY READING FROM MY WEBCAM
    #IF RET IS TRUE i.e. Reading is sucessful
    if ret:
        # back is what the camera is reading
        cv2.imshow("image", back)
        #Wait for 5 ms
        if cv2.waitKey(5) == ord('q'):#unicode value of q
            # save the image
            cv2.imwrite('C:/Users/hp/Desktop/image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
