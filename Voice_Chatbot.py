import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import pywhatkit
import pyjokes
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# 0 for male voice and 1 for female voice

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        speak("Good Morning!!!")
    elif hour>=12 and hour<16:
        speak("Good After noon!!!")
    else:
        speak("Good Evening!!!")

    speak("I am Nova. Please tell how may I help you?")

def takeCommand():
    #It takes speech input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        #print("Recogniting....")
        query = r.recognize_google(audio,language='en-in')

        #It can also give output in hindi..... language--> hi-en
        print("User said: ",query)

    except Exception as e:
        #print(e) #-->This will print any errors that he will face.
        print("Sorry I can't recognize that can you say that again...\n")
        return "None"
    return query

if __name__== "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

#Logic for executing tasks

        if 'youtube' in query:
            speak("Open ing Youtube...")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Open ing google...")
            webbrowser.open("search.google.com")

        elif 'open map' in query:
            speak("Open ing google maps...")
            webbrowser.open("googlemaps.com")

        elif 'mail' in query:
            speak("Open ing your g mails...")
            webbrowser.open("https://mail.google.com//mail")

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strtime}")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'tell me about' in query:
            search = query.replace('tell me about','')
            speak('here s what i found')
            pywhatkit.search(search)
            results = wikipedia.summary(search, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'vs code' in query:
            speak("Opening V.S. Code...")
            #Use your default vs code location
            vs_code='"C:\\Users\\KIIT0001\\Desktop\\Visual Studio Code.lnk"'
            os.startfile(os.path.join(vs_code))

        elif 'i love you' in query:
            speak("I am in a encrypted relationship with WIFI")

        elif'what can you do' in query:
            speak("I can play songs for you; play youtube videos for you; open maps and much more. just ask")

        elif 'camera' in query:
                    speak("Opening Camera.     Smile Please!!!")
                    cap = cv2.VideoCapture(0)
                    speak("press q to exit")
                    while True:
                        # Capture frame-by-frame
                        ret, frame = cap.read()

                        # Display the frame
                        cv2.imshow('Camera', frame)

                        # Press 'q' to exit
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                    # Release the camera and close the window
                    cap.release()
                    cv2.destroyAllWindows()

        elif 'shutdown' in query:
            speak("Turning off P.C.")
            os.system("shutdown /s /t 2")

        elif 'restart' in query:
            speak("Restarting P.C.")
            os.system("shutdown /r /t 2")                    

        elif 'stop' in query:
            speak("I am glad to be in your service")
            break


##        if 'wikipedia' in query:
##            speak('loo king out in wikipedia...')
##            query = query.replace("wikipedia", "")
##            results = wikipedia.summary(query, sentences=2)
##            speak("According to wikipedia")
##            speak(results)
##        elif 'play music' in query:
##            speak("okay!!  Playing music...")
##            music_dir = 'C:\\Users\\KIIT0001\\Music'
##            songs = os.listdir(music_dir)
##            print(songs)
##            os.startfile(os.path.join(music_dir, songs[0]))
