import telebot
import config as cnf
import os
import random
from gtts import gTTS

language = "ru"
random.seed(version=2)

bot = telebot.TeleBot(cnf.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(
        message.chat.id, f"Гоу.",
    )


@bot.message_handler(commands=["isalive"])
def cmd_isalive(message):
    bot.send_message(
        message.chat.id, f"Yes, I am",
    )


@bot.message_handler(commands=["anekdot"])
def cmd_anekdot(message):
    msg = bot.send_message(message.chat.id, "А ну давай")
    bot.register_next_step_handler(msg, tts)


def tts(message):
    speech = gTTS(text=message.text, lang=language, slow=False)
    speech.save("anekdot.mp3")
    audio = open("anekdot.mp3", "rb")
    bot.send_audio(message.chat.id, audio)


# @bot.message_handler(content_types=["sticker"])
# def get_sticker_id(message):
#     bot.send_message(message.chat.id, message.sticker.file_id)


@bot.message_handler(func=lambda x: True)
def user(message):
    if message.from_user.id == 587575071:
        num = random.randint(0, 4)
        if num == 0:
            bot.send_message(message.chat.id, "Олег, это ты?")
            bot.send_message(message.chat.id, "пошел нахуй")
        if num == 1:
            bot.send_sticker(
                message.chat.id,
                "CAACAgIAAxkBAAIB8V6fMLAEfjhmkBHzfAvPFo2zsuqQAAJsAAMuJbMT9RhhXYwmlk8YBA",
            )
        if num == 2:
            bot.send_sticker(
                message.chat.id,
                "CAACAgIAAxkBAAIB816fMTU3qlmp4as_l6M6P73lERo-AAJwAAMuJbMT-_hDJquudNcYBA",
            )
        if num == 3:
            bot.send_sticker(
                message.chat.id,
                "CAACAgIAAxkBAAIB916fMXjrGpJfryjZmVJ53Z5qj0KHAALEAAMuJbMTZ6K63oB38bQYBA",
            )
        if num == 4:
            bot.send_message(message.chat.id, "Не в этот раз, Олег")
    if message.from_user.id == 491143055:
        bot.send_message(message.chat.id, "Паша, здорова!")
    if message.from_user.id == 312301600:
        pass
        # bot.send_message(message.chat.id, "Папай, здорова!")
    # bot.send_message(message.chat.id, "пошел нахуй")


bot.polling()
