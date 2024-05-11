print('vkusnaya_eda.ru')
milks = ['1', 'Молоко Луг 3.2% 1л.', 90, '2', 'Творог Луг 9% 180гр.', 120, '3', 'Ряженка Луг 4% 500мл.', 80, '4',
         'Кефир Луг 4% 1л.', 130]
fruits = ['5', 'Яблоки 1кг', 60, '6', 'Апельсины 1кг.', 100, '7', 'Бананы 1кг', 120, '8', 'Груши 1 кг', 110]
vegetables = ['9', 'Помидоры 1кг', 100, '10', 'Огурцы 1кг.', 78, '11', 'Морковь 1кг', 20, '12', 'Редис 1 кг', 150]
sweets = ['13', 'Батончик Sneakers', 40, '14', 'Конфеты белая лилия(20 шт.) 50', 100, '15', 'Батончик Twix', 120, '16',
          'Батончик Bounty', 110, '21', 'Подарочный набор', 5000]
drinks = ['17', 'Добрый Кола 1л', 90, '18', 'Добрый Фанта 1л', 85, '19', 'Минеральная вода 1л', 50, '20',
          'Молочный коктейль 550 мл', 45]
korzina = []
users = open('users.txt', 'r', encoding='utf-8').read().split(',')
del users[-1]
while True:
    print('1 - Войти', '2 - Зарегистрироваться')
    f_menu = input('Введите номер раздела: ')
    print()
    if f_menu == '1':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if login in users:
            if users[users.index(login) + 1] == password:
                print('Доступ разрешен')
                print()
                break
            else:
                print('Неверный пароль')
                print()
        else:
            print('Несуществующий пользователь')
            print()
    elif f_menu == '2':
        newlogin = input('Придумайте логин: ')
        newpassword = input('Придумайте пароль: ')
        snewpassword = input('Повторите пароль: ')
        print()
        if newlogin not in users:
            if newpassword == snewpassword:
                users.extend([newlogin, newpassword, 0, 1, 0])
                print('Вы успешно зарегестрировались!')
                file = open('users.txt', 'w', encoding='utf-8')
                for i in users:
                    file.write(str(i))
                    file.write(',')
                file.close()
                login = newlogin
                break
            else:
                print('Пароли не совпадают')
        else:
            print('Логин занят')

while True:
    print('1 - молочка, 2 - фрукты, 3 - овощи, 4 - сладости, 5 - напитки, 6 - личный кабинет, 7 - корзина')
    menu = input('Введите номер раздела: ')
    print()
    if menu == '1':
        print('Молочные продукты')
        for i in range(0, len(milks), 3):
            print(milks[i], '-', milks[i + 1], '; Цена:', milks[i + 2], 'руб.')
        print()
        milki = input('Выберите номер товара: ')
        if milki in milks:
            if milki not in korzina:
                korzina.append(milki)
                korzina.append(milks[milks.index(milki) + 1])
                korzina.append(milks[milks.index(milki) + 2])
                korzina.append(1)
            else:
                korzina[korzina.index(milki) + 2] = korzina[korzina.index(milki) + 2] + korzina[
                    korzina.index(milki) + 2] / korzina[korzina.index(milki) + 3]
                korzina[korzina.index(milki) + 3] += 1

    elif menu == '2':
        print('Фрукты')
        for i in range(0, len(fruits), 3):
            print(fruits[i], '-', fruits[i + 1], '; Цена:', fruits[i + 2], 'руб.')
        print()
        fruitsi = input('Выберите номер товара: ')
        if fruitsi in fruits:
            if fruitsi not in korzina:
                korzina.append(fruitsi)
                korzina.append(fruits[fruits.index(fruitsi) + 1])
                korzina.append(fruits[fruits.index(fruitsi) + 2])
                korzina.append(1)
            else:
                korzina[korzina.index(fruitsi) + 2] = korzina[korzina.index(fruitsi) + 2] + korzina[
                    korzina.index(fruitsi) + 2] / korzina[korzina.index(fruitsi) + 3]
                korzina[korzina.index(fruitsi) + 3] += 1
    elif menu == '3':
        print('Овощи')
        for i in range(0, len(vegetables), 3):
            print(vegetables[i], '-', vegetables[i + 1], '; Цена:', vegetables[i + 2], 'руб.')
        print()
        vegetablesi = input('Выберите номер товара: ')
        if vegetablesi in vegetables:
            if vegetablesi not in korzina:
                korzina.append(vegetablesi)
                korzina.append(vegetables[vegetables.index(vegetablesi) + 1])
                korzina.append(vegetables[vegetables.index(vegetablesi) + 2])
                korzina.append(1)
            else:
                korzina[korzina.index(vegetablesi) + 2] = korzina[korzina.index(vegetablesi) + 2] + korzina[
                    korzina.index(vegetablesi) + 2] / korzina[korzina.index(vegetablesi) + 3]
                korzina[korzina.index(vegetablesi) + 3] += 1
    elif menu == '4':
        print('Сладости')
        for i in range(0, len(sweets), 3):
            print(sweets[i], '-', sweets[i + 1], '; Цена:', sweets[i + 2], 'руб.')
        print()
        sweetsi = input('Выберите номер товара: ')
        if sweetsi in sweets:
            if sweetsi not in korzina:
                korzina.append(sweetsi)
                korzina.append(sweets[sweets.index(sweetsi) + 1])
                korzina.append(sweets[sweets.index(sweetsi) + 2])
                korzina.append(1)
            else:
                korzina[korzina.index(sweetsi) + 2] = korzina[korzina.index(sweetsi) + 2] + korzina[
                    korzina.index(sweetsi) + 2] / korzina[korzina.index(sweetsi) + 3]
                korzina[korzina.index(sweetsi) + 3] += 1
    elif menu == '5':
        print('Напитки')
        for i in range(0, len(drinks), 3):
            print(drinks[i], '-', drinks[i + 1], '; Цена:', drinks[i + 2], 'руб.')
        print()
        drinksi = input('Выберите номер товара: ')
        if drinksi in drinks:
            if drinksi not in korzina:
                korzina.append(drinksi)
                korzina.append(drinks[drinks.index(drinksi) + 1])
                korzina.append(drinks[drinks.index(drinksi) + 2])
                korzina.append(1)
            else:
                korzina[korzina.index(drinksi) + 2] = korzina[korzina.index(drinksi) + 2] + korzina[
                    korzina.index(drinksi) + 2] / korzina[korzina.index(drinksi) + 3]
                korzina[korzina.index(drinksi) + 3] += 1
    elif menu == '6':
        print('Профиль - ', login)
        print('Ваш баланс: ', users[users.index(login) + 2], 'руб.')
        print('Ваша скидка: ', users[users.index(login) + 3], '%')

        print('До следующей скидки осталось потратить: ', 5000 - int(users[users.index(login) + 4]), 'руб')


        print()
        print('1 - Пополнить баланс', '2 - Выйти в главное меню')
        s_menu = input('Выберите номер раздела: ')
        if s_menu == '1':
            balans = input('Введите сумму пополнения: ')
            if balans.isdigit():
                balans = int(balans)
                users[users.index(login) + 2] = int(users[users.index(login) + 2]) + balans
                print('Баланс успешно пополнен')
            else:
                print('Некоректный ввод')
    elif menu == '7':
        print('Корзина')
        for i in range(0, len(korzina), 4):
            print(korzina[i], '-', korzina[i + 1], '; Цена:', korzina[i + 2], 'руб.', 'кол-во: ', korzina[i + 3], 'шт.')
        print()
        print('Итог: ', sum(korzina[2::4]), 'руб.', 'Итог с учетом скидки: ',
              sum(korzina[2::4]) - sum(korzina[2::4]) // 100 * int(users[users.index(login) + 3]), 'руб.')
        print()
        print('1 - Выйти в главное меню, 2 - Измнеить корзину, 3 - Перейти к оплате')
        menkor = input('Введите номер раздела: ')
        if menkor == '2':
            delkor = input('Введите номер товара для удаления: ')
            if delkor in korzina:
                if korzina[korzina.index(delkor) + 3] == 1:
                    del korzina[korzina.index(delkor):korzina.index(
                        delkor) + 4]  # от индекса номера товара до кол-во включительно
                else:
                    korzina[korzina.index(delkor) + 2] -= korzina[korzina.index(delkor) + 2] / korzina[
                        korzina.index(delkor) + 3]
                    korzina[korzina.index(delkor) + 3] -= 1
        elif menkor == '3':
            if int(users[users.index(login) + 2]) >= sum(korzina[2::4]) - sum(korzina[2::4]) // 100 * int(
                    users[users.index(login) + 3]):
                users[users.index(login) + 2] = int(users[users.index(login) + 2]) - int(
                    sum(korzina[2::4]) - sum(korzina[2::4]) // 100 * int(users[users.index(login) + 3]))
                users[users.index(login) + 4] = int(users[users.index(login) + 4]) + int(
                    sum(korzina[2::4]) - sum(korzina[2::4]) // 100 * int(users[users.index(login) + 3]))
                korzina = []
                print('Оплата прошла успешно!')
                while int(users[users.index(login) + 4]) >= 5000 and int(users[users.index(login) + 3]) < 15:
                    users[users.index(login) + 4] = int(users[users.index(login) + 4]) - 5000
                    if int(users[users.index(login) + 3]) < 15:
                        users[users.index(login) + 3] = int(users[users.index(login) + 3]) + 1

    file = open('users.txt', 'w', encoding='utf-8')
    for i in users:
        file.write(str(i))
        file.write(',')
    file.close()