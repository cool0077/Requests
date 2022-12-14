import requests as req
import json
from openpyxl import Workbook


wb = Workbook()
ws = wb.active

title = ['課名', '作者', '價格']
ws.append(title)

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

for index in range(37):
    url = 'https://api.hahow.in/api/courses?limit=24&page=0&sort=NUM_OF_STUDENT&status=PUBLISHED'
    url = url + str(index)
    print(url)
    r = req.get(url, headers = header)
    print(r)
    
    root_json = r.json()
    
    for data in root_json["data"]:
        course = []
        course.append(data['title'])
        course.append(data['owner']['name'])      
        course.append(data['price'])
        ws.append(course)

wb.save('data.xlsx')