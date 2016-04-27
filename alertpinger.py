import telebot
import constants
import pinger
import time

bot = telebot.TeleBot(constants.token)

def timetoping():
    pinger.startping()

    if pinger.aaa == 1:
        bot.send_message(constants.chatid, "10.0.1.10 is down")

    if pinger.bbb == 1:
        bot.send_message(constants.chatid, "10.0.1.11 is down")

    if pinger.ccc == 1:
        bot.send_message(constants.chatid, "10.0.1.12 is down")

    if pinger.ddd == 1:
        bot.send_message(constants.chatid, "10.0.1.16 is down")

    time.sleep(5);

    timetoping()

timetoping()