import json
import os
from ftplib import FTP
FILE_CONFIG = 'config.json'
FOLDER_SE015 = 'SE015'

def upload_file(file_name):
    if not os.path.isfile(file_name):
        ftp.quit()
        print(f'ไม่พบไฟล์ {file_name}')
    else:
        try:
            print('กำลังอัพโหลดไฟล์...')
            ftp.storbinary(f'STOR {file_name}', open(file_name, 'rb'))
        except:
            ftp.quit()
            print(f'อัพโหลดไฟล์ {file_name} ล้มเหลว')
        else:
            ftp.quit()
            print(f'อัพโหลดไฟล์ {file_name} สำเร็จ')
            
try:
    config_file = open(FILE_CONFIG)
except:
    print(f'ไม่พบไฟล์ {FILE_CONFIG}')
else:
    try:
        config = json.load(config_file)
        config_file.close()
        host = config['host']
        username = config['username']
        password = config['password']
    except:
        config_file.close()
        print(f'รูปแบบข้อมูลในไฟล์ {FILE_CONFIG} ไม่ถูกต้อง')
    else:
        try:
            print('กำลังเชื่อมต่อไปยังเซิร์ฟเวอร์ ...')
            ftp = FTP(host)
        except:
            ftp.quit()
            print('การเชื่อมต่อไปยังเซิร์ฟเวอร์ล้มเหลว')
        else:
            print('การเชื่อมต่อไปยังเซิร์ฟเวอร์สำเร็จ')
            try:
                print('กำลังเข้าสู่ระบบ ...')
                ftp.login(user=username, passwd=password)
            except:
                ftp.quit()
                print('ชื่อผู้ใช้หรือรหัสผ่าน ไม่ถูกต้อง')
            else:
                print('การเข้าสู่ระบบสำเร็จ')
                try:
                    ftp.cwd(FOLDER_SE015)
                except:
                    ftp.mkd(FOLDER_SE015)
                    ftp.cwd(FOLDER_SE015)
                finally:
                    student_id = input('กรุณาป้อนรหัสนิสิต: ')
                    try:
                        ftp.cwd(student_id)
                    except:
                        ftp.mkd(student_id)
                        ftp.cwd(student_id)
                    finally:
                        file_name = input('กรุณาป้อนเส้นทางไฟล์ที่ต้องการอัพโหลด: ')
                        upload_file(file_name)
