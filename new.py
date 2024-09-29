#family community login

username = str(input("ведите свое имя чтобы войти в семейный счет! : "))


def family_login(name):
    if username == "лена":
        print(f"добро пожаловать {username}")
    elif username == "марита":
        print(f"добро пожаловать {username}")
    else:
        print("you dont belong to the family community!")

family_login(name=username)