import facebook
import random

token = input("請輸入使用的token:")  # 所使用的token
version = '2.7'  # 使用的API版本
graph = facebook.GraphAPI(access_token=token,version=version)
object_id = input("要抓取的文章ID:")  # 要抓取的文章ID

#取得按讚的人數
list_likes = []
post = graph.get_object(id=object_id+'?fields=likes.limit(1000)')
likes = post['likes']['data']
print ('共有'+str(len(likes))+'按讚')
for like in likes:
    list_likes.append(like['name'])       
print(list_likes)

#取得有留言的人數
list_comments = []
post = graph.get_object(id=object_id+'?fields=comments.limit(1000)')
comments = post['comments']['data']
print ('共有'+str(len(comments))+'留言')
for comment in comments:
    list_comments.append(comment['from']['name'])
print (list_comments)

#取得有留言和按讚的人數
list_people = []
for p in list_likes:
    if p in list_comments:
        list_people.append(p)        
print ('共有'+str(len(list_people))+'留言和按讚')
print (list_people)

#隨機抽出有留言和按讚的人  
no = random.randint(0,len(list_people)-1)
print("恭喜 {}  抽中!".format(list_people[no]))
