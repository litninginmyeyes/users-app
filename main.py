
users = []

while True:
    comm = input()
    if comm == "quit":
        break
    elif comm == "add":
        user = {}
        user['name'] = input("Введите имя пользователя:\n")
        age = ""
        while True:
            age = input("Введите возраст пользователя:\n")
            if age.isdigit():
                break
            print("Неверный возраст, попробуйте еще раз:\n")
        user['age'] = int(age)
        user['email'] = input("Введите почту пользователя:\n")
        users.append(user)
        print("Пользователь добавлен\n")
    elif comm == "list":
        for user in users:
            print(f"{user['name']}, {user['age']} лет, {user['email']}\n")
    elif comm == "find":
        find_anchor = True
        find = input("Введите имя:\n")
        for user in users:
            if user['name'] == find:
                print(f"{user['name']}, {user['age']} лет, {user['email']}\n")
                find_anchor = False

        if find_anchor:
            print("Пользователь не найден")
            
    else:
        print("Неизвестная команда")