import telebot

from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError
# bot = telebot.TeleBot("1349882772:AAEoP8sexgGSTPNQTrcFdOb9YELthSc2TbU", parse_mode = None)
bot = telebot.TeleBot("1349882772:AAEoP8sexgGSTPNQTrcFdOb9YELthSc2TbU")
# owm = OWM("738075ca055cff0d50cb2aa5c263beef")
# mgr = owm.weather_manager()
week=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}, напиши день недели,когда не можешь.")


@bot.message_handler(content_types = ['text'])
def send_echo(message):
    day = message.text
    names=""
    i=0
    if day.title() == "Restart":
        week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        bot.send_message(-406662444, f"{message.from_user.first_name} перезапустил голосование. \n\n{', '.join(week)}")


    while i < len(week):
        if day.title() == week[i]:
            del week[i]
            print(week)
            #bot.send_message(564020327, f"{message.from_user.first_name} внес свои коррективы. Свободны следующие дни: \n\n{', '.join(week)}")
            #stef
            #bot.send_message(345505231, f"{message.from_user.first_name} внес свои коррективы. Свободны следующие дни: \n\n{', '.join(week)}")
            #kir
            #bot.send_message(132734082, f"{message.from_user.first_name} внес свои коррективы. Свободны следующие дни: \n\n{', '.join(week)}")
            #egor
            #bot.send_message(180044811, f"{message.from_user.first_name} внес свои коррективы. Свободны следующие дни: \n\n{', '.join(week)}")
            #group
            bot.send_message(-406662444, f"{message.from_user.first_name} внес свои коррективы. Свободны следующие дни: \n\n{', '.join(week)}")
            print(message.chat.id)
            i += 1
        else:
            i += 1



    # if message.text.title() == "Привет":
    #     bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}.")
    # else:
    #     try:
    #         observation = mgr.weather_at_place(message.text)
    #
    #         w = observation.weather
    #         z = w.temperature('celsius')["temp"]
    #
    #
    #         answer = f"Текущая температура в городе {message.text} сейчас:  {round(z)} градус/ов.\n\n"
    #
    #         if z < 0:
    #             answer += "Холодрыжество! Надевай вторые штаны.\n\n"
    #         if z < -5:
    #             answer += "А так же шапку и варежки.\n\n"
    #         if z < -10:
    #             answer += "Утепляйся на максимум!!!\n\n"
    #         if z > 24:
    #             answer += "Ох,везет же людям...\n\n"
    #
    #         #answer += "Хорошего дня! Спасибо, что пользуетесь нашими сервисами.\n"
    #         answer += "Ты пидор!\n"
    #
    #         bot.send_message(message.chat.id, answer)
    #     except NotFoundError:
    #         bot.send_message(message.chat.id, f"{message.text.title()}? Ты это сам придумал? Сказал же,пиши без ошибок...")


bot.polling(none_stop = True)
