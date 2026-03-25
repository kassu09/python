import json
import requests
url = f"https://dummyjson.com/posts"

# API päringu tegemine
response = requests.get(url)
populaarseim = 0
populaarseim_title = ""
views_Kokku = 0
if response.status_code == 200:
    response = requests.get(url)
# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json() 

posts = data['posts']
for i in posts:
    print(i['title'])
    reaktsioonid = (i['reactions']['likes']+i['reactions']['dislikes'])
    if reaktsioonid > populaarseim:
        populaarseim = reaktsioonid
        populaarseim_title = i['title']
print (populaarseim)
print (f"Kõige populaarseim postitus on: {populaarseim_title}")

# for post in posts:
#     views_Kokku += post["views"]
# print(views_Kokku)   

# vaatamised = views_Kokku
# print(vaatamised // 30)