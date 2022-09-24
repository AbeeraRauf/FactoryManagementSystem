import json
import requests

def bookExcel():
    headers = {"Authorization": "Bearer ya29.a0Aa4xrXPSMLfsRTE_UCp6H7rXhQ0jaAoDlV2-4_nRbIvIxkflOo4xaUar0szqlH9esuFbT8wQCOcszEy7syF_UFXa6HF6pyjBUvjLJiE5gza8v_x8Mz9FcXK28P7EKBh-F12ZwbFaqq1uz-PyBNU_XMbX2DodaCgYKATASARISFQEjDvL9CZIFqn8q2T5KoWnViJhBow0163"}
    para = {
        "name": "book.xlsx",
        "parents": ["1QAxCY94S-IbQ7jxwQOYZu44Nld8-eARr"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./book.xlsx", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    
def bookExpense():
    headers = {"Authorization": "Bearer ya29.a0Aa4xrXPSMLfsRTE_UCp6H7rXhQ0jaAoDlV2-4_nRbIvIxkflOo4xaUar0szqlH9esuFbT8wQCOcszEy7syF_UFXa6HF6pyjBUvjLJiE5gza8v_x8Mz9FcXK28P7EKBh-F12ZwbFaqq1uz-PyBNU_XMbX2DodaCgYKATASARISFQEjDvL9CZIFqn8q2T5KoWnViJhBow0163"}
    para = {
        "name": "BookExpense.xlsx",
        "parents": ["1QAxCY94S-IbQ7jxwQOYZu44Nld8-eARr"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./BookExpense.xlsx", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )