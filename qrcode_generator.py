import qrcode
qr_code='hello this is my qr code'
data=qrcode.make(qr_code)
data.save('qrcode1.png')
print('qr code is saved ')