import cv2
camera = cv2.VideoCapture(0)
ret, frame = camera.read()
if ret:
     cv2.imwrite("spycam.png", frame)

camera.release()
cv2.destroyAllWindows()