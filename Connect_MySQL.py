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


def get_url(id):
    pa = re.compile("[A-Za-z0-9]{4}")
    checkid = pa.findall(id)
    if(len(checkid) != 1 or len(id) != 4):
        return(False, "invalid parameter", 403)

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from shortlink where short = '" + id + "'") 
    
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    if(len(data)<=0):
        return(False, "Link not found", 404)

    try:
        data = data[0]['link']
        return(True, data, 302)
    except:
        return(False, "Database error", 500)

def insert_link(link, creator, wfrom, tablename = "shortlink"):
    stat = False
    pa = re.compile("^((https|http|ftp|rtsp|mms)?:\/\/).*\..*[^\s]+")
    if(len(pa.findall(link)) != 1):
        stat = False
        return(stat, "无效网址。请不要省略\"http://\"或\"https://\"")

    randstr = tools.generate_randstring(4)

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from " + tablename + " where short = \'" + randstr + "\'")
    data = cursor.fetchall()

    while(len(data)>0):
        randstr = tools.generate_randstring(4)
        cursor.execute("select * from " + tablename + " where short = \'" + randstr + "\'")
        data = cursor.fetchall()
  
    insql = "insert into " + tablename + "(short, link, creator, wfrom) values('%s', '%s', '%s', '%s')" % (randstr, link, creator, wfrom)
    data = cursor.fetchall()

    try:
        cursor.execute(insql)
        conn.commit()
        stat = True
        randstr = set.website.url + randstr
    except:
       conn.rollback()
       randstr = '数据写入失败'
       stat = False
       
    cursor.close()
    conn.close()
    return(stat, randstr)


#print(get_data("drop"))
#print(insert_link('qwq','adm','adm'))