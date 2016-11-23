import os
import subprocess
import telebot
import config

bot = telebot.TeleBot(config.token)

# message.text = text from user
# message = json from user message

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
#    chat = os.system('sudo lsof -Pni:80')
    if message.from_user.username == config.name:
        try:
            chat = subprocess.check_output(message.text, shell=True)
        except:
            chat = sys.exc_info()[1]
        bot.send_message(message.chat.id, chat)
    else:
        bot.send_message(message.chat.id, 'Good try, but no')


if __name__ == '__main__':
    bot.polling(none_stop=True)
