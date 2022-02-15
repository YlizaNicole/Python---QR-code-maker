#Contact Tracing App
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read




import webbrowser
import cv2

# setting up cam
cap = cv2.VideoCapture(0)
# setting up detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        input=data
        break
    #result
    cv2.imshow("QRCODE scanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break

webscanner=webbrowser.open(str(input))
cap.release()
cv2.destroyAllWindows()