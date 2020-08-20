import requests
import random
import urllib.parse
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from window import Ui_App
import sys

uencode = urllib.parse.quote
issub, ispost, ismiles = True, True, True

if 'subjects' not in os.listdir():
    os.mkdir('subjects')
if 'posts' not in os.listdir():
    os.mkdir('posts')
if 'addr.txt' not in os.listdir():
    file = open('addr.txt', 'w').close()

if not os.listdir(f'{os.getcwd()}\\subjects'):
    issub = False
if not os.listdir(f'{os.getcwd()}\\posts'):
    ispost = False
with open('addr.txt') as file:
    if not file.readlines():
        ismiles = False


def resource_path(relative):
    # функция позволяющая импортироать файлы при компиляции
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


def msend(sfrom, sto, subj, body):
    rjson = {'from': sfrom, 'to': sto, 'subject': subj, 'body': body}
    url = urllib.parse.urlencode(rjson)
    r = requests.post('http://mailspoofer.herokuapp.com/',
                      url)
    return rjson, r.status_code


def dir_to_list(dir):
    dlist = []
    os.chdir(f'{os.getcwd()}\\{dir}')
    for file in os.listdir():
        with open(file, 'r', encoding='utf-8') as tfile:
            dlist.append(''.join(tfile.readlines()))
    os.chdir(os.getcwd().replace(f'\\{dir}', ''))
    return dlist


class Display(QMainWindow, Ui_App):
    # создание окна отображения данных
    def __init__(self):
        self.scount = 0
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))

        self.startButton.clicked.connect(self.main)
        if issub is False:
            self.log_browser.append('Заполни директорию subjects темами (каждая .txt)')
        if ispost is False:
            self.log_browser.append('Заполни директорию posts письмами (каждое .txt)')
        if ismiles is False:
            self.log_browser.append('Заполни фалик addr.txt почтами (каждая с новой строки)')
        if issub * ispost * ismiles == 0:
            self.log_browser.append('И перезапусти меня')

    def main(self):
        self.scount = 0
        self.log_browser.clear()
        if self.from_text.text() != '':
            with open('addr.txt', 'r') as mail_list:
                mails = list(map(lambda x: x.replace('\n', ''), mail_list.readlines()))
            subj_list = dir_to_list('subjects')
            post_list = dir_to_list('posts')
            fmail = self.from_text.text()
            QApplication.processEvents()
            for x, mail in enumerate(mails):
                QApplication.processEvents()
                json, stat = msend(fmail, mail, random.choice(subj_list), random.choice(post_list))
                print(f'Отправленно на {mail}')
                if stat == 200:
                    self.log_browser.append(f'Отправленно на {mail} статус Заебись')
                    self.scount += 1
                else:
                    self.log_browser.append(f'Отправленно на {mail} статус Хуета - ошибка {stat}')
                QApplication.processEvents()
            else:
                self.log_browser.append(f'Всего отправленно успешно {self.scount}')

        else:
            self.log_browser.setText('Майл введи дурилка')


app = QApplication(sys.argv)
ex = Display()
ex.show()
sys.exit(app.exec_())
