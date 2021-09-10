import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'], commands=['start', 'help'])
def handle_start_help(message):
    if message.text == "/start":
        bot.send_sticker(message.chat.id, data=config.StartSticker)
    if message.text == "/help":
        bot.send_sticker(message.chat.id, data=config.HelpSticker)
    bot.send_message(message.chat.id, text="Hello! Im am Linear Algebra helper! Here you can solve several Linal problems! If something does not work, contact to @yeawou! Good luck!")

def test1(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['text'])
def linal(message):
    bot.send_message(message.chat.id, text="salam")


bot.polling(none_stop=True)