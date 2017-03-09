import pyaudio
import wave
import speech_recognition as sr
from commands import Commander


def play_audio(filename):
    """
    play_audio is a method that takes one argument, filename.
    play_audio plays the wav files that you hear at the start and end of the app
    argument:
        filename = the path to/ name of a WAVE file you wish to play
    """
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


def init_speech():
    """
    initSpeech contains the while loop that is this application
    it takes no arguments
    initSpeech listens for user and commands and quits if that is the command,
    returns to top of while loop if command not recognized, otherwise it passes
    the command off to discover
    """
    program = True
    while program is True:
        print('Listening...')
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(command)
        except:
            continue

        if command in ['quit', 'exit', 'exits', 'exxat', 'bye', 'by' 'good-by', 'goodbye']:
            program = False
            play_audio('./audio/sentnc16.wav')
            break

        cmmd.discover(command)

play_audio('./audio/sentnc10.wav')
init_speech()
