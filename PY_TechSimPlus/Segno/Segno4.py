import segno
from PIL import Image
qrcode = segno.make('Henry Lee')
qrcode.save('henry-lee.svg')  # SVG document
qrcode.save('henry-lee.png')  # PNG image
qrcode.save('henry-lee.eps')  # EPS document
qrcode.save('henry-lee.txt')  # Text output
qrcode.show()
