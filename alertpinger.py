import telebot
import constants
import pinger
import time

bot = telebot.TeleBot(constants.token)

def timetoping():
    pinger.startping()

    if pinger.aaa == 1:
        bot.send_message(constants.chatid, "srv1 is down")

    if pinger.bbb == 1:
        bot.send_message(constants.chatid, "srv2 is down")

    if pinger.ccc == 1:
        bot.send_message(constants.chatid, "srv3 is down")

    if pinger.ddd == 1:
        bot.send_message(constants.chatid, "srv4 is down")

    time.sleep(5);

    timetoping()

timetoping()
