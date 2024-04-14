from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json

#Google Drive Auth

parentsId = '1_frLyHvrKV2tPk4XLRXGeGrOBxiYPVHP'
dirPath = r"C:\Users\OEM\Desktop\files_to_upload"

class File_Metadata:

    def __init__(self, title, parentsId='', filename='txt', mimeType='text/plain'):
        self.file_metadata = {
                'title': title,
                'parents': [{'id': parentsId}],
                'filename': filename,
        }

    def SetTitle(self, title):
        self.file_metadata['title'] = title
    def SetParentsId(self,parentsId):
        self.file_metadata['parents'] = [{'id': parentsId}]

    def GetFileMetaData(self):
        return self.file_metadata


def main():
    gAuth = GoogleAuth(settings_file='config/settings.yaml')
    gAuth.LocalWebserverAuth()
    drive = GoogleDrive(gAuth)

    directory = {
        "dir": r"C:\Users\OEM\Desktop\files_to_upload",
        "sendedFiles": [{
            "name": "",
            "modificationDate": ""
        }]
    }

    fileD = File_Metadata('title')

    print(os.listdir(dirPath))

    for file in os.listdir(dirPath):
        title, type = file.split(".")
        file_metadata = File_Metadata(title, parentsId, type)

        dFile = drive.CreateFile(file_metadata.GetFileMetaData())
        #print(dFile)
        dFile.SetContentFile(os.path.join(dirPath,file))
        dFile.Upload()

        print(title, type)
        print(dirPath)






    # Get File listed
    #folders = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

    # for folder in folders:
    #     if folder['id'] == parentsId:
    #         print('title: %s, id: %s' % (folder['title'], folder['id']));
    #         #file_metadata['parents'] = [{'id': folder['id']}]
    #         fileD.SetParentsId(folder['id'])
    #         file = drive.CreateFile(fileD.GetFileMetaData()) #{'parents': [{'id': folder['id']}]})
    #         file.SetContentString('Testing content file')
    #         file.Upload()

main()
