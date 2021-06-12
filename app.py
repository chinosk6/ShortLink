from flask import Flask,redirect,request,jsonify
import connect_settings as set
import Connect_MySQL
import json

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

@app.route('/api',methods = ['GET','POST'])
def api():
    key = request.args.get("key")
    typ = request.args.get("type")#add/del
    link = request.args.get("link")

    if(all([key, typ, link]) == False):
        return(jsonify({"stat":-1,"msg":"Missing required parameters"}), 412)
    if(key != set.website.key):
        return(jsonify({"stat":-1,"msg":"Invalid secret key"}), 403)

    if(typ == "add"):
        creator = str(request.args.get("creator"))
        frm = str(request.args.get("from"))

        stat = Connect_MySQL.insert_link(link, creator, frm)
        if(stat[0] == False):
            return(jsonify({"stat":-1,"msg":stat[1]}), 400)
        else:
            return(jsonify({"stat":0,"msg":stat[1]}), 200)

    elif(typ == "del"):
        stat = Connect_MySQL.del_link(link)
        if(stat[0] == False):
            return(jsonify({"stat":-1,"msg":stat[1]}), 400)
        else:
            return(jsonify({"stat":0,"msg":stat[1]}), 200)

    else:
        return(jsonify({"stat":-1,"msg":"Invalid parameter : \"type\""}), 412)

if __name__ == '__main__':
    app.run(set.flask_basic.host, set.flask_basic.port,debug = True)
