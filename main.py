import speech_recognition as spr
import jsonread as student
import speechdev as speak

r1 = spr.Recognizer()
r3 = spr.Recognizer()

student_data = []
welcome_message = "Hi, I am Dev. Developed by Cloudedots."
ask_me = "You can ask me anything related to my knowledge."


def read_student_data():
    student_data.append(student.data)


def call_dev():
    r2 = spr.Recognizer()
    with spr.Microphone() as source:
        r3.adjust_for_ambient_noise(source)
        listen = r3.listen(source)
        text = r2.recognize_google(listen)
        print(f"word: {text}")
        if "dev" in str(text).lower():
            r2 = spr.Recognizer()
            with spr.Microphone() as source:
                message = "What can I help you?"
                print("Example: Ask any below question")
                print("- What is the total fees paid in this year?")
                print("- What is the total fees due for this year?")
                print("- How many students do we have in total?")
                print("- What is the percentage of students who have passed this year?")
                print("- What is the percentage of students who have failed this year?")
                print(f"Yes: please, {message}")
                speak.text(message)
                return r2.listen(source)
        return ""


def ask_dev(speech_text):
    try:
        asked = r3.recognize_google(speech_text)
        print(f"You: {asked}")
        return asked
    except spr.UnknownValueError:
        print(f"Yes: There was an error. Please try again.")
        return ""


print("loading database...")
student_data.append(read_student_data())
print("successfully loaded.\n")

print(f"Yes: {welcome_message}")
speak.text(welcome_message)
print(f"Yes: {ask_me}")
speak.text(ask_me)

while True:
    try:
        text = call_dev()
        print(f"text: {text}")
        if text:
            ask = ask_dev(text)

            if 'exit' in ask:
                break

            elif 'how are you' in ask:
                message = "I am great."
                print(f"Yes: {message}")
                speak.text(message)

            elif 'what is 10 + 10' in ask:
                message = "It is 20."
                print(f"Yes: {message}")
                speak.text(message)

            elif 'what is the total fees paid in this year' in ask or 'total fees collection' in ask:
                searching_message = "I am doing calculation"
                speak.text(searching_message+"...")
                total_received = 0
                print("*"*30)
                print("Name\t\tReceived")
                for student in student_data[0]:
                    received_amount = int(student["fees"]["received"])
                    print(f"{student['name']}\t{received_amount}")
                    total_received += received_amount
                print("*"*30)
                print(f"Total\t\t{total_received}")
                message = f"It is {total_received}"
                print(f"\nYes: {message}")
                speak.text(message)

            elif 'what is the total fees due for this year' in ask or "total fees due" in ask:
                searching_message = "I am doing calculation"
                speak.text(searching_message+"...")
                total_due = 0
                print("*"*30)
                print("Name\t\tDue")
                for student in student_data[0]:
                    received_amount = int(student["fees"]["received"])
                    total_fees = int(student["fees"]["total"])
                    due = total_fees - received_amount
                    print(f"{student['name']}\t{due}")
                    total_due += due
                print("*"*30)
                print(f"Total\t\t{total_due}")
                message = f"It is {total_due}"
                print(f"\nYes: {message}")
                speak.text(message)

            elif 'how many students do we have in total' in ask or "total students" in ask:
                searching_message = "I am doing calculation"
                speak.text(searching_message+"...")
                total_students = 0
                print("*"*30)
                print("Name\t\tClass\t\tSection")
                for student in student_data[0]:
                    print(
                        f"{student['name']}\t{student['class']}\t\t{student['section']}")
                    total_students += 1
                print("*"*30)
                print(f"Total: {total_students}")
                message = f"It is {total_students}"
                print(f"\nYes: {message}")
                speak.text(message)

            elif 'what is the percentage of students who have passed this year' in ask or "total passed percentage" in ask:
                searching_message = "I am doing calculation"
                speak.text(searching_message+"...")
                total_pass = 0
                total_students = 0
                print("*"*30)
                print("Name\t\tResult")
                for student in student_data[0]:
                    if(str(student['result']).lower() == 'pass'):
                        print(f"{student['name']}\t{student['result']}")
                        total_pass += 1
                    total_students += 1
                print("*"*30)
                print(f"Total: {total_pass} out of {total_students}")
                percentage = (total_pass * 100) / total_students
                message = f"It is {percentage:.2f}%"
                print(f"\nYes: {message}")
                speak.text(message)

            elif 'what is the percentage of students who have failed this year' in ask or "total failed percentage" in ask:
                searching_message = "I am doing calculation"
                speak.text(searching_message+"...")
                total_fail = 0
                total_students = 0
                print("*"*30)
                print("Name\t\tResult")
                for student in student_data[0]:
                    if(str(student['result']).lower() == 'fail'):
                        print(f"{student['name']}\t{student['result']}")
                        total_fail += 1
                    total_students += 1
                print("*"*30)
                print(f"Total: {total_fail} out of {total_students}")
                percentage = (total_fail * 100) / total_students
                message = f"It is {percentage:.2f}%"
                print(f"\nYes: {message}")
                speak.text(message)

            else:
                print("I didn't hear you. Please try again")
    except:
        print("please try again.")

    if 0xFF == ord('q'):
        break
