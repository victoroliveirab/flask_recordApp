import os
import subprocess

from flask import Flask, request, render_template, url_for, redirect, send_file
import ffmpeg


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/savetofile", methods=["POST"])
def save_to_file():
    f = request.files['data']
    filename = request.values['filename']
    f.save(os.path.join(os.getcwd(), filename + ".ogg"))
    command = 'ffmpeg -i {}.ogg -ac 2 -codec:a libmp3lame -b:a 48k -ar 16000 {}.mp3'.format(filename, filename)
    subprocess.call(command, shell=True)
    return redirect(url_for("index"))


@app.route("/cama")
def audio_cama():
    f = os.path.join(os.getcwd(), "cama.mp3")
    if (os.path.isdir(f)):
        return send_file(f, as_attachment=True)

if __name__ == "__main__":
    app.run()