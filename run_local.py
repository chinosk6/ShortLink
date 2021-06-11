import random
import string
from flask import Flask,g,redirect,url_for
from flask import render_template,request,flash
import time
import sqlite3
import os.path
import connect_settings as set
import Connect_MySQL

app = Flask(__name__)


key = random.sample(string.ascii_letters + string.digits, 8)
app.secret_key=str(key)

 #= 'C:/Users/Y7000/Desktop/sdk_v2.6.5/flask/test/FlaskWebProject1/FlaskWebProject1/database/test.db'

def query_db(db_path,query, args=(),one=False): #数据库查询
    g.db = sqlite3.connect(db_path)
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    g.db.close()
    return (rv[0] if rv else None) if one else rv





@app.route('/users/<int:user_id>')
def get_userinfo(user_id):
    return 'Your user_id is ' + str(user_id)

@app.route('/mb/<title_in>')
def home(title_in):
    my_list=[1,2,3,4,5,6,7,8,9,2,5]
    names=['qwedqads','dqe2dew2wed','dew1d5d55']
    return render_template(
        '071872438.html',
        title=title_in,
        my_list=my_list,
        names=names
    )
@app.route('/msg/<msgid>')
def webmove(msgid):
    return(redirect('https://www.chinosk6.cn/msg_g/' + msgid + '.html',code=302))


@app.route('/arcquery/<user_id>')
def queryhist_page(user_id):
    if str.isdigit(user_id) == False:
        return('非法id',403)
    db_p='C:\\Users\\Administrator\\Desktop\\arc\\qu_history\\userplayed.db'

    user_h = query_db(db_p,'select * from \''+ user_id +'\' order by time DESC')
    user_info = query_db(db_p,'select * from userinfo where id glob \''+ user_id +'\'')
    print(user_info)
    if os.path.isfile('C:\\Users\\Administrator\\Desktop\\arc\\qu_history\\no_query\\' + user_id):
        return('用户已设置禁止被查询',403)
    return render_template('userhist.html',user_info=user_info,user_h=user_h)

@app.route('/re/<input>',methods = ['GET','POST'])
def hello(input:str):
    stat = Connect_MySQL.get_url(input)
    if(stat[0] == True):
        return(redirect(stat[1],code=stat[2],))
    else:
        return(stat[1],stat[2])
 
if __name__ == '__main__':
    app.run('127.0.0.1', 11451) 


#import FlaskWebProject1.views_my
