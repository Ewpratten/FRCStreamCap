from flask import Flask
from flask import request

import getdata as data

app = Flask(__name__)

@app.route("/")
def index():
    return "This is FRCStreamCap. Hello!"

# get frame from stream
# parse
# turn into dict
# return
@app.route("/api/get")
def get():
    if not request.args.get("account"):
        return "Invalid request. use the account argument along with a twitch account"
    
    # Get a frame
    frame = data.getFrame(request.args.get("account"))
    data = data.parseFrame(frame)

    return str(data)

if __name__ == "__main__":
    #debug
    print(data.parseFrame(data.getFrame("test")))

    #app
    # app.run()