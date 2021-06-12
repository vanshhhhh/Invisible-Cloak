import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, back = cap.read()
    if ret == True:
        cv2.imshow("image",back)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite("assets/image.jpg",back)
            break
cap.release()
cv2.destroyAllWindows()