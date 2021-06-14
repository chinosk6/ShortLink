import pymysql
import connect_settings as set
import tools
import re

host = set.mysql.host
port = set.mysql.port
db = set.mysql.db
user = set.mysql.user
password = set.mysql.password

def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    return conn


def get_safe(name, passwd, tablename = "user_table"):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    ret = cursor.execute("select * from user_table where username=%s and password=%s" , (name, passwd)) 
    
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if(ret):
        print("成功")
    else:
        print("失败")

def get_unsafe(name, passwd, tablename = "user_table"):

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    ret = cursor.execute("select * from user_table where username='%s' and password='%s'" % (name, passwd)) 
    
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if(ret):
        print("成功")
    else:
        print("失败")

get_safe("123","123")
get_safe("'or 1 = 1 -- ",'')
print("----")
get_unsafe("123","123")
get_unsafe("'or 1 = 1 -- ",'')