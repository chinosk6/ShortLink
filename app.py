from flask import Flask,redirect
import connect_settings as set
import Connect_MySQL

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/<input>',methods = ['GET','POST'])
def hello(input:str):
    stat = Connect_MySQL.get_url(input)
    if(stat[0] == True):
        return(redirect(stat[1],code=stat[2],))
    else:
        return(stat[1],stat[2])


if __name__ == '__main__':
    app.run(set.flask_basic.host, set.flask_basic.port,debug = True)
