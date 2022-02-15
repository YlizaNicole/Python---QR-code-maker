#Contact Tracing App
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read


from datetime import datetime
import sys
import numpy as np
import cv2
from pyzbar.pyzbar import decode

sys.stdout = open("test.txt", "w")

#adding date stamp
dateTimeObj = datetime.now()
print(dateTimeObj)

# setting up cam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# setting up detector
detector = cv2.QRCodeDetector()
while True:
    success, img = cap.read()
    # detect and decode
    for barcode in decode (img):
        print (barcode.data)
        myData= barcode.data.decode ('utf-8')
        print (myData)
        pts= np.array ([barcode.polygon], np.int32)
        pts = pts.reshape ((-1,1,2))
        cv2.polylines(img, [pts], True, (65, 105, 255),5 )
    #result
 
    cv2.imshow('Scan Qrcode here', img)    
    if cv2.waitKey(1) == ord("q"):
        break

    #save as text file
sys.stdout.close()

