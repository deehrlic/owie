from flask import Flask, render_template, request, send_file
import wikipedia
import functools,operator,re,os,io,sys,time
from google.cloud import vision
#from radar import RadarClient


#radar = RadarClient("prj_live_sk_5ec7432841dec7376548dc61e7fb6c395e4729d5")


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

    #geo = radar.geocode.ip(ip='67.180.229.63')
    #print(geo.latitude)
    #lat = re.findall('.*\.',str(geo.latitude))[0][:-1]
    #lng = re.findall('.*\.',str(geo.longitude))[0][:-1]
    lat = 37
    lng = -122

    print(lat,lng)
    
    #WEBCAM CAPTURE TIME
    os.system("ffmpeg -f video4linux2 -r 25 -y -s 920x1080 -t 10 -i /dev/video0 /home/pi/Desktop/owie/video.avi")
    os.system("ffmpeg -i video.avi -vcodec png -y -vframes 1 -an -f rawvideo cap.png")
    
    #GCP LABEL TIME
    client = vision.ImageAnnotatorClient()
    with io.open('cap.png', 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    
    if "Photography" in labels:
        labels.del("Photography")
    if "Portrait" in labels:
        labels.del("Photography")
    if "Illustration" in labels:
        labels.del("Photography")
        
    
    for label in labels:
        print(label.description)
        

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))    

    
    
    return "succcess"


if __name__ == "__main__":
    app.run(debug=True)
