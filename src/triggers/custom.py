"""Detect keyword in the audio stream."""

import snowboydecoder
import sys
import signal

import logging
import numpy as np


interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

# import trigger in aiy project
class Trigger(object):

    """Base class for a Trigger."""

    def __init__(self):
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def start(self):
        pass


logger = logging.getLogger('trigger')


class CustomTrigger(Trigger):

    """Detect claps in the audio stream."""

    def __init__(self, recorder):
        super().__init__()

        self.have_keyword = True  # don't start yet
        self.prev_sample = 0
        recorder.add_processor(self)

    def start(self):
        self.prev_sample = 0
        self.have_keyword = False

    def detected(self):
        self.have_keyword = True
        self.callback()

    def add_data(self, data):
        # capture SIGINT signal, e.g., Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)
        detector = snowboydecoder.HotwordDetector("Alice.pmdl", sensitivity=0.5, audio_gain=1)
        # detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
        print('Listening... Press Ctrl+C to exit')
        # main loop
        detector.start(detected_callback=self.detected(),
                    interrupt_check=interrupt_callback,
                    sleep_time=0.03)
        detector.terminate()

        """ audio is mono 16bit signed at 16kHz """
        # audio = np.fromstring(data, 'int16')
        # if not self.have_keyword:
        #     # alternative: np.abs(audio).sum() > thresh
        #     shifted = np.roll(audio, 1)
        #     shifted[0] = self.prev_sample
        #     val = np.max(np.abs(shifted - audio))
        #     if val > (65536 // 4):  # quarter max delta
        #         logger.info("clap detected")
        #         self.have_keyword = True
        #         self.callback()
        # self.prev_sample = audio[-1]
