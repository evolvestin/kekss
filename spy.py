# -*- coding: utf-8 -*-
#equip

import telebot
from telebot import types
import urllib3
import re
import requests
import time
from time import sleep
import datetime
from datetime import datetime
import _thread

#=================================================================
token = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"
bot = telebot.TeleBot(token)

clkwait = 61
coltwink = 23
globtime = 0
beatva = 0
timefort = 0

less = '🌲'
morfort = '⚓️'
gori = '⛰'
mo = '🇲🇴'
gp = '🇬🇵'
cy = '🇨🇾'
va = '🇻🇦'
im = '🇮🇲'
eu = '🇪🇺'
ki = '🇰🇮'
atk = '⚔️'
deff = '🛡'
eq = '🎽'
gold = '💰'
moon = '🌑'
hmm = '🤔'

idMe = 396978030
idBlack = 394850016
idDBlack = 200299701 #MISSSPACEX
idBlue = 491625180
idDBlue = 541062392 #NAMI_LEE
idYellow = 392562894 #Gummy
idYellow2 = 242839185 #M_ONYA
idDYellow = 485591553
idWhite = 430602902
idRed = 555979421 #DARETEN
idRed2 = 200299701 #MISSSPACEX
idDRed = 497892874
idTwilight = 462139760 #NAMI_LEE
idDTwilight = 350037139
idMoon = 130875246 #RDVRK

idChatPeregovorka = -1001175146945
idChatCommandirka = -1001116128920
idChannelPins = -1001290002880

urlClear = 'http://bitlux.ru/evolve.php?text=none'
urldo = 'http://bitlux.ru/evolve.php?text='
urlcoldonate = 'http://bitlux.ru/donate.php?donate='
urleq = 'http://bitlux.ru/equip.html'
urleqlog = 'http://bitlux.ru/equip.php?eq='
#====================================================================================
starttime = int(datetime.utcfromtimestamp(int(int(datetime.now().timestamp()) + 3 * 60 * 60)).strftime('%H'))
if starttime == 16 or starttime == 17 or starttime == 18 or starttime == 19:
    keyboardst = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboardst.row(less + 'Лес', mo, eq + 'Экипировка')
    keyboardst.row(gp, cy, va)
    keyboardst.row(im, eu, ki)
    keyboardst.row(less + 'Лесной форт', gori + 'Горный форт', morfort + 'Морской форт')
else:
    keyboardst = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboardst.row(less + 'Лес', mo, eq + 'Экипировка')
    keyboardst.row(gp, cy, va)
    keyboardst.row(im, eu, ki)
bot.send_message(idMe, "<i>._.</i>", reply_markup=keyboardst, parse_mode='HTML')


def prikaz():
    time.sleep(clkwait)
    content = requests.get(urlClear)
    bot.send_message(idMe, '<i>Исполнено</i>', reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(commands=['time'])
def handle_chas_command(message):
    global globtime
    global beatva
    global timefort
    if beatva == 'da':
        bot.send_message(message.chat.id, '<b>БИТВА СКОРО!</b>\nСмотрите, время тикает: ' + globtime, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Время: ' + str(globtime))


@bot.message_handler(commands=['berman'])
def handle_berman_command(message):
    global globtime
    global seconds
    if seconds == 0 or seconds == 10 or seconds == 11 or seconds == 20 or seconds == 21 or seconds == 30 or seconds == 31 or seconds == 40 or seconds == 41 or seconds == 50 or seconds == 51:
        bot.send_message(message.chat.id, 'Только что в мире умер один человек, почтим его память тремя секундами перемирия')
        sleep(3)
        bot.send_message(message.chat.id, 'Траур завершен, у вас есть 7 секунд, чтобы успеть повоевать')
    else:
        bot.send_message(message.chat.id, 'Траур завершен, у вас есть ~7 секунд, чтобы успеть повоевать')



@bot.message_handler(commands=['id'])
def handle_id_command(message):
    orbo = message.chat.id
    if orbo > 0:
        bot.send_message(message.chat.id, "Твой ID: " + str(orbo))
    elif orbo < 0:
        bot.send_message(message.chat.id, "ID этой группы: " + str(orbo))


@bot.callback_query_handler(func=lambda call: True)
def callback_equip(call):
    global clkwait
    global keyboard
    global zader
    if call.message.chat.id == idMe:
        if call.data == 'attack':
            bot.edit_message_text(chat_id=call.message.chat.id, text=atk + 'Шмот надеваем <code>(' + str(zader) + ')</code>', message_id=call.message.message_id, parse_mode='HTML')
            content = requests.get(urldo + 'Attack')
            prikaz()
            content = requests.get(urleqlog + 'Attack')
        elif call.data == 'defend':
            bot.edit_message_text(chat_id=call.message.chat.id, text=deff + 'Шмот надеваем <code>(' + str(zader) + ')</code>', message_id=call.message.message_id, parse_mode='HTML')
            content = requests.get(urldo + 'Defend')
            prikaz()
            content = requests.get(urleqlog + 'Defend')

@bot.message_handler(content_types=["new_chat_members"])
def get_new_member(message):
    if message.new_chat_member is not None and message.new_chat_member.username == 'whgklwehgwklejw_bot':
        bot.send_message(message.chat.id, 'Меня добавили в какой-то чат, пидорасы')
        bot.send_message(idMe, 'Меня добавили в какой-то чат, пидорасы')

@bot.message_handler(func=lambda message: message.text)
def repeat_all_messages(message):
    global globtime
    global clkwait
    global zader
    global keyboard
    global timefort

    if message.forward_date is not None:
        origmes = message.forward_date
        origmesH = datetime.utcfromtimestamp(int(origmes + 3 * 60 * 60)).strftime('%H')
        origmesM = datetime.utcfromtimestamp(int(origmes)).strftime('%M')
        origmesS = datetime.utcfromtimestamp(int(origmes)).strftime('%S')
        origtime = ' <code> ' + str(origmesH) + ':' + str(origmesM) + ':' + str(origmesS) + '[F]</code>'
    else:
        origtime = ' <code> ' + str(globtime) + '</code>'

    specmessage = '<code>: </code>' + message.text + origtime

    if timefort == 0:
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row(less + 'Лес', mo, eq + 'Экипировка')
        keyboard.row(gp, cy, va)
        keyboard.row(im, eu, ki)
    else:
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row(less + 'Лес', mo, eq + 'Экипировка')
        keyboard.row(gp, cy, va)
        keyboard.row(im, eu, ki)
        keyboard.row(less + 'Лесной форт', gori + 'Горный форт', morfort + 'Морской форт')

    if message.chat.id == idDBlack and message.forward_date is not None:
        if str(message.forward_from.username) == 'CWRedBot':
            bot.send_message(idChatCommandirka, atk + im + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + im + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ToweRobot':
            bot.send_message(idChatCommandirka, deff + gp + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, deff + gp + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')

    elif message.chat.id == idRed:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, atk + im + '<code>(Dareten)</code>' + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + im + '<code>(Dareten)</code>' + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, atk + im + '<code>(Dareten)</code>' + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + im + '<code>(Dareten)</code>' + specmessage, parse_mode='HTML')

    elif message.chat.id == idDRed:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, deff + im + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, deff + im + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, deff + im + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, deff + im + specmessage, parse_mode='HTML')

    elif message.chat.id == idBlack:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, atk + gp + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + gp + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, atk + gp + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + gp + specmessage, parse_mode='HTML')

    elif message.chat.id == idBlue:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, atk + eu + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + eu + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, atk + eu + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + eu + specmessage, parse_mode='HTML')

    elif message.chat.id == idDBlue:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, atk + eu + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + eu + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, atk + eu + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + eu + specmessage, parse_mode='HTML')

    elif message.chat.id == idYellow or message.chat.id == idYellow2:
        if str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, atk + va + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + va + specmessage, parse_mode='HTML')


    elif message.chat.id == idDYellow:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, deff + va + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, deff + va + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, deff + va + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, deff + va + specmessage, parse_mode='HTML')

    elif message.chat.id == idWhite:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, atk + cy + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + cy + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        else:
            bot.send_message(idChatCommandirka, atk + cy + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, atk + cy + specmessage, parse_mode='HTML')

    elif message.chat.id == idDTwilight:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, deff + ki + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, deff + ki + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ChatWarsBot':
            bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
            bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
        elif str(message.forward_from.username) == 'TwilightCastleBot':
            bot.send_message(idChatCommandirka, deff + ki + prikazTwilight(message), parse_mode='HTML')
            bot.send_message(idChannelPins, deff + ki + prikazTwilight(message), parse_mode='HTML')
        else:
            bot.send_message(idChatCommandirka, deff + ki + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, deff + ki + specmessage, parse_mode='HTML')

    elif message.chat.id == idTwilight:
        if message.forward_from is None:
            bot.send_message(idChatCommandirka, ki + specmessage, parse_mode='HTML')
            bot.send_message(idChannelPins, ki + specmessage, parse_mode='HTML')
        elif message.forward_from is not None:
            if str(message.forward_from.username) == 'ChatWarsBot':
                bot.send_message(idChatCommandirka, forwardCW(message), parse_mode='HTML')
                bot.send_message(message.chat.id, 'Ваш репорт был отправлен куда нужно, но без указания ника. Вы в безопасности')
            elif str(message.forward_from.username) == 'TwilightCastleBot':
                bot.send_message(idChatCommandirka, ki + prikazTwilight(message), parse_mode='HTML')
                bot.send_message(idChannelPins, ki + prikazTwilight(message), parse_mode='HTML')
            else:
                bot.send_message(idChatCommandirka, ki + specmessage, parse_mode='HTML')
                bot.send_message(idChannelPins, ki + specmessage, parse_mode='HTML')

    elif message.chat.id == idMoon:
        if message.forward_from is None:
            bot.send_message(message.chat.id, 'Без форварда' + hmm + ' Ладно, отправлю.', parse_mode='HTML')
            bot.send_message(idMe, moon + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'MoonlightCastleBot':
            bot.send_message(idMe, moon + specmessage, parse_mode='HTML')
            bot.send_message(message.chat.id, '<i>Отправлено</i>', parse_mode='HTML')

    elif message.chat.id == idMe:
        if message.text == less + 'Лес':
            bot.send_message(idMe, 'Идем в' + less + 'Лес <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'les')
            prikaz()

        elif message.forward_from is not None:
            if str(message.forward_from.username) == 'ChatWarsBot':
                bot.send_message(idMe, forwardCW(message), parse_mode='HTML')

        elif message.text == less + 'Лесной форт':
            bot.send_message(idMe, 'Идем в ' + less + 'Лесной форт <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'lesfort')
            prikaz()
        elif message.text == morfort + 'Морской форт':
            bot.send_message(idMe, 'Идем в ' + morfort + 'Морской форт <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'morfort')
            prikaz()
        elif message.text == gori + 'Горный форт':
            bot.send_message(idMe, 'Идем в ' + gori + 'Горный форт <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'gorifort')
            prikaz()

        elif str(message.text).startswith('/donate'):
            donate = message.text
            donate = donate.replace('/donate ', '')
            donateform = urlcoldonate + donate
            content = requests.get(urldo + 'donate')
            content = requests.get(donateform)
            donate = int(donate) * coltwink
            bot.send_message(idMe, 'Вдонатить ~' + str(donate) + ' <code> (' + str(zader) + ')</code>', parse_mode='HTML')
            prikaz()

        elif message.text == eq + 'Экипировка':
            equiplog = requests.get(urleq).text
            if equiplog == 'Attack':
                equiplog = atk + 'Атакерская'
            elif equiplog == 'Defend':
                equiplog = deff + 'Деферская'
            keyroad = types.InlineKeyboardMarkup(row_width=2)
            buttons = []
            buttons.append(types.InlineKeyboardButton(text=atk + 'Шмот', callback_data='attack'))
            buttons.append(types.InlineKeyboardButton(text=deff + 'Шмот', callback_data='defend'))
            keyroad.add(*buttons)
            bot.send_message(idMe, eq + 'Экипировка: ' + equiplog, reply_markup=keyroad, parse_mode='HTML')

        elif message.text == mo or message.text == gp or message.text == cy or message.text == va or message.text == im or message.text == eu or message.text == ki:
            bot.send_message(idMe, 'Идем в ' + message.text + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
            if message.text == mo:
                content = requests.get(urldo + 'mo')
            elif message.text == gp:
                content = requests.get(urldo + 'gp')
            elif message.text == cy:
                content = requests.get(urldo + 'cy')
            elif message.text == va:
                content = requests.get(urldo + 'va')
            elif message.text == im:
                content = requests.get(urldo + 'im')
            elif message.text == eu:
                content = requests.get(urldo + 'eu')
            elif message.text == ki:
                content = requests.get(urldo + 'ki')
            prikaz()


def prikazTwilight(message):
    origmes = message.forward_date
    origmesH = datetime.utcfromtimestamp(int(origmes + 3 * 60 * 60)).strftime('%H')
    origmesM = datetime.utcfromtimestamp(int(origmes)).strftime('%M')
    origmesS = datetime.utcfromtimestamp(int(origmes)).strftime('%S')
    origtime = ' <code> ' + str(origmesH) + ':' + str(origmesM) + ':' + str(origmesS) + '[F]</code>'
    search = re.search('(\n\nГотовность\n)', message.text)
    if search:
        delprikaz = message.text.replace(search.group(1), '')
        i = 1
        srch = re.search("(@.*)", delprikaz)
        while srch:
            delprikaz = delprikaz.replace(srch.group(1), '')
            srch = re.search("(@.*)", delprikaz)
        delprikaz = '<code>: </code>' + delprikaz + origtime

        return delprikaz
    else:
        delprikaz = '<code>: </code>' + message.text + origtime
        return delprikaz


def forwardCW(message):
    zamki = '(' + mo + '|' + gp + '|' + im + '|' + cy + '|' + va + '|' + eu + '|' + ki + ')'
    repsearch = re.search(zamki + '(.+)' + atk + ':', message.text)
    kazsearch = re.search(zamki + '(.+)( замок)', message.text)
    CWtime = message.forward_date
    CWtimeD = str(datetime.utcfromtimestamp(int(CWtime)).strftime('%d'))
    CWtimeM = str(datetime.utcfromtimestamp(int(CWtime)).strftime('%m'))
    CWtimeY = str(datetime.utcfromtimestamp(int(CWtime)).strftime('%Y'))
    CWtimeH = int(datetime.utcfromtimestamp(int(CWtime + 3 * 60 * 60)).strftime('%H'))
    CWtimeHour = datetime.utcfromtimestamp(int(CWtime + 3 * 60 * 60)).strftime('%H')
    CWtimeMin = datetime.utcfromtimestamp(int(CWtime)).strftime('%M')
    CWtimeS = datetime.utcfromtimestamp(int(CWtime)).strftime('%S')
    if repsearch:
        report = message.text.replace(repsearch.group(2), '')
        if CWtimeH > -1 and CWtimeH < 4:
            repchas = '0 часов'
        if CWtimeH > 3 and CWtimeH < 8:
            repchas = '4 часа'
        if CWtimeH > 7 and CWtimeH < 12:
            repchas = '8 часов'
        if CWtimeH > 11 and CWtimeH < 16:
            repchas = '12 часов'
        if CWtimeH > 15 and CWtimeH < 20:
            repchas = '16 часов'
        if CWtimeH > 19 and CWtimeH < 24:
            repchas = '20 часов'
        repdate = CWtimeD + '.' + CWtimeM + '.' + CWtimeY + ' в ' + repchas
        report = report + '\n <code>Битва ' + str(repdate) + '</code>'
        return report
    elif kazsearch:
        kazflag = kazsearch.group(1)
        kazname = kazsearch.group(2)
        kazsearch = re.search('(Казна замка:\n)([0-9]+)' + gold + ' ([0-9]+)' + less + ' ([0-9]+)' + gori, message.text)
        if kazsearch:
            kaznatime = '<code>' + str(CWtimeHour) + ':' + str(CWtimeMin) + ':' + str(CWtimeS) + '[F]</code>'
            kazna = kazflag + kazname + ':' + '\n' + kazsearch.group(2) + gold + ' ' + kazsearch.group(3) + less + ' ' + kazsearch.group(4) + gori + '\n' + kaznatime
            return kazna
        kazna = 'Странная у тебя казна...'
        return kazna
    else:
        report = 'Форварды из ЧВ отключены (кроме репортов и казны), ради вашей безопасности'
        return report


def bitva_detector():
    global globtime
    global clkwait
    global hours
    global minutes
    global curr_time
    global zader
    global beatva
    global seconds
    while True:
        try:
            sleep(0.3)
            curr_time = int(datetime.now().timestamp())
            hourso = datetime.utcfromtimestamp(int(curr_time + 3 * 60 * 60)).strftime('%H')
            minuteso = datetime.utcfromtimestamp(int(curr_time)).strftime('%M')
            secondso = datetime.utcfromtimestamp(int(curr_time)).strftime('%S')
            hours = int(datetime.utcfromtimestamp(int(curr_time + 3 * 60 * 60)).strftime('%H'))
            minutes = int(datetime.utcfromtimestamp(int(curr_time)).strftime('%M'))
            seconds = int(datetime.utcfromtimestamp(int(curr_time)).strftime('%S'))
            globtime = str(hourso) + ':' + str(minuteso) + ':' + str(secondso)
            if hours == 3 or hours == 7 or hours == 11 or hours == 15 or hours == 19 or hours == 23:
                if minutes < 30:
                    clkwait = 30 + 1 # плюс доп задержка
                    beatva = 'net'
                elif minutes > 30 and minutes < 50:
                    beatva = 'da'
                    clkwait = 15 + 1 # плюс доп задержка
                elif minutes > 50 and minutes < 58:
                    beatva = 'da'
                    clkwait = 8 + 1 # плюс доп задержка
                elif minutes > 58 and minutes < 59:
                    beatva = 'da'
                    clkwait = 1 + 1 # плюс доп задержка
                elif minutes > 59 and seconds > 0:
                    clkwait = 1 + 1 # плюс доп задержка
                    if seconds > 40:
                        clkwait = 0.3 + 0.1 # плюс доп задержка
            else:
                clkwait = 60 + 1 # плюс задержка
                beatva = 'net'

            zader = clkwait - 1
        except Exception as e:
            sleep(0.3)


def merc_detector():
    global hours
    global minutes
    global curr_time
    global keyboard
    while True:
        try:
            sleep(1)
            merc_sec = int(datetime.utcfromtimestamp(int(curr_time)).strftime('%S'))
            if hours == 3 or hours == 7 or hours == 11 or hours == 15 or hours == 19 or hours == 23:
                if merc_sec == 25 and minutes == 59:
                    bot.send_message(idChatCommandirka, "Woop-woop! That's the sound of da ebolbo-police!", parse_mode='HTML')
                elif merc_sec == 30 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 35 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 40 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 45 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 50 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 55 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
            elif hours == 4 or hours == 8 or hours == 12 or hours == 16 or hours == 20 or hours == 24:
                if merc_sec == 0 and minutes == 0:
                    bot.send_message(idChatCommandirka, '00:00', parse_mode='HTML')
                elif merc_sec == 3 and minutes == 0:
                    bot.send_message(idChatCommandirka, '<i>Опасность миновала. Можете продолжать ничего не делать.</i>', parse_mode='HTML')
        except Exception as e:
            sleep(1)


def fort_detector():
    global timefort
    global hours
    while True:
        try:
            sleep(60)
            if hours == 16 or hours == 17 or hours == 18 or hours == 19:
                timefort = 1
            else:
                timefort = 0
        except Exception as e:
            sleep(60)

def telepol():
    try:
        bot.polling(none_stop=True, timeout=60)
    except:
        bot.stop_polling()
        sleep(5)
        telepol()

if __name__ == '__main__':
    _thread.start_new_thread(bitva_detector, ())
    _thread.start_new_thread(fort_detector, ())
    _thread.start_new_thread(merc_detector, ())
    telepol()
