import os
from os import path
import shutil


USER = ''  # Windows username
SOURCE = r'C:\Users\{}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'.format(USER)  # Let stay as is
DEST = r'C:\Users\{}\Desktop\Заставки'.format(USER)  #  Destination path
MIN_FILE_SIZE = 100 * 1024  # 100kb by default


if not path.isdir(DEST):
    os.mkdir(DEST)

real_index = 0
for filename in os.listdir(path=SOURCE):
    src = path.join(SOURCE, filename)
    if not path.isdir(src) and os.stat(src).st_size > MIN_FILE_SIZE:
        dst = path.join(DEST, 'pic_' + str(real_index) + '.jpg')
        
        shutil.copy(src, dst)

        real_index += 1
        print('[ ok ] {}'.format(dst))