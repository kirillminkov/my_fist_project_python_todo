import telebot
import random

token = "5281740167:AAEUH5lMd6fbuvAby5e3fefXZQA_I2Wxfik"

bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список /add + дата + задача.
/show - напечатать все добавленные задачи /show + дата.
/exit - выход из программы
/random - добавлять случайную задачу на дату Сегодня"""

random_tasks = ["Сделать зарядку", "Написать Гвидо письмо",
                "Покормить кошку", "Помыть машину"]

tasks = {}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add", "random"])
def add(message):
    command = message.text.split(maxsplit=2)
    if command[0] == "/add":
        date = command[1].lower()
        task = command[2]
    elif command[0] == "/random":
        date = "сегодня"
        task = random.choice(random_tasks)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "- " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
