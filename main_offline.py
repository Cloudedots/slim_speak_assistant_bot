import speech_recognition as spr

r1 = spr.Recognizer()
r2 = spr.Recognizer()
r3 = spr.Recognizer()


def call_dev():
    r2 = spr.Recognizer()
    with spr.Microphone() as source:
        listen = r3.listen(source)
        print(f"source: {spr.Microphone()}")
        try:
            text = r2.recognize_sphinx(listen)
            print(f"word: {str(text).lower()}")
            if "dev" in str(text).lower() or "slim" in str(text).lower():
                r2 = spr.Recognizer()
                with spr.Microphone() as source:
                    print("Dev:Yes please, what can I help you?")
                    return r2.listen(source)
        except:
            print("Sphinx could not understand audio")

    return ""


def ask_dev(speech_text):
    try:
        asked = r3.recognize_google(speech_text)
        print(f"You: {asked}")
        return asked
    except spr.UnknownValueError:
        print(f"Dev: There was an error. Please try again.")
        return ""


print("Dev: Hi, I am Dev. Developed by Cloudedots")
print("Dev: You can ask me anything related to my knowledge.")

while True:

    try:
        text = call_dev()
        if text:
            ask = ask_dev(text)

            if 'exit' in ask:
                break

            elif 'how are you' in ask:
                print("Dev: I am great.")

            elif 'where are you' in ask:
                print("Dev: I am at Cloudedots.")

            elif 'what is 10 + 10' in ask:
                print("Dev: It is 20.")

            elif 'what is 11 + 11' in ask:
                print("Dev: It is 22")

            elif 'what is the total fees collection of this month' in ask:
                print("Dev: It is 10 Lakh.")

            elif 'what is the passing percentage for class 9' in ask:
                print("Dev: It is 90% pass rate this year for class 9th.")
            else:
                print("I didn't hear you. Please try again")
    except:
        print("please try again.")

    if 0xFF == ord('q'):
        break
