import os 
import sys
import shutil
import ntpath
import time
from datetime import date,datetime
 
DIRECTORIES = { 
    "HTML": [".html5", ".html", ".htm", ".xhtml"], 
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
               ".heif", ".psd"], 
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
               ".qt", ".mpg", ".mpeg", ".3gp"], 
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                  "pptx"], 
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
                 ".dmg", ".rar", ".xar", ".zip"], 
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
    "PLAINTEXT": [".txt", ".in", ".out"], 
    "PDF": [".pdf"], 
    "PYTHON": [".py"], 
    "XML": [".xml"], 
    "EXE": [".exe"], 
    "SHELL": [".sh"]  
} 
  
FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats}

def junkOrganizer(basis):
    inputFilePath = os.getcwd()
    if(basis =='ext'):
        for eachFile in os.scandir(): 
            if not eachFile.is_dir():
                filePath = os.path.abspath(eachFile)
                fileExtension = os.path.splitext(filePath)[1].lower()
                if fileExtension in FILE_FORMATS:
                    destParentFolder = os.path.join(inputFilePath,"organizer")
                    if not os.path.exists(destParentFolder):
                        os.mkdir(destParentFolder)
                    destFolder = os.path.join(destParentFolder,FILE_FORMATS[fileExtension])
                    if not os.path.exists(destFolder):
                        os.mkdir(destFolder)
                    shutil.copy2(filePath,destFolder)
                    Destination = os.path.join(destFolder,eachFile)
                    if os.path.exists(Destination):
                        os.remove(filePath)

    if(basis == 'size'):
        for eachFile in os.scandir():
            if not eachFile.is_dir():
                filePath = os.path.abspath(eachFile)
                size = os.stat(eachFile).st_size
                destParentFolder = os.path.join(inputFilePath,"organizer")
                if not os.path.exists(destParentFolder):
                    os.mkdir(destParentFolder)
                if 0<=size<=100 :
                    destFolder = os.path.join(destParentFolder,"SMALL")
                    if not os.path.exists(destFolder):
                        os.mkdir(destFolder)
                    shutil.copy2(filePath,destFolder)
                    Destination = os.path.join(destFolder,eachFile)
                    if os.path.exists(Destination):
                        os.remove(filePath)
                elif 100<size<=1000:
                    destFolder = os.path.join(destParentFolder,"MEDIUM")
                    if not os.path.exists(destFolder):
                        os.mkdir(destFolder)
                    shutil.copy2(filePath,destFolder)
                    Destination = os.path.join(destFolder,eachFile)
                    if os.path.exists(Destination):
                        os.remove(filePath)
                elif 1000<size<=16000:
                    destFolder = os.path.join(destParentFolder,"LARGE")
                    if not os.path.exists(destFolder):
                        os.mkdir(destFolder)
                    shutil.copy2(filePath,destFolder)
                    Destination = os.path.join(destFolder,eachFile)
                    if os.path.exists(Destination):
                        os.remove(filePath)
                elif 16000<size<=128000:
                    destFolder = os.path.join(destParentFolder,"HUGE")
                    if not os.path.exists(destFolder):
                        os.mkdir(destFolder)
                    shutil.copy2(filePath,destFolder)
                    Destination = os.path.join(destFolder,eachFile)
                    if os.path.exists(Destination):
                        os.remove(filePath)
                elif size>128000:
                    destFolder = os.path.join(destParentFolder,"GIGANTIC")
                    if not os.path.exists(destFolder):
                        os.mkdir(destFolder)
                    shutil.copy2(filePath,destFolder)
                    Destination = os.path.join(destFolder,eachFile)
                    if os.path.exists(Destination):
                        os.remove(filePath)
    elif(basis=='alpha'):
        for eachFile in os.scandir():
            if not eachFile.is_dir():
                filePath = os.path.abspath(eachFile)
                destParentFolder = os.path.join(inputFilePath,"organizer")
                if not os.path.exists(destParentFolder):
                    os.mkdir(destParentFolder)
                head, tail = ntpath.split(filePath)
                alp = tail[0].upper()
                destFolder = os.path.join(destParentFolder,alp)
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
                Destination = os.path.join(destFolder,eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)

    elif(basis == 'date'):
        date_format = "%m/%d/%Y"
        today = date.today().strftime('%m/%d/%Y')
        a = datetime.strptime(today, date_format)
        for eachFile in os.scandir():
            if not eachFile.is_dir():
                filePath = os.path.abspath(eachFile)
            destParentFolder = os.path.join(inputFilePath,"organizer")
            if not os.path.exists(destParentFolder):
                os.mkdir(destParentFolder)
            file_date = time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(filePath)))
            b = datetime.strptime(file_date, date_format)
            days = (a-b).days
            if days==0:
                destFolder = os.path.join(destParentFolder,"Today")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            elif days == 1:
                destFolder = os.path.join(destParentFolder,"Yesterday")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            elif 1<days<=7:
                destFolder = os.path.join(destParentFolder,"This_Week")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            elif 7<days<=14:
                destFolder = os.path.join(destParentFolder,"Last_Week")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            elif 14<days<=31:
                destFolder = os.path.join(destParentFolder,"This_Month")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            elif 31<days<=62:
                destFolder = os.path.join(destParentFolder,"Last_Month")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            elif 62<days<=365:
                destFolder = os.path.join(destParentFolder,"This_Year")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            elif 365<days:
                destFolder = os.path.join(destParentFolder,"Long_Time")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath,destFolder)
            Destination = os.path.join(destFolder,eachFile)
            if os.path.exists(Destination):
                os.remove(filePath)
            



basis = sys.argv[1]
junkOrganizer(basis)