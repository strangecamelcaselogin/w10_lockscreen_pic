import os
import shutil

USER = 'User'
SOURCE = r'C:\Users\{}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'.format(USER)
DEST = r'C:\Users\User\Desktop\Заставки'

try:
    file_list = os.listdir(path=SOURCE)
    
    real_index = 0
    for index, filename in enumerate(file_list):
        src = os.path.join(SOURCE, filename)
        if not os.path.isdir(src) and \
                (os.stat(src).st_size / 1024) > 100:
                    
            real_index += 1
            dst = os.path.join(DEST, 'pic_'+str(real_index) + '.jpg')    
            shutil.copy(src, dst)
            
            print('[ ok ] {}'.format(dst))

except Exception as e:
    print(e)
