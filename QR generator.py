# import qrcode as qr
# img=qr.make("982333385")
# img.save("SulavTrader.png")

import qrcode

# Replace this URL with the link to your hosted image
image_url = "https://your-image-host-link.com/image.jpg"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(image_url)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode_image_link.png')

print("QR code generated and saved as 'qrcode_image_link.png'.")
