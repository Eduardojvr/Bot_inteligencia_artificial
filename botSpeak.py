# _*_ coding: utf-8 _*_

#imports do bot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
# imports do reconhecimento de voz
import speech_recognition as sr
import pyttsx3
#import objc


bot = ChatBot('Bot do dudu')
speak = pyttsx3.init()

def Speak(text):  
    speak.say(text)
    speak.runAndWait() 

conv = ['Hi','Hello','How are you', 'I"m fine, thanks', 'whats your name?','my name is Bot']

bot.set_trainer(ListTrainer) #define o método de treinamento
bot.train(conv) #define as listas de conversas


voz = sr.Recognizer()

with sr.Microphone() as s:
    voz.adjust_for_ambient_noise(s) # se adapta ao ruido

    while True:
        try:
            audio = voz.listen(s) # escuta a fala
            #speech = voz.recognize_google(audio, language='pt') # pega a fala
            speech = voz.recognize_google(audio) # pega a fala    
            response = bot.get_response(speech)
            print('Você: ',speech)
            print('Bot: ', response)
            Speak(response)
        except:
            pass
