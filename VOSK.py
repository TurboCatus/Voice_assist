from vosk import KaldiRecognizer, Model
import vosk
import queue
import sounddevice as sd
import pyaudio

def new():
    model = Model('C:\\Users\\TurboCat\\Documents\\speech_backup\\model\\')
    recognizer = KaldiRecognizer(model, 16000)

    cap=pyaudio.PyAudio()
    stream=cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,frames_per_buffer=8192)
    stream.start_stream()
    while True:
        data =  stream.read(4096)
        #if len(data) == 0:
            #break
        if recognizer.AcceptWaveform(data):
            #print(recognizer.Result())
            txt = recognizer.Result()
            print (txt)
            with open('speech.txt','w') as f:
                f.write(txt)
            if txt == "раз":
                print('Ок')


new()

'''
def do(text):
    if text == 'раз':
        print('Ok')

while True:
    do(new())
'''