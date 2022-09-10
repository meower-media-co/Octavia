from cloudlink import Cloudlink

# ======================================================================
#
# Octavia - The not-so friendly chatbot for Meower - Created by MikeDEV
# Based upon Octavia! Chatbot on Scratch.
#
# This software is Licensed using the MEOW License.
#
# Requires cloudlink >= 0.1.8.4
#
# ======================================================================

BOT_USERNAME = "Octavia"
BOT_PASSWORD = ""
BOT_DEBUG_MODE = True
SERVER_ADDRESS = "ws://127.0.0.1:3000/"
BOT_STARTUP_MESSAGE = "Hi! I'm Octavia. Simply @ me and I'll be happy to reply!"
LINK_DEFAULT_ROOM = "org.meower.Meower"

# ======================================================================

class Octavia:
    def __init__(self, cloudlink):
        # To use callbacks, you will need to initialize your callbacks class with Cloudlink. This is required.
        self.cloudlink = cloudlink
        self.supporter = cloudlink.supporter
        self.log = cloudlink.supporter.log
        self.bot_ready = False

    def on_connect(self): # Called when the client is connected to the server.
        self.log(f"{BOT_USERNAME} is now connected to the server!", True)
        self.cloudlink.setUsername("Octavia")

    def on_close(self, close_status_code, close_msg): # Called when the client is disconnected from the server.
        self.log(f"{BOT_USERNAME} is no longer connected!", True)

    def on_error(self, error): # Called when the client encounters an exception.
        self.log(f"An error has occurred: {error}", True)

    def on_statuscode(self, code:str, message:any): # Called when a packet is received with the statuscode command.
        if "listener" in message:
            if message["listener"] == "username_set":
                self.log(f"{BOT_USERNAME}'s client object is {self.cloudlink.myClientObject}", True)
                self.log(f"Linking {BOT_USERNAME} to room {LINK_DEFAULT_ROOM}, please wait...", True)
                self.cloudlink.linkToRooms(LINK_DEFAULT_ROOM, "link_check")
            
            if message["listener"] == "link_check":
                self.log(f"{BOT_USERNAME} is now linked to {LINK_DEFAULT_ROOM}, now authenticating the bot...", True)
                self.cloudlink.sendCustom(cmd="authpswd", message={"username": str(BOT_USERNAME), "pswd": str(BOT_PASSWORD)}, listener="auth_bot")
            
            if message["listener"] == "auth_bot":
                if message["code"] == self.supporter.codes["OK"]:
                    self.log(BOT_USERNAME, "is now authenticated, and is ready to accept commands!", True)
                    self.bot_ready = True
                    self.cloudlink.sendCustom(cmd="gmsg", message=BOT_STARTUP_MESSAGE)
                else:
                    self.log(f"{BOT_USERNAME} failed to authenticate! Error code {message['code']}", True)
                    self.log(f"{BOT_USERNAME} is now disconnecting from the server due to failed authentication...", True)
                    self.cloudlink.stop()
    
    def on_gmsg(self, message:str): # Called when a packet is received with the gmsg command.
        pass

    def on_ulist(self, userlist:any):
        #self.log(userlist, True)
        pass

if __name__ == "__main__":
    # Initialize Cloudlink. You will only need to initialize one instance of the main cloudlink module.
    cl = Cloudlink()

    # Create a new client object. This supports initializing many clients at once.
    client = cl.client(logs=BOT_DEBUG_MODE)

    # Create callbacks. You can only initialize callbacks after you have initialized a cloudlink client object.
    bot = Octavia(client)

    # Bind callbacks
    client.callback(client.on_connect, bot.on_connect)
    client.callback(client.on_close, bot.on_close)
    client.callback(client.on_error, bot.on_error)
    client.callback(client.on_statuscode, bot.on_statuscode)
    client.callback(client.on_gmsg, bot.on_gmsg)
    client.callback(client.on_ulist, bot.on_ulist)

    # Connect to the server and run the bot.
    client.run(ip=SERVER_ADDRESS)