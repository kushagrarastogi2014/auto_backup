import os 
import shutil
import sys
import schedule
from datetime import datetime

from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 

def create_zip(path, file_name):
    try:
        shutil.make_archive(f"archive/{file_name}", 'zip', path)
        return True
    except FileNotFoundError as e:
        return False

def google_auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth) 
    return gauth, drive

def upload_backup(drive, path, file_name):
    f = drive.CreateFile({'parents': [{'id': '1xwBc8T-tQLYmq0JnapiiweNFvamTD91G'}]}) 
    f.SetContentFile(os.path.join(path, file_name))
    f.Upload() 
    f = None

def controller():
    path = r"C:/Users/Kushagra Rastogi/Desktop/gdrive-file-backup-main/backup_me"
    now = datetime.now()
    with open('a.txt', 'a') as file:
        file.write('Recorded at: %s\n' %datetime.now())
    file_name = "backup " + now.strftime(r"%d/%m/%Y %H:%M:%S").replace('/', '-').replace(":","-")

    if  not create_zip(path, file_name):
        sys.exit(0)

    auth, drive = google_auth()
    upload_backup(drive, r"C:\Users\Kushagra Rastogi\Desktop\gdrive-file-backup-main\archive", file_name+'.zip')

if __name__=="__main__":
    schedule.every().day.at("04:04").do(controller)
    while True:
        schedule.run_pending()
