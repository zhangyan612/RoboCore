import os
import aiy.cloudspeech

def main():
    recognizer = aiy.cloudspeech.get_recognizer()

    while True:
        print('Listening...')
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
        if 'goodbye' in text:
            os._exit(0)

if __name__ == '__main__':
    main()
