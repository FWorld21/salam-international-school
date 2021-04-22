#!/usr/bin/env python3

import telebot
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-i', '--initials', type='string', dest='initials', help='Use this parameter to set INITIALS')
parser.add_option('-p', '--phone', type='string', dest='phone', help='Use this parameter to set PHONE number')
parser.add_option('-c', '--comment', type='string', dest='comment', help='Use this parameter to set COMMENT')
(options, args) = parser.parse_args()

bot_api_file = open('api.txt', 'r')
bot = telebot.TeleBot(bot_api_file.read())
bot_api_file.close()

chat_id_file = open('chat_id.txt', 'r')
chat_id = chat_id_file.read()
chat_id_file.close()
print(chat_id)


message = f'Поступила новая заявка с сайта \n<b>Salam International School</b>: \n\n\
<b>Ф.И.О</b>: <i> {options.initials} </i> \n\
<b>Телефонный номер</b>: <i> {options.phone} </i> \n\
<b>Примечание</b>: <i> {options.comment} </i>'

bot.send_message(chat_id=chat_id, text=message, parse_mode='html')
