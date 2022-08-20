#!/usr/bin/env python3
# =========================================
# Makers! Implement your own actions here.
# =========================================

import aiy.audio
import aiy.cloudspeech
import aiy.voice

def main():
    my_motion_detector = MotionDetector()
    recognizer = aiy.cloudspeech.get_recognizer()
    aiy.audio.get_recorder().start()
    while True:
        my_motion_detector.WaitForMotion()
        text = recognizer.recognize()
        aiy.audio.say('You said ', text)

if __name__ == '__main__':
    main()