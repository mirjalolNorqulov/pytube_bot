# webhook
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a simple echo bot using decorators and webhook with flask
# It echoes any incoming text messages and does not use the polling method.

import telebot

from flask import Flask, request
from main import bot


server = Flask(__name__)

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://pytube-bot.herokuapp.com/bot")
    return "!", 200

