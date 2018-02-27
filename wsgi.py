import socket
import datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    with open('/mnt/logfile', 'a+') as log:
        log.write('Greetings from '+socket.gethostname()+' at ' + str(datetime.datetime.now() + '\n')
        log.seek(0)
        data = log.read()
    
    return data


if __name__ == "__main__":
    application.run()
