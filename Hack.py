
import uuid
import telebot
import random
import PIL
from PIL import Image
from telebot import types
import requests
import pyqrcode

files = {}
token = "615720180:AAGx9q-gtRHXizHEIMyV0AGBC9VVGzvH7Qg"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
bot = telebot.TeleBot(token=token)
current_tasks = {}
tasks = [
    ('Пользователь делает вклад в размере 100000 рублей сроком на 5 лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).Написать, сколько денег будет на счету пользователя.', "161051"),
    ('Вводится два целых числа: 1012 и 600. Найдите их наибольший общий делитель.', '161051'),
    ('В самолете 40 мест. Три четверти от всех пассажиров самолета v имеют билеты 2 классастоимостью 5000 рублей каждый. Остальные пассажира имеют билеты 1 класса, которые стоят в 2 раза дороже билетов 2 класса. Какую сумму денег получит авиакомпания от продажи билетов на этот рейс.', '250000'),
    ('Дан прямоугольник со сторонами 5 и 8. Нужно найи произведение его периметра и площади', "1040"),
    ('Условие: дан код на python:\n n = int (input("382"))\n a = n // 100\n b = (n % 100) // 10\n c = n % 10\n print( a + b + c )\n Задача: Что выведет этот код?',"13"),
    ('Напишите фамилию создателя python',"Россум"),
    ('Условия:Даны числа: 10,9,6,60,90,70,66. Вопрос:какое число будет следующим?', "96"),
    ('Человек, который решает проблему, о которой вы и незнали, таким способом, который вы не понимаете.', "Программист"),
    ('Условия:В книге N страниц, пронумерованных как обычно от 1 до N. Если сложить количество цифр,содержащихся в каждом номере страниц, будет 1095. Сколько страниц в книге?', "401"),
    ('Пифагорейский тройня-это набор из трех натуральных чисел, a < b < c для чего,\n a2 + b2 = c2 \nНапример, 32 + 42 = 9 + 16 = 25 = 52.\n Существует ровно одна тройка Пифагора, для которой a + b + c = 1000.\nНайти продукт abc.', "31875000"),
    ('1 + 4 = 5\n2 + 5 = 12\n3 + 6 = 21\n8 + 11 =?', "40")
]
history = []
points = ["1", "2"]

@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Добрый день! Чтобы начать игру, Вам требуется путешествовать по территории лагеря GoTo и искать QR коды, по мере нахождения - решать задачи и получать за них GoTo coins и стикеры ❤️. Пришлите первый QR code, чтобы начать:") 


@bot.message_handler(content_types=['photo'])
def QR(message):
    global current_tasks
    print('got photo')
    user = message.chat.id
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    p = 'https://api.telegram.org/file/bot{0}/'.format(token) + path.file_path
    url = 'http://api.qrserver.com/v1/read-qr-code/'
    res = requests.post(url, {'fileurl': p})
    try:
        x = res.json()[0]['symbol'][0]['data']
        if x not in points:
            bot.send_message(user, "Не удается разобрать QR код.")
            return

    except:
        bot.send_message(user, "Не удается разобрать QR код.")
        return

    history = [(user , x)]
    current_tasks[user]=random.choice(tasks)
    bot.send_message(user, current_tasks[user])
       
@bot.message_handler(content_types=['text'])
def answer(message):
    user = message.chat.id
    if message.text == current_tasks[message.chat.id][1]:
        bot.send_message(user, 'Ваш ответ верный. Вам начислено 0.25 коинов')
    else:
        bot.send_message(user, 'Вы ошиблись. Попробуйте через 10 минут.')
    
bot.polling(none_stop = True)
