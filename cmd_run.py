import Connect_MySQL as cms
import sys

argvs = sys.argv

if(len(argvs)<4):
    print("参数错误")
    sys.exit()

stat = cms.insert_link(argvs[1],argvs[2],argvs[3]) #链接,创建者,来自
if(stat[0] == False):
    print(stat[1])
    sys.exit()
else:
    print("创建成功:" + stat[1])