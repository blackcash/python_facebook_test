#使用python讀取facebook文章中的按讚數,並將從中抽出有留言和按讚的人

1.取得token和要抽取出來的文章<br>
(1)連上facebook開發者平台(https://developers.facebook.com/tools-and-support/)<br>
(2)選取"圖形 API 測試工具",即可取得token <br>
(3)在命令列打"me/posts"即可找出自己所po的文章,在從中找出文章的id <br>
<br>
2.安裝facebook sdk: <br>
       pip install facebook-sdk<br>
<br>
3.程式:<br>
(1)匯入要使用的facebook api : import facebook  <br>
(2)建構使用的物件:graph = facebook.GraphAPI(access_token=token,version=version) <br>
(3)使用物件取得資料(取得有留言且限制1000筆):graph.get_object(id=object_id+'?fields=comments.limit(1000)') <br>
