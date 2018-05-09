# _*_ coding: utf-8 _*_

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conv = ['oi','olá, bom dia!', 'bom dia','bom dia, como vai?', 'estou bem', 'bot burro', 'voce seu merda!']

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Bot: ', response)