import qrcode
data = input("Enter URL or text: ").strip()
filename = input("Enter filename (with .png): ").strip()

# Create a QRCode object
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create the image
image = qr.make_image(fill_color='black', back_color='white')

# Save the image
image.save(filename)

print(f"QR code saved as {filename}")
