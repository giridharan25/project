'''
pip install pyttsx3
pip install SpeechRecognition
pip install chatterbot

'''

import pyttsx3
import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


bot= ChatBot("CoCo")
bot.set_trainer(ListTrainer)
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('chatterbot.corpus.english')
print("Say Bye to terminate the convo")


while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    
    try:
        message= r.recognize_google(audio)
        message= message.lower()
        print("you : {}".format(message))
    
    except:
        print("CoCo : Sorry could not recognize your voice")
    
    if message.strip()!="bye":
        reply= bot.get_response(message)
        print("CoCo : ",reply)
        speak(reply)
      
    if message.strip()=="bye":
        print("CoCo : Bye, see you")
        speak("bye see you later") 
        break

def speak(x):
    
    engine= pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
    
    

        
