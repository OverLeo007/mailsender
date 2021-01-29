
import random
import urllib.parse
import os
from time import sleep
from spoofer.models.smtpconnection import SMTPConnection
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from new_window import Ui_App
import sys
import re

uencode = urllib.parse.quote
issub, ispost, ismails, isfmails, issmtp, iss_name = True, True, True, True, True, True
devider = '#'

if 'subjects.txt' not in os.listdir():
    file = open('subjects.txt', 'w').close()
if 'posts' not in os.listdir():
    os.mkdir('posts')
if 'addr.txt' not in os.listdir():
    file = open('addr.txt', 'w').close()
if 'fromaddr.txt' not in os.listdir():
    file = open('fromaddr.txt', 'w').close()
if 'smtpaccs.txt' not in os.listdir():
    file = open('smtpaccs.txt', 'w').close()
if 'sendernames.txt' not in os.listdir():
    file = open('sendernames.txt', 'w').close()

with open('subjects.txt') as subs:
    if not subs.readlines():
        issub = False
if not os.listdir(f'{os.getcwd()}\\posts'):
    ispost = False
with open('addr.txt') as names:
    if not names.readlines():
        ismails = False
with open('fromaddr.txt') as fnames:
    if not fnames.readlines():
        isfmails = False
with open('smtpaccs.txt') as smtps:
    if not smtps.readlines():
        issmtp = False
with open('sendernames.txt') as snms:
    if not snms.readlines():
        iss_name = False


def resource_path(relative):
    # функция позволяющая импортироать файлы при компиляции
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


def msend(sender, sender_name, recipient, subject, html, smtp):
    connection = SMTPConnection(smtp['host'], str(smtp['port']))
    connection.login(smtp['login'], smtp['password'])
    message = connection.compose_message(
        sender,
        sender_name,
        recipient,
        subject,
        html
    )
    status = connection.send_mail(message)
    return status


def dir_to_list(dir):
    dlist = []
    os.chdir(f'{os.getcwd()}\\{dir}')
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as tfile:
            dlist.append(''.join(tfile.readlines()))
    os.chdir(os.getcwd().replace(f'\\{dir}', ''))
    return dlist


def rand(arr):
    return random.choice(arr)


def make_sy_text(text):
    newtext = []
    for string in text.split('\n'):
        count = 0
        synonims = []
        for word in string.split(' '):
            if devider in word:
                string = string.replace(word, f'{devider}{count}')
                synonims.append(word.split(devider))
                count += 1

        if synonims:
            string = [synonims, string]
            newtext.append({'syn': synonims, 'str': string[1]})
        else:
            newtext.append({'str': string})

    for num, string in enumerate(newtext):
        sn_syn = re.findall('{(.*?)}', string['str'])
        if sn_syn:
            for x, syns in enumerate(sn_syn):
                sn_syn[x] = syns.split('/')
            for syns in sn_syn:
                newtext[num]['str'] = re.sub('{(.*?)}', rand(syns), newtext[num]['str'], count=1)
    restext = []
    for string in newtext:

        if string.get('syn', False):
            for ind, syn in enumerate(string['syn']):
                string['str'] = string['str'].replace(f'#{ind}', rand(syn), 1)
        restext.append(string['str'])

    restext = '\n'.join(restext)
    return restext


class Display(QMainWindow, Ui_App):
    # создание окна отображения данных
    def __init__(self):
        self.scount = 0
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))

        self.startButton.clicked.connect(self.main)

        if issmtp is False:
            self.log_browser.append(
                'Заполни файлик smtpaccs.txt смтп аккаунтами в формате smtp:port:login:password (каждое с новой строки)')
        if issub is False:
            self.log_browser.append('Заполни файлик subjects.txt темами (каждая с новой строки)')
        if ispost is False:
            self.log_browser.append('Заполни директорию posts письмами (каждое .txt)')
        if ismails is False:
            self.log_browser.append('Заполни файлик addr.txt почтами (каждая с новой строки)')
        if isfmails is False:
            self.log_browser.append('Заполни файлик fromaddr.txt почтами с которых отправлять (каждая с новой строки)')
        if iss_name is False:
            self.log_browser.append('Заполни файлик sendernames.txt именами отправителя (каждое с новой строки)')
        if issub * ispost * ismails == 0:
            self.log_browser.append('И перезапусти меня')

    def main(self):
        self.log_browser.clear()
        fmail_delay_time = self.delayTime_1.text()
        fmail_len = self.hmMails.text()
        onepost_delay_time = self.delayTime_2.text()

        if onepost_delay_time == '':
            self.log_browser.append('Введи время ожидания между постами')
            return
        if fmail_delay_time == '':
            self.log_browser.append('Введи время ожидания между сообщениями')
            return
        if fmail_len == '':
            self.log_browser.append('Введи кол-во почт, на которые будет отправлены майл с одного адреса')
            return
        try:
            onepost_delay_time = float(onepost_delay_time)
        except ValueError:
            self.log_browser.append('Введи в one post цифры блен')
        try:
            fmail_delay_time = float(fmail_delay_time)
        except ValueError:
            self.log_browser.append('Введи в from email цифры блен')
            return
        try:
            fmail_len = int(fmail_len)
        except ValueError:
            self.log_browser.append('Введи how many mails цифры блин')
            return
        with open('sendernames.txt', 'r', encoding='utf-8') as snames:
            sendernames_list = map(lambda x: x.replace('\n', ''), snames.readlines())
        with open('smtpaccs.txt', 'r', encoding='utf-8') as smtps:
            smtp_list = ''
        with open('addr.txt', 'r', encoding='utf-8') as mails:
            mail_list = list(map(lambda x: x.replace('\n', ''), mails.readlines()))
        with open('subjects.txt', 'r', encoding='utf-8') as subjs:
            subj_list = list(map(lambda x: x.replace('\n', ''), subjs.readlines()))
        with open('fromaddr.txt', 'r', encoding='utf-8') as fmails:
            fmail_list = list(map(lambda x: x.replace('\n', ''), fmails.readlines()))
        with open('smtpaccs.txt', 'r', encoding='utf-8') as smtps:
            to_dict = lambda x: {'host': x[0], 'port': x[1], 'login': x[2], 'password': x[3]}
            smtp_list = iter([to_dict(smtp.split(':')) for smtp in
                         list(map(lambda x: x.replace('\n', ''), smtps.readlines()))])
        post_list = dir_to_list('posts')
        # print(post_list)

        for fmail in fmail_list:
            self.scount = 0
            send_len, list_len = fmail_len, len(mail_list)
            if send_len >= list_len:
                send_len = list_len
            self.log_browser.append(f'Начинаю отправку с {fmail}')
            sender_name = next(sendernames_list)
            c_smtp = next(smtp_list)
            QApplication.processEvents()
            for i in range(send_len):
                mail = mail_list[0]
                QApplication.processEvents()
                stat = msend(fmail, sender_name, mail, rand(subj_list), make_sy_text(rand(post_list)), c_smtp)
                if stat == 200:
                    self.log_browser.append(f'Отправленно на {mail} статус заебись')
                    self.scount += 1
                else:
                    self.log_browser.append(f'Отправленно на {mail} статус  - ошибка {stat}')
                mail_list.pop(0)
                with open('addr.txt', 'r', encoding='utf-8') as _mails:
                    newmail_list = _mails.readlines()
                newmail_list.pop(0)
                with open('addr.txt', 'w', encoding='utf-8') as __mails:
                    __mails.writelines(newmail_list)
                QApplication.processEvents()
                sleep(onepost_delay_time)
            else:
                self.log_browser.append(f'C {fmail} всего отправленно успешно {self.scount}')
            sleep(fmail_delay_time)


#
app = QApplication(sys.argv)
ex = Display()
ex.show()
sys.exit(app.exec_())
