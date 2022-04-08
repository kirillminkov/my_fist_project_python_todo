import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы
random - добавлять случайную задачу на дату Сегодня"""


random_tasks = ["Сделать зарядку", "Написать Гвидо письмо",
                "Покормить кошку", "Помыть машину"]

tasks = {}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print(f"Задача {task} добавлена на дату {date}")


while True:
    command = input("Введите команду: ").lower()
    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("Введите дату выполнения задачи: ").lower()
        task = input("Введите задачу: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(random_tasks)
        add_todo("сегодня", task)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ").lower()
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
