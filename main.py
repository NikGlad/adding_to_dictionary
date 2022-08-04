username = {}

while True:
    name = input("Введите имя: ")
    age = input("Введите возраст: ")

    isName = username.get(name, None)
    if isName is None:
        username[name] = age

    command = input("Введите команду: ")
    if command == "show":
            for name in [username]:
                print(username)