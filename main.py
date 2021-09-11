import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

theoryAndCalculatingMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
theoryButton = types.KeyboardButton("Theory")
calcButton = types.KeyboardButton("Calculating")
theoryAndCalculatingMarkup.add(theoryButton, calcButton)

@bot.message_handler(content_types=['text'], commands=['start', 'help'])
def handle_start_help(message):



    if message.text == "/start":
        bot.send_sticker(message.chat.id, data=config.StartSticker)
        bot.send_message(message.chat.id,
                         text="Hello, {0.first_name}!\nI am <b>{1.first_name}</b>, and I am <b>LinAl bot</b>. \nI hope I can help you somehow. ❤️".format(
                             message.from_user, bot.get_me()), parse_mode='HTML', reply_markup=theoryAndCalculatingMarkup)
    if message.text == "/help":
        bot.send_sticker(message.chat.id, data=config.HelpSticker)
        bot.send_message(message.chat.id, text="Use buttons to navigate!", reply_markup=theoryAndCalculatingMarkup)


def test1(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['text'])
def messageChecker(message):
    if message.chat.type == 'private':
        if message.text == 'Theory':
            theory(message)
        elif message.text == "Calculating":
            calculating(message)
        else:
            bot.send_message(message.chat.id, text="Sorry, unknown command, please, check your input.")

def theory(message):

    themesMarkup = types.InlineKeyboardMarkup(row_width=1)
    themes = config.themes
    for i in range(len(themes)):
        item = types.InlineKeyboardButton(themes[i], callback_data=str(i))
        themesMarkup.add(item)

    bot.send_message(message.chat.id, text="Here are some themes. Select anything:", reply_markup=themesMarkup)

def calculating(message):
    bot.send_message(message.chat.id, text="Calculating in progress...")


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            for i in range(len(config.themes)):
                if call.data == str(i):
                    bot.send_message(call.message.chat.id, config.linksToThemes[i])
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Here are some themes. Select anything:",
                                  reply_markup=None)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)