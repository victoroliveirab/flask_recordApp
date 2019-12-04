import os
import subprocess

from flask import Flask, request, render_template, url_for, redirect, send_file
#from ffmpy import FFmpeg
import ffmpeg

#pip install -r requirements.txt
#ae
#https://elements.heroku.com/buildpacks/jonathanong/heroku-buildpack-ffmpeg-latest


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
    command = 'ffmpeg -y -i {}.ogg -ac 2 -codec:a libmp3lame -b:a 48k -ar 16000 {}.mp3'.format(filename, filename)
    subprocess.call(command, shell=True)
    #ff.run()
    return redirect(url_for("index"))


@app.route("/cama")
def audio_cama():
    audio_name = "cama.mp3"
    f = os.path.join(os.getcwd(), audio_name)
    if (not os.path.isdir(f)):
        return send_not_available()
    return send_file(f, as_attachment=True)

@app.route("/cafeteira")
def audio_cafeteira():
    audio_name = "cafeteira.mp3"
    f = os.path.join(os.getcwd(), audio_name)
    if (not os.path.isdir(f)):
        return send_not_available()
    return send_file(f, as_attachment=True)

@app.route("/geladeira")
def audio_geladeira():
    audio_name = "geladeira.mp3"
    f = os.path.join(os.getcwd(), audio_name)
    if (not os.path.isdir(f)):
        return send_not_available()
    return send_file(f, as_attachment=True)

@app.route("/tv")
def audio_tv():
    audio_name = "televisao.mp3"
    f = os.path.join(os.getcwd(), audio_name)
    if (not os.path.isdir(f)):
        return send_not_available()
    return send_file(f, as_attachment=True)

@app.route("/luz")
def audio_luz():
    audio_name = "luz.mp3"
    f = os.path.join(os.getcwd(), audio_name)
    if (not os.path.isdir(f)):
        return send_not_available()
    return send_file(f, as_attachment=True)

@app.route("/fogao")
def audio_fogao():
    audio_name = "fogao.mp3"
    f = os.path.join(os.getcwd(), audio_name)
    if (not os.path.isdir(f)):
        return send_not_available()
    return send_file(f, as_attachment=True)

@app.route("/microondas")
def audio_microondas():
    audio_name = "microondas.mp3"
    f = os.path.join(os.getcwd(), audio_name)
    if (not os.path.isdir(f)):
        return send_not_available()
    return send_file(f, as_attachment=True)


########## UTILS ##########
def send_not_available():
    return send_file(os.path.join(os.getcwd(), "indisponivel.mp3"), as_attachment=True)

if __name__ == "__main__":
    app.run()