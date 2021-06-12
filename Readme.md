# ShortLink
 - 使用Flask+MySQL自行部署短链接生成

# 部署:
 - 需要`Python3`环境以及`Flask`,`pymysql`模块  
 - 需要一个域名和MySQL环境,不再赘述  
 - 创建一个数据库后运行`shortlink.sql`初始化一张表  
 - 填写`connect_settings.py`内相关内容  
 - 完事
 
# 添加/删除链接(手动)
 - 添加:参考`add_link_example.bat`  
 - 删除:手动删数据库吧  
 (后续会添加API添加方式)
  
# 添加/删除链接(API)
访问
```
http://您的链接/api?参数
```
|参数|描述|必填|备注|
|:-:|:-:|:-:|:-:|
|key|访问秘钥|Yes|您在`connect_settings.py`中设置的key|
|type|操作方式|Yes|仅可填写`add`或`del`|
|link|想操作的链接|Yes|`type`为`add`时,填入网址<br>`type`为`del`时,填入短链接后缀或者完整短链接|
|creator|链接创建者|No|记录创建者<br>仅当`type`为`add`时有效|
|from|链接创建者来源|No|记录创建者来源(群号,网站等)<br>仅当`type`为`add`时有效|

最后得到像下面的链接
```
http://127.0.0.1:5000/api?key=QnuGfefJIhuGYUF84&type=del&link=sicr
http://127.0.0.1:5000/api?key=QnuGfefJIhuGYUF84&type=del&link=http://myweb.site/sicr
http://127.0.0.1:5000/api?key=QnuGfefJIhuGYUF84&type=add&link=http://www.baidu.com&creator=123&from=qwq
```