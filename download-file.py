import json
from ftplib import FTP
FILE_CONFIG = 'config.json'

def download_file(file_name):
    try:
        local_file = open(file_name, 'wb')
    except:
        print(f'พื้นที่จัดเก็บสำหรับไฟล์ {file_name} ไม่เพียงพอ')
    else:
        try:
            ftp.retrbinary(f'RETR {file_name}', local_file.write, 1024)
        except:
            print(f'ไม่มีไฟล์ {file_name} ในเซิร์ฟเวอร์')
        else:
            ftp.quit()
            print(f'ดาวน์โหลดไฟล์ {file_name} สำเร็จ')
        finally:
            local_file.close()
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
                file_name = input('กรุณาป้อนเส้นทางไฟล์ที่ต้องการดาวน์โหลด: ')
                download_file(file_name)
