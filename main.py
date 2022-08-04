#создание пустого слолваря
username = {}
#создание цикла while со значением True
while True:
    # ввод данных от пользователя
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    # добавление введённых данных в словарь
    isName = username.get(name, None)
    if isName is None:
        username[name] = age
    # запрос команды от пользователя
    command = input("Введите команду: ")
    # проверка совпадения введённой команды с условием
    if command == "show":
        for name in [username]:
            # вывод словаря с добавленного в него данными
            print(username)