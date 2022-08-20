#import threading
from multiprocessing import Process
import aiy.voicehat
import aiy.audio
import lina
import time

def main():
    Running = False
    print('LED is ON while button is pressed (Ctrl-C for exit).')
    button = aiy.voicehat.get_button()
    listenerThread = Process(target = lina.LinstenForCry)
    while True:
        button.wait_for_press()
        Running = not Running
        # print(Running)
        if Running:
            aiy.audio.say("Start listening for sound")
            print(listenerThread.exitcode)
            if listenerThread.exitcode != None:
               listenerThread = Process(target = lina.LinstenForCry)
            listenerThread.start()
        else:
            time.sleep(1)
            listenerThread.terminate()
            aiy.audio.say("Shut down")
        

if __name__ == '__main__':
    main()
