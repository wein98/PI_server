from flask import Flask, json, request
import flask
from threading import Thread
import requests
import time

piStr = ''

# source: https://mail.python.org/pipermail/edu-sig/2006-July/006810.html 
def pi_digits(x):
    """Generate x digits of Pi."""
    k,a,b,a1,b1 = 2,4,1,12,4
    while x > 0:
        p,q,k = k * k, 2 * k + 1, k + 1
        a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d,d1 = a/b, a1/b1
        while d == d1 and x > 0:
            global piStr 
            piStr += str(int(d))
            if len(piStr) == 1:
              piStr += '.'
            r = requests.get(url = "http://127.0.0.1:5000/update?pi="+str(piStr))
            # apidata.update(self.piStr)
            # print(self.getPiStr())
            # yield int(d)
            x -= 1
            a,a1 = 10*(a % b), 10*(a1 % b1)
            d,d1 = a/b, a1/b1
            time.sleep(2)

api = Flask(__name__)
currData = ''

# GET // get the most updated PI stored in currData
@api.route('/getPI', methods=['GET'])
def get_PI():
  global currData
  resp = api.make_response({"data": currData})
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

# GET // update currData everytime a new PI is calculated
@api.route('/update', methods=['GET'])
def update():
  global currData
  currData = request.args['pi']
  return ('ok', 200)


if __name__ == '__main__':
    # run two threads at the same time
    t1 = Thread(target = api.run)
    t2 = Thread(target = pi_digits, args = (1000, ))
    t1.start()
    t2.start()

# NOTE:
# URL max string (https://stackoverflow.com/questions/812925/what-is-the-maximum-possible-length-of-a-query-string#:~:text=3%20Answers&text=RFC%202616%20(Hypertext%20Transfer%20Protocol,a%20query%20string%20(section%203.2.&text=RFC%203986%20(Uniform%20Resource%20Identifier,3).)