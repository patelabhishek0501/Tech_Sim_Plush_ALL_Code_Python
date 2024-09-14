import segno
from PIL import Image
micro_qrcode = segno.make('Rain', error='q')
micro_qrcode.save('micro_qrode_rain.png', scale=4, dark='darkblue', data_dark='steelblue')
micro_qrcode.show()