import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )
    data_stream = wf.readframes(chunk)
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmmd = Commander()

def initSpeech():
    print('Listening...')
    with sr.Microphone() as source:
        audio = r.listen(source)
    # play_audio('./audio/sentnc16.wav')
    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print('I could not understand you')
    print('Your command:')
    print(command)
    if command in ['quit', 'exit', 'exits' 'bye', 'by' 'good-by', 'goodbye']:
        global running
        running = False
        
    cmmd.discover(command)

play_audio('./audio/sentnc10.wav')
while running == True:
    initSpeech()
