import segno
from PIL import Image

qrcode = segno.make('Yellow Submarine', error='h')
img = qrcode.to_pil(scale=3).rotate(45, expand=True)
img.save('yellow-submarine-rotated.png')
img.show()