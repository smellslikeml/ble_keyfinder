#!/usr/bin/env python
import os
import sys
import pickle
from flask import Flask
from flask_ask import Ask, statement
sys.path.append('./mdls')
from predict import loc_predict

app=Flask(__name__)
ask = Ask(app, '/')

mdl_ = pickle.load(open('bt_model.dat', 'rb'))

@ask.intent('findkeys')
def retrievr():
    os.system('sound_alarm.py &')
    speech_text = guess_locate()
    print(speech_text)
    return statement(speech_text).standard_card(title='Retrievr says...', text=speech_text)


def guess_locate():
    reply_str = loc_predict(mdl_)
    return reply_str


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
