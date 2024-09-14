import segno
from PIL import Image
qrcode = segno.make("https://66902cffbd7c2027de422e3d--storied-swan-8d9083.netlify.app/")
qrcode.save("Abhi.png",scale=10,light="pink")
print("QR code is a generated")
image = Image.open("Abhi.png")
image.show()

