from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import os
import soundfile as sf
import librosa
import wave
from pydub import AudioSegment
from dgx_enquire import dgx_enquire
from dgx_enquire_audio import dgx_enquire_audio
from dgx_resp import dgx_resp
app = Flask(__name__)

AUDIO_SAMPLE_RATE = 16000

dgxWelcomeMsg = ["Hi, I'm DGX Bot. You can ask me questions about DGX systems. For example: ", 
" ", 
"What is DGX System?",
"How to monitor the DGX System?",
"What are the storage options available for DGX system?",
"What are the benefits of using DGX?"]

dgxData = {
    "queries": [None],
    "responses": [dgxWelcomeMsg],
    "count": 1,
    "reloadSpeech": False  # offset the reload.
}

@app.route("/")
def root_page():
    return render_template('home.html')

@app.route('/dgxSubmit', methods=['POST'])
def dgxSubmit():
    dgx_query = request.form['dgx_query']
    print(dgx_query)
    if dgx_query == '':
        dgx_query = "Hello, DGX!"
    dgxData["queries"].append(dgx_query)
    dgxData["count"] += 1
    return redirect(url_for('dgxChat', query=dgx_query))

@app.route('/dgxUpload', methods=['POST'])
def dgxUpload():
    if "audio_file" in request.files:
        dgxAudioFile = request.files['audio_file']
        i = len(os.listdir("dgxAudios"))
        audioSavePath = "dgxAudios/audio_file_{}.wav".format(i)
        dgxAudioFile.save(audioSavePath)
        audio, sample_rate = librosa.load(audioSavePath)
        sf.write(audioSavePath, audio, sample_rate)

        wf = wave.open(audioSavePath, 'rb')
        with open(audioSavePath, 'rb') as fh:
            data = fh.read()
        # Accepted by Riva
        dgx_query = dgx_enquire_audio(wf, data)
        dgxData["queries"].append(dgx_query)
        dgxData["count"] += 1
    #    dgxData["reloadSpeech"] = True
        return redirect(url_for('dgxChat', query=dgx_query))

@app.route('/DGXChat')
def dgxChat():
    dgxQuery = dgxData["queries"][dgxData["count"] - 1]
    if dgxQuery != None:
        with open("dgxUtter/dgx_utter.txt", "a") as f:
            f.write(dgxQuery + "\n")
    if (dgxQuery != None) and (len(dgxData["responses"]) < dgxData["count"]):
        className = dgx_enquire([dgxQuery])
        dgxResp = dgx_resp(className)
        dgxData["responses"].append(dgxResp)
    #if dgxData["reloadSpeech"]:
    #    del dgxData["responses"][len(dgxData["responses"]) - 1]
    #    dgxData["reloadSpeech"] = False
    print(dgxData)
    return render_template("DGXChat.html", dgxData=dgxData)

@app.route('/static')
def staticPage():
    return render_template('static.html')
     
if __name__ == '__main__':
    # app.run(host="10.19.27.27", ssl_context=('cert/server.crt', 'cert/server.key'))
    app.run(host="10.19.27.27")
