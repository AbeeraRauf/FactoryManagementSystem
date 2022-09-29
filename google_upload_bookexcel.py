import json
import requests
from googleapiclient.http import MediaFileUpload
from Google import Create_Service

def bookExcel():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    ## Replace Existing File on Google Drive
    file_id = '1nDkf_GldeR5RRlyzJ-sRi89J10z9V6GW'

    media_content = MediaFileUpload('book.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    service.files().update(
        fileId=file_id,
        media_body=media_content
    ).execute()
    
def bookExpense():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    ## Replace Existing File on Google Drive
    file_id = '178maODKyZDKKLpe9hbViBnTH-mBp-jWD'

    media_content = MediaFileUpload('book.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    service.files().update(
        fileId=file_id,
        media_body=media_content
    ).execute()