from flask import Flask, render_template, request

import numpy as np
import os

import youtube_dl
from time import time
from datetime import timedelta
import moviepy.editor as mp
import soundfile as sf
from keras.models import load_model
import numpy as np
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from threading import Thread, Event
import librosa
from sklearn.preprocessing import LabelEncoder

model = load_model('saved_model/my_model.h5')

port = 12390

threads = [Thread()]
def project_id():
    import json
    info = json.load(
        open(os.path.join(os.environ['HOME'], ".smc", "info.json"), 'r'))
    return info['project_id']


base_url = "/%s/port/%s/" % (project_id(), port)
static_url = "/%s/port/%s/static" % (project_id(), port)
app = Flask(__name__, static_url_path=static_url)

classes=[ 'dog', 'one', 'down', 'right', 'cat', 'bed', 'up', 'eight', 'marvin', 'six', 'nine', 'four', 'five', 'yes', 'three', 'wow', 'sheila', 'zero', 'seven', 'happy', 'go', 'bird', 'two', 'stop', 'off', 'tree',  'house', 'on', 'left', 'no']

le = LabelEncoder()
le.fit(classes)
classes= list(le.classes_)

def predict(audio_path):
    global classes
    print("started pPredicting")
    samples,sr = librosa.load(audio_path, sr=16_000)
    audio = librosa.resample(samples, sr, 8_000)
    prob = model.predict(audio.reshape(-1,8_000,1)) #prob is a vector of 10 values
    index = np.argmax(prob[0])
    print(classes[index])
    print("Finished Predicting")
    return classes[index]


@app.route(base_url, methods=['POST', 'GET'])
def home():
    name = "TensorFlow Speech Recognition Challenge - Universal"
    return render_template('Speech-Recognition---Kaggle.html', name=name)


@app.route(base_url+'/predict', methods=['POST', 'GET'])
def youtube_url():
    global threads
    print('I am predicting! Please Wait!')
    file_object =request.files.get('file')
    file_object.save('static/audio.wav')
    prediction = predict('static/audio.wav')
    return prediction

@app.route(base_url+'/thread-check', methods=['POST', 'GET'])
def thread_check():
    global threads
    return "1" if threads[0].is_alive() else "0"
    
if __name__ == "__main__":
    # you will need to change code.ai-camp.org to other urls if you are not running on the coding center.
    print(
        "Try to open\n\n    https://cocalcg12.ai-camp.org" + base_url + '\n\n')
    # We don't need to call app.run(), we just call socketio to run everything since it's a flask wrapper.
    # We need also to have .js and .map file in static, and reference them from the client or html side
    app.run( host='0.0.0.0', port=port, debug=True)
    import sys
    sys.exit(0)
