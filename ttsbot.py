import time
import re
import random
import datetime
import telepot
from subprocess import call
import subprocess
import os
import sys
from telepot.loop import MessageLoop
import base64 
import uuid
from pyttsreverso import pyttsreverso 

language=os.getenv('TTS_LANG')
pitch = os.getenv('TTS_PITCH')
bitrate = os.getenv('TTS_BITRATE')
bot_api_key = os.getenv('BOT_API_KEY')
data_file=''

def tts_convert(msg,chat_id):
    global data_file
    global language
    global speed
    global bitrate

    message_bytes = msg.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    convert = pyttsreverso.ReversoTTS()
    data = convert.convert_text(voice=language, pitch=pitch, bitrate=bitrate, msg=msg)
    f = open(data_file , 'w+b')
    f.write(data)
    f.close()
    return data


def handle(msg):
    global data_file
    chat_id = msg['chat']['id']
    command = msg['text']
    data_file = str('./' + ' '.join(command.split(' ')[:3]) + '.mp3')
    tts_convert(command,chat_id)
    bot.sendAudio(chat_id,open(data_file, 'rb'),'Voice')
    os.remove(data_file)


bot = telepot.Bot(bot_api_key)
MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')
 
while 1:
    time.sleep(10)
