import os
import subprocess

from flask import Flask, request, render_template, url_for, redirect, send_file
#from ffmpy import FFmpeg
import ffmpeg

#pip install -r requirements.txt
#ae


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/savetofile", methods=["POST"])
def save_to_file():
    f = request.files['data']
    filename = request.values['filename']
    ogg = filename + ".ogg"
    mp3 = filename + ".mp3"
    f.save(os.path.join(os.getcwd(), ogg))
    #ff = FFmpeg(inputs={ogg: None}, outputs={mp3: '-ac 2 -codec:a libmp3lame -b:a 48k -ar 16000'})
    command = 'ffmpeg -i {}.ogg -ac 2 -codec:a libmp3lame -b:a 48k -ar 16000 {}.mp3'.format(filename, filename)
    subprocess.call(command, shell=True)
    #ff.run()
    return redirect(url_for("index"))


@app.route("/cama")
def audio_cama():
    f = os.path.join(os.getcwd(), "cama.mp3")
    print(os.listdir())
    return send_file(f, as_attachment=True)

@app.route("/cafeteira")
def audio_cafeteira():
    f = os.path.join(os.getcwd(), "cafeteira.mp3")
    print(os.listdir())
    return send_file(f, as_attachment=True)

@app.route("/geladeira")
def audio_geladeira():
    f = os.path.join(os.getcwd(), "geladeira.mp3")
    print(os.listdir())
    return send_file(f, as_attachment=True)

@app.route("/tv")
def audio_tv():
    f = os.path.join(os.getcwd(), "televisao.mp3")
    print(os.listdir())
    return send_file(f, as_attachment=True)

if __name__ == "__main__":
    app.run()