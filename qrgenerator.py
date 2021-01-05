import qrcode

target = input("Enter the url for which you want to generate qr code")
qr = qrcode.make(target)
name = input('Enter the name for the file (image of you your QR code): ')
qr.save(name+".png", "PNG")
