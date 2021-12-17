import telebot

from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError
# bot = telebot.TeleBot("1349882772:AAEoP8sexgGSTPNQTrcFdOb9YELthSc2TbU", parse_mode = None)
bot = telebot.TeleBot("1349882772:AAEoP8sexgGSTPNQTrcFdOb9YELthSc2TbU")
owm = OWM("738075ca055cff0d50cb2aa5c263beef")
mgr = owm.weather_manager()


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет бичис, хочешь узнать погоду? Какой город тебя интересует?")
    bot.send_message(message.chat.id, "Только вводи без ошибок ,иначе все нахрен взорвется")

@bot.message_handler(content_types = ['text'])
def send_echo(message):

    if message.text.title() == "Привет":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}.")
    elif message.text.title() == "Hello":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}.")
    elif message.text.title() == "Как Дела?":
        bot.send_message(message.chat.id, f"Нормально. Пиши уже город....мммбеааатч")
    else:
        try:
            observation = mgr.weather_at_place(message.text)

            w = observation.weather
            z = w.temperature('celsius')["temp"]


            answer = f"Текущая температура в городе {message.text} сейчас:  {round(z)} градус/ов.\n\n"

            if z < 0:
                answer += "Холодрыжество! Надевай вторые штаны.\n\n"
            if z < -5:
                answer += "А так же шапку и варежки.\n\n"
            if z < -10:
                answer += "Утепляйся на максимум!!!\n\n"
            if z > 24:
                answer += "Ох,везет же людям...\n\n"

            answer += "Хорошего дня! Спасибо, что пользуетесь нашими сервисами.\n"
            

            bot.send_message(message.chat.id, answer)
        except NotFoundError:
            bot.send_message(message.chat.id, f"{message.text.title()}? Ты это сам придумал? Сказал же,пиши без ошибок...")


bot.polling(none_stop = True)
