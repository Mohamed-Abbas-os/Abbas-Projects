import pyttsx3
import speech_recognition as sr
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
def listen():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_sphinx(audio)
            print('you said :',text)
            return text.lower()
        except sr.UnknownValueError:
            print('sorry,I did not catch that.')
            return ''
        except sr.RequestError as e:
            print('recognizer error:{0}'.format(e))
            return ''
def main():
    speak('hello i am your offline assistant.hoe can i help you?')
    while True:
        command=listen()
        if 'hello ' in command:
            speak('hi there')
        elif 'time' in command:
            import datetime
            now=datetime.datetime.now()
            speak(f"the current time is {now.strftime('%I:%M%p')}")
        elif 'exit' in command:
            speak('goodbye')
            break
        elif command!='':
            speak('I heard you say :' + command)
        else:
            speak('please try again')
if __name__=='__main__':
    main()