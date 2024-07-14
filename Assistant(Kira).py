import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
count = 0
def say(text):
    engine.say(text)
    engine.runAndWait()
def start():
    print('Hello, myself Kira, how may i help you')
    say('Hello, myself Kira, how may i help you')

start()
def input_command():
    command = ""
    try:
        with sr.Microphone() as source:
            
            print("Listening...")
            say('im Listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Alexa' in command:
                command = command.replace('Kira','')


    except:
        pass
    return command
def run_alexa():
    command = input_command()
    print(command)
    if 'play' in command:
        video = command.replace('play ','')
        say('Opening you tube')
        say('Playing' + video)
        pywhatkit.playonyt(video)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I : %M ') #b= month a=week c= everything g= year
        print(time)
        # time = time.replace(':','')
        say('The time s'+time)
    elif 'who is' in command:
        search = command.replace('who is ','')
        Info = wikipedia.summary(search,1)
        print(Info)
        say(Info)
    elif 'what is an ' in command:
        search = command.replace('what is an ','')
        Info = wikipedia.summary(search,1)
        print(Info)
        say(Info)
    elif 'what is a ' in command:
        search = command.replace('what is a ','')
        Info = wikipedia.summary(search,1)
        print(Info)
        say(Info)
    elif 'what is the ' in command:
        search = command.replace('what is the ','')
        Info = wikipedia.summary(search,1)
        print(Info)
        say(Info)
    elif 'define' in command:
        search = command.replace('define ', '')
        Info = wikipedia.summary(search,1)
        say(f'The definition of {search} is...')
        say(Info)
    elif 'how are you' in command:
        say('I\'m good, hope you\'re good too')
    elif 'joke' in command:
        say(pyjokes.get_joke())
    elif 'hello' in command:
        say('Hello , hope you are doing good')
    elif 'thank you' in command:
        say('Nice talking to you, see you again')
    else:
        print('Hey, i dint herd that please say it again')
        say('Hey, i dint herd that please say it again')
        no_response()

def no_response():
    global count
    count+=1
    print(count)
    if count  == 3:
        say('Can i say a joke for you')
        command=input_command()
        if command == 'yes':
            say(pyjokes.get_joke())
        else:
            count = 0
    else:
        input_command()

while True:
    run_alexa()

