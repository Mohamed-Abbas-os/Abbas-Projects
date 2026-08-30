import cv2
file=r'my_qrcode.png'
image=cv2.imread(file)
if image is None:
    print('no image')
else:
    cv2.imshow('QR Code',image)
    qr_det=cv2.QRCodeDetector()
    data,points,_=qr_det.detectAndDecode(image)
    if data :
        print('decoded data:',data)
    else:
        print('no qr detected')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
