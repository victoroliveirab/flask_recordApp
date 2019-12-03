const requestMicDiv = document.getElementById("request_mic");
const startStopDiv = document.getElementById("start_stop");
const audioTypeDiv = document.getElementById("audio_type");
const audioPlayerDiv = document.getElementById("audio_player");

const enableMicButton = document.getElementById("enable_mic");
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const uploadButton = document.getElementById("upload");

const audioConf = {
    tag: "audio",
    type: "audio/ogg",
    ext: ".ogg"
};

let stream, blob, recorder;
let audioChunks = [];


enableMicButton.onclick = e => {
    navigator.mediaDevices.getUserMedia({audio: true}).then(_stream => {
        stream = _stream;
        requestMicDiv.style.display = "none";
        startStopDiv.style.display = "grid";
        enableStartButton();
        recorder = new MediaRecorder(stream);
        recorder.ondataavailable = e => {
            audioChunks.push(e.data);
            if (recorder.state == "inactive") {
                processBlob();
            }
        }
    });
}

startButton.onclick = e => {
    enableStopButton();
    audioChunks = [];
    recorder.start();
};

stopButton.onclick = e => {
    enableStartButton();
    recorder.stop();
}

uploadButton.onclick = e => {
    saveBlob();
}

function enableStartButton() {
    startButton.disabled = false;
    startButton.style.backgroundColor = '#fedcba';
    stopButton.style.backgroundColor = '#ccc';
    stopButton.disabled = true;
}

function enableStopButton() {
    startButton.disabled = true;
    stopButton.style.backgroundColor = '#fedcba';
    startButton.style.backgroundColor = '#ccc';
    stopButton.disabled = false;
}

function processBlob() {
    blob = new Blob(audioChunks, {type: audioConf["type"]});
    let mediaTag = document.createElement(audioConf.tag);
    mediaTag.controls = true;
    mediaTag.src = URL.createObjectURL(blob);
    audioPlayerDiv.innerHTML = "";
    audioPlayerDiv.appendChild(mediaTag);
}

function saveBlob() {
    
    var fd = new FormData();
    let name = document.querySelector("input[name=equipment]:checked").value;
    fd.append('filename', name);
    fd.append('data', blob);
    $.ajax({
        type: 'POST',
        url: '/savetofile',
        data: fd,
        processData: false,
        contentType: false
    }).done(function() {
        audioPlayerDiv.innerHTML = "<center>Audio para " + name + " salvo com sucesso!</center>";
    });
}