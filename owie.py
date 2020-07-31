from flask import Flask, render_template, request, send_file
import wikipedia
import functools,operator,re
from radar import RadarClient


radar = RadarClient("prj_test_sk_a014dc93fd7af85ef7ae08dba757a3316987e979")


app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
    return render_template("owiepage.html")

@app.route("/parse",methods=['GET', 'POST'])
def gen():

    res = wikipedia.random()
    total = 1
    total = [ord(num) for num in res]
    mul = functools.reduce(operator.add,total)
    ttl = (mul%10)+1

    geo = radar.geocode.ip(ip='67.180.229.63')
    #print(geo.latitude)
    lat = re.findall('.*\.',str(geo.latitude))[0][:-1]
    lng = re.findall('.*\.',str(geo.longitude))[0][:-1]

    print(lat,lng)

    return str((mul%10)+1)
    #//funs tuff


if __name__ == "__main__":
    app.run(debug=True)
