import speech_recognition as spr
import jsonread as student
import speechdev as speak

student_data = []
welcome_message = "Hi, I am Hello. Developed by Cloudedots."
ask_me = "You can ask me anything related to my knowledge."

# func:1 get student data


def read_student_data():
    student_data.append(student.data)

# func: 2 call hello


def call_hello():
    r2 = spr.Recognizer()
    with spr.Microphone() as source:
        listen = r2.listen(source)
        text = r2.recognize_google(listen)
        print(f'You said: {text}')
        if "hello" in str(text).lower():
            print("\nList of questions you can ask me:")
            print("1) What is the total fees paid in this year?")
            print("2) What is the total fees due for this year?")
            print("3) How many students do we have in total?")
            print("4) What is the percentage of students who have passed this year?")
            print("5) What is the percentage of students who have failed this year?")
            print("0) Say 'Exit' - To exit the program. \n")
            message = "What can I help you?"
            print(f"Hello: {message}")
            speak.text(message)
        else:
            print('Say "hello" again...')
            call_hello()


def ask_hello():
    r2 = spr.Recognizer()
    with spr.Microphone() as source:
        command = r2.listen(source)
        asked = r2.recognize_google(command)
        print(f"You asked: {asked}")
        return asked
    return ""


def hello_answer(ask):

    if 'exit' in ask:
        raise SystemExit

    elif 'how are you' in ask:
        message = "I am great."
        print(f"Hello: {message}")
        speak.text(message)
        print("Say 'hello' now")

    elif 'what is 10 + 10' in ask:
        message = "It is 20."
        print(f"Hello: {message}")
        speak.text(message)
        print("Say 'hello' now")

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
        print(f"\nHello: {message}")
        speak.text(message)
        print("Say 'hello' now")

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
        print(f"\nHello: {message}")
        speak.text(message)
        print("Say 'hello' now")

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
        print(f"\nHello: {message}")
        speak.text(message)
        print("Say 'hello' now")

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
        print(f"\nHello: {message}")
        speak.text(message)
        print("Say 'hello' now")

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
        print(f"\nHello: {message}")
        speak.text(message)
        print("Say 'hello' now")
    else:
        message = "I did't get you. Can you repeat it again, please?"
        speak.text(message)
        print("Speack now.")
        asked = ask_hello()
        hello_answer(asked)


print("Connecting to the SLIM database...")
student_data.append(read_student_data())
print("Successfully connected.\n")

print(f"Hello: {welcome_message}")
speak.text(welcome_message)
print(f"Hello: {ask_me}")
speak.text(ask_me)
print("Say 'hello' now")

while True:
    try:
        call_hello()
        asked = ask_hello()
        hello_answer(str(asked).lower())
    except:
        print("There was problem. Please re-run program again.")
        raise SystemExit
