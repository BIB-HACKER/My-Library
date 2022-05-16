import qrcode

img = qrcode.make("https://ticker.finology.in/")

img.save("stock reserch.jpg")





# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('9134431264')
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
