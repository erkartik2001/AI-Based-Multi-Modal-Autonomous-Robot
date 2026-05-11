import cv2

url = "rtsp://192.168.1.4:1945/"

cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

while True:

    ret, frame = cap.read()

    if not ret:
        print("frame failed")
        break

    cv2.imshow("Feed", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()