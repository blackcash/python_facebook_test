import requests
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse
import facebook
import shutil
import simplejson

group_id = input("請輸入社團的ID:")
token =  input("請輸入使用的token:")
version = '2.7'  # 使用的API版本
graph = facebook.GraphAPI(access_token=token,version=version)

#獲取API內容

url_adr = 'https://graph.facebook.com/v'+version+'/{}/feed?access_token={}'.format(group_id, token)
print (url_adr)
res = requests.get(url_adr)

#使用迴圈爬取並放到list

posts = []
for post in res.json()['data']:
    #posts.append([parse(post.get('created_time')[0:19]), post.get('id'), post.get('message'), post.get('story')])
    posts.append([parse(post.get('created_time')[0:19]), post.get('id'), post.get('message')])
    object_id = post.get('id')
    try:
        picb = graph.get_object(id=object_id+'?fields=full_picture')
        print (type(picb),picb)
        if 'full_picture' in picb.keys():
            print (picb['full_picture'])
            res = requests.get(picb['full_picture'] , stream = True)
            f = open("B"+post.get('id')+".jpg",'wb')
            shutil.copyfileobj(res.raw,f)
        else:
            print(object_id+"沒有大圖片資料")

        pics = graph.get_object(id=object_id+'?fields=picture')    
        print (type(pics),pics)
        if 'picture' in pics.keys():	   
            print (pics['picture'])
            res = requests.get(pics['picture'] , stream = True)
            f = open("S"+post.get('id')+".jpg",'wb')
            shutil.copyfileobj(res.raw,f)
        else:
            print(object_id+"沒有小圖片資料")
    except:
        print(object_id+"沒有圖片資料")

#輸出內容

df = pd.DataFrame(posts)
#df.columns = ['貼文時間', '貼文ID', '貼文內容', '分享內容']
df.columns = ['貼文時間', '貼文ID', '貼文內容']
df.to_csv('測試.csv', index=False)    