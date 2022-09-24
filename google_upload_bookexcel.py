import json
import requests
headers = {"Authorization": "Bearer ya29.a0Aa4xrXM9bzPVDohgqLy7iQBcy96Z5aMrh1jdctEwmyM34tkhFSVGFZRsYGxsCxS35A6XinaMef0PwZJwKXeEn3CCEuaXTvMT49qKhNPWHWYRIDl-O-qxwzjb6oOs-W0EZ2m8dACepD0PzhbEB4pvoHjY5omKaCgYKATASARASFQEjDvL9CSLroRtAXP3KZePHYjp2Uw0163"}
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