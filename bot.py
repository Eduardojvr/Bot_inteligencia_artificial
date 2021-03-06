# _*_ coding: utf-8 _*_
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Bot do dudu')

conv = ['oi','olá, bom dia!', 'bom dia','bom dia, como vai?', 'estou bem']
filmes = ['Qual seu filmes favorito?','Sou um bot, não assisto filmes!']
emocoes = ['tá feliz?', 'tô felizão', 'magoado', 'tô chorando', 'loser','pegou pesado']

bot.set_trainer(ListTrainer)
bot.train(conv)
bot.train(filmes)
bot.train(emocoes)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence > 0.5):
        print('Bot: ', response)
    else:
        print('Não entendi!')
