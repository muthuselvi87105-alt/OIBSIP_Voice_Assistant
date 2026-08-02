import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# Initialize
engine = pyttsx3.init()
recognizer = sr.Recognizer()

print("===================================")
print("     Voice Assistant Started")
print("Say: hello, time, date, search ...")
print("Say 'exit' to stop")
print("===================================")

while True:

    with sr.Microphone() as source:
        print("\nSpeak something...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        text = text.lower()

        print("You said:", text)

        # Exit
        if "exit" in text or "stop" in text:
            print("Goodbye!")
            engine.say("Goodbye")
            engine.runAndWait()
            break

        # Hello
        elif "hello" in text:
            print("Hello! How can I help you?")
            engine.say("Hello! How can I help you?")
            engine.runAndWait()

        # Time
        elif "time" in text:
            current_time = datetime.datetime.now().strftime("%I:%M %p")

            print("Current Time:", current_time)

            engine.say(f"The current time is {current_time}")
            engine.runAndWait()

        # Date
        elif "date" in text or "today" in text:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")

            print("Today's Date:", current_date)

            engine.say(f"Today's date is {current_date}")
            engine.runAndWait()

        # Search
        elif "search" in text:

            search_query = text.replace("search", "").strip()

            if search_query:

                print("Searching for:", search_query)

                engine.say(f"Searching for {search_query}")
                engine.runAndWait()

                webbrowser.open(f"https://www.google.com/search?q={search_query}")

            else:

                print("Please say what you want to search.")

                engine.say("Please say what you want to search.")

                engine.runAndWait()

        # Unknown Command
        else:

            print("Sorry, I don't know this command.")

            engine.say("Sorry, I don't know this command.")

            engine.runAndWait()

    except sr.UnknownValueError:

        print("Sorry, I could not understand your voice.")

        engine.say("Sorry, I could not understand your voice.")

        engine.runAndWait()

    except sr.RequestError:

        print("Network Error!")

        engine.say("Please check your internet connection.")

        engine.runAndWait()