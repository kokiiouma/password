import random


def password_generator(length):
    symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_[]{};/?.,'
    password = ''

    for i in range(5):
        password = ''
        for j in range(length):
            password += random.choice(symbols)
        print(f'{i + 1}. cгенерированный пароль: {password}')


state = True

while state:
    print('*********************************************')
    length = int(input("Введите длину пароля: "))
    password_generator(length)

    answer = int(input("Подолжить? (1 - да, 0 - нет): "))

    if answer != 1:
        state = False
        print('************** КОНЕЦ РАБОТЫ *******************')
