import requests
import random
import urllib.parse
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from window import Ui_App
import sys

uencode = urllib.parse.quote


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


def main():
    with open('addr.txt', 'r') as mail_list:
        mails = list(map(lambda x: x.replace('\n', ''), mail_list.readlines()))
    subj_list = dir_to_list('subjects')
    post_list = dir_to_list('posts')
    fmail = input('введите мыло с которого отправлять\n')
    for mail in mails:
        msend(fmail, mail, random.choice(subj_list), random.choice(post_list))


class Display(QMainWindow, Ui_App):
    # создание окна отображения данных
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))
        self.startButton.clicked.connect(self.main)

    def main(self):
        if self.from_text.text() != '':
            with open('addr.txt', 'r') as mail_list:
                mails = list(map(lambda x: x.replace('\n', ''), mail_list.readlines()))
            subj_list = dir_to_list('subjects')
            post_list = dir_to_list('posts')
            fmail = self.from_text.text()
            QApplication.processEvents()
            for x, mail in enumerate(mails):
                QApplication.processEvents()
                print(f'Отправленно на {mail}')
                self.log_browser.append(f'Отправленно на {mail}')
                msend(fmail, mail, random.choice(subj_list), random.choice(post_list))
                QApplication.processEvents()
        else:
            self.log_browser.setText('Майл введи дурилка')


app = QApplication(sys.argv)
ex = Display()
ex.show()
sys.exit(app.exec_())
