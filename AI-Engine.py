# import pyttsx3
# import datetime
# import speech_recognition as sr
# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# def wishme():
#     hour=int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak('good morning sir')
#     elif hour>=12 and hour<18:
#         speak('good afternoon sir')
#     else:
#         speak('good evening sir')
#     speak('how can i help you')
# def takecommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening...')
#         r.pause_threshold=1
#         audio=r.listen(source) 
#     try:
#         print('wait for few moments...')
#         query=r.recognize_google(audio)
#         print('user said:',query)
#     except Exception as e:
#         print(e)
#         print('say that again,please ')         
#         return ""
# if __name__=="__main__":
#     wishme()
#     takecommand()

# import pyttsx3
# import datetime
# import speech_recognition as sr
# import wikipedia

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 170)

# def speak(audio):
#     print("Assistant:", audio)
#     engine.say(audio)
#     engine.runAndWait()
#     engine.stop()   

# def wishme():
#     hour = datetime.datetime.now().hour

#     if hour < 12:
#         speak("Good morning sir")
#     elif hour < 18:
#         speak("Good afternoon sir")
#     else:
#         speak("Good evening sir")

#     speak("I am ready")

# def takecommand():
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         r.adjust_for_ambient_noise(source, duration=0.5)

#         try:
#             audio = r.listen(source, timeout=5, phrase_time_limit=6)
#         except:
#             return ""

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio)
#         print("User said:", query)
#         return query.lower()

#     except:
#         return ""

# def wiki_answer(query):
#     try:
#         query = query.replace("wikipedia", "").strip()

#         if query == "":
#             return "Please say a topic."

#         speak("Searching Wikipedia")

#         result = wikipedia.summary(query, sentences=2)

#         return result

#     except:
#         return "Sorry, I couldn't find anything."

# def answer(query):

#     try:
#         if "exit" in query or "stop" in query:
#             speak("Goodbye")
#             return "exit"

#         elif "time" in query:
#             now = datetime.datetime.now().strftime("%I:%M %p")
#             speak(f"The time is {now}")

#         elif "date" in query:
#             today = datetime.date.today()
#             speak(f"Today's date is {today}")

#         else:
#             result = wiki_answer(query)
#             speak(result)

#     except Exception as e:
#         print("Error:", e)
#         speak("Something went wrong")

#     return ""

# if __name__ == "__main__":
#     wishme()

#     while True:
#         query = takecommand()

#         if query:
#             result = answer(query)

#             if result == "exit":
#                 break


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(text):
    engine = pyttsx3.init()  
    engine.setProperty('rate', 170)

    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning sir")
    elif hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

    speak("I am ready")

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
        except:
            return ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("User said:", query)
        return query.lower()

    except:
        return ""

def wiki_answer(query):
    try:
        query = query.replace("wikipedia", "").strip()

        if query == "":
            return "Please say a topic"

        speak("Thinking...")
        page = wikipedia.search(query)
        result = wikipedia.summary(page[0], sentences=2)
        return result

    except:
        return "I could not find anything"

def answer(query):

    if "exit" in query or "stop" in query:
        speak("Goodbye")
        return "exit"

    elif "time" in query:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "date" in query:
        today = datetime.date.today()
        speak(f"Today's date is {today}")

    else:
        result = wiki_answer(query)
        speak(result)

    return ""

if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand()

        if query:
            result = answer(query)

            if result == "exit":
                break