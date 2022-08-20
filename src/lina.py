import aiy.audio
import pyaudio
import numpy as np
import time

p=pyaudio.PyAudio()

def LinstenForCry():
    CHUNK = 2**11
    RATE = 44100
    Counter = 0
    triggerThreshold = 23000
    trigger = 5

    #for i in range(int(10*44100/1024)): #go for a few seconds
    while True:
        stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        numBar = int(50*peak/2**16)
        bars="#"*numBar
        # print("%04d %05d %s"%(i,peak,bars))
        print("%05d %s"%(peak,bars))
        if peak > triggerThreshold:
            Counter+=1
        else:
            Counter = 0

        if Counter >= trigger:
            print('too loud, trigger action')
            aiy.audio.play_wave("triggers/resources/ding.wav")
            aiy.audio.say("Lina, stop crying")
            Counter = 0
            time.sleep(5)

    print('exception, restart stream')
    stream.stop_stream()
    stream.close()
    p.terminate()



if __name__ == "__main__":
    LinstenForCry()
    


