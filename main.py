from cloudlink import CloudLink
from tinydb import TinyDB, Query
import json
import requests
from time import sleep

# ======================================================================
# OCTAVIA BOT v0.1.0 - Developed by MikeDEV
# Based upon the Octavia! AI Chat Bot v0.3a by Jun-Dragon on Scratch.
#
# This software is Licensed using the MEOW License.
#
# ======================================================================

BOT_USERNAME = ""
BOT_PASSWORD = ""
BOT_DEBUG_MODE = True
BOT_DB_LOCATION = "./db.json"
API_ADDRESS = "https://api.meower.org/"
SERVER_ADDRESS = "wss://server.meower.org/"

# ======================================================================

class bootup: # Cloudlink setup stuff.
    def __init__(self):
        pass
    
    def bootscript1(self):
        cl.sendPacket({"cmd": "direct", "val": {"cmd": "authpswd", "val": {"username": str(BOT_USERNAME), "pswd": str(BOT_PASSWORD)}}, "listener": "auth"})
        
    def bootscript2(self):
        cl.sendPacket({"cmd": "direct", "val": {"cmd": "post_home", "val": "Hi! I'm Octavia. Simply @ me and I'll be happy to reply!"}, "listener": "startup"})
        
    def bootscript3(self):
        print("Octavia is booted up and running!")

class Octavia:
    def __init__(self):
        self.state = 0
        self.context = {}
        self.bootup = bootup()
    
    def checkCmdKeys(self, checkKeys, msg):
        checkOK = True
        for key in checkKeys:
            if not key in msg:
                checkOK = False
        return checkOK
    
    def startup(self, msg): # Bot's initialization script.
        self.codecheck = ["init", "auth", "startup"]
        self.cmdstate = [ # Shitty switch-case
            self.bootup.bootscript1,
            self.bootup.bootscript2,
            self.bootup.bootscript3
        ]
        
        if self.checkCmdKeys(["cmd", "val", "listener"], msg):
            if msg["cmd"] == "statuscode":
                if msg["listener"] == self.codecheck[self.state]:
                    if msg["val"]== cl.codes["OK"]:
                        self.cmdstate[self.state]()
                        self.state += 1
                    else:
                        print(f"Error at state {self.state}, got code {msg['val']}")
                        exit()
    
    def run(self, msg={}): # Bot main thread, handles booting the bot.
        if self.state in range(0, 3):
            self.startup(msg)
        else:
            self.main(msg)
    
    def add_new_msg(self, question, response):
        db.insert({"msg": question, "resp": response})
    
    def main(self, msg={}): # Shove your bot's main code here.
        if self.checkCmdKeys(["cmd", "val"], msg) and self.checkCmdKeys(["type", "post_origin", "p", "u"], msg["val"]):
            print(f"{msg['val']['u']} says: {msg['val']['p']}")
            msg_tmp = msg["val"]["p"]
            msg_tmp = msg_tmp.split(" ")
            
            #print(msg_tmp[0]) # Select first item in the list
            #print(msg_tmp[1:]) # Select all items after the first item
            #print(msg_tmp)
           
            if msg_tmp[0].lower() == ("@" + BOT_USERNAME.lower()):
                queryMsg = " ".join(msg_tmp[1:]).lower()
                print(queryMsg)
                print("bot mentioned")
                
                if not msg["val"]["u"] in self.context:
                    Response = Query()
                    responses = db.search(Response.msg == queryMsg)
                    
                    if len(responses) != 0:
                        resp = responses[0]["resp"]
                        resp = resp.replace("[username]", msg["val"]["u"])
                        resp = resp.replace("[size]", str(len(db)))
                        print(resp)
                        cl.sendPacket({"cmd": "direct", "val": {"cmd": "post_home", "val": f"@{msg['val']['u']} {resp}"}})
                    else:
                        print("no valid response present, creating new context")
                        self.context[msg["val"]["u"]] = queryMsg
                        cl.sendPacket({"cmd": "direct", "val": {"cmd": "post_home", "val": f"@{msg['val']['u']} I'm not sure how to respond to that yet. You can help me out by @'ing me with a response, or just tell me \"nevermind\"."}})
                else:
                    if "nevermind" == queryMsg:
                        cl.sendPacket({"cmd": "direct", "val": {"cmd": "post_home", "val": f"@{msg['val']['u']} Got it, I'll ignore further messages for now. Feel free to ask me anything by @'ing me!"}})
                    else:
                        db.insert({"msg": self.context[msg["val"]["u"]], "resp": queryMsg})
                        cl.sendPacket({"cmd": "direct", "val": {"cmd": "post_home", "val": f"@{msg['val']['u']} Got it, I'll respond with {queryMsg} if I get asked that question in the future. Feel free to ask me anything by @'ing me!"}})
                    del self.context[msg["val"]["u"]]
                #sleep(1)
                
def on_connect():
    cl.sendPacket({"cmd": "direct", "val": {"cmd": "ip", "val": requests.get(API_ADDRESS + "ip").text}})
    cl.sendPacket({"cmd": "direct", "val": {"cmd": "type", "val": "js"}})
    cl.sendPacket({"cmd": "direct", "val": "meower", "listener": "init"})
    
def on_error(error):
    print(f"{error}")

def on_packet(message):
    message = json.loads(message)
    bot.run(message)

if __name__ == "__main__":
    cl = CloudLink(BOT_DEBUG_MODE)
    db = TinyDB(BOT_DB_LOCATION)
    bot = Octavia()
    
    cl.callback("on_packet", on_packet)
    cl.callback("on_error", on_error)
    cl.callback("on_connect", on_connect)

    cl.client(ip=SERVER_ADDRESS)
