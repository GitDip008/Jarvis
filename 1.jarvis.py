import pyttsx3                         # installed
import datetime
import speech_recognition as sr        # installed
import wikipedia                       # installed
import webbrowser
import os
import smtplib
import random
# business
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good Noon")

    elif hour >= 16 and hour < 18:
        speak("Good Afternoon")

    elif hour >= 18 and hour < 21:
        speak("Good Evening")

    else:
        speak("Good Night")

    speak("I am Jarvis. How may I help you sir?")


# taking command from microphone and outputs a string

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .8
        audio = r.listen(source)

    try:
        print("Recognizing your commands...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)            # to print the error

        error_text = "Sorry sir. I am not programmed to do this."
        print(error_text)
        return "None"

    return query


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("shourovdip145@gmail.com", "")
    server.sendmail('shourovdip145@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()

    while True:
        query = take_command().lower()

        if "how are you doing" in query:
            speak("Everything is going on just fine. How about you,Sir?")
            reply = take_command()
            if "not feeling good" in reply:
                speak("Oh o. I feel sad hearing that. What would you like me to do,Sir?")
            elif "fine" in reply:
                speak("That's great! What would you like me to do for you,Sir?")

        elif 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get().open("www.youtube.com")
            speak("Here you go Sir! May you find something interesting to watch!"
                  "You can watch some AI and Machine Learning stuff to improve me!!!")

        elif 'open google' in query:
            webbrowser.get().open("www.google.com")
            speak("Here Sir! I opened Google for you.")

        elif 'in google' in query:
            speak("What should I search for,Sir?")
            search_item = take_command().lower()
            url = 'https://google.com/search?q=' + search_item
            webbrowser.get().open(url)
            speak("I have found this for " + search_item)
            speak("What would you like me to do next,Sir?")

        elif 'location' in query:
            speak("What location are you looking for,Sir?")
            location = take_command()
            location_url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(location_url)
            speak("Here's the location for " + location + ",Sir")

        elif 'stackoverflow' in query:
            webbrowser.get().open("www.stackoverflow.com")
            speak("I opened it for you. Remember to copy from answers, NOT FROM QUESTIONS!!!")

        elif 'sing a song' in query:
            speak("Sorry Sir! I can not do that. But I can play music for you")

        elif 'play music' in query:
            music_dir = "G:\\MP3\\pink floyd\\"
            songs = os.listdir(music_dir)
            print(songs)
            random_num = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[random_num]))
            speak("Enjoy the music Sir!")

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H%M%S")
            print(time)
            speak(f"The time is {time}")

        elif 'sublime' in query:
            sw_path = "C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(sw_path)
            speak("Happy coding Sir!")



        elif 'email' in query:
            try:
                speak("What should i write sir?")
                content = take_command()
                to = "shourovdip143@gmail.com"
                send_email(to, content)
                speak("The Email has been sent. No need to call him to be confirmed,Sir.")
            except Exception as e:
                print(e)
                speak("Sorry sir. Could not send the e-mail")

        elif 'quit' in query:
            speak("Jarvis will now go to sleep sir. Love you three thousand!")
            exit()

        elif 'exit' in query:
            speak("Jarvis will now go to sleep sir. Love you three thousand!")
            exit()

        elif 'you may go' in query:
            speak("Jarvis will now go to sleep sir. Love you three thousand!")
            exit()

        else:
            speak("Sorry Sir! I am not programmed to do this. Tell me to do something else!")