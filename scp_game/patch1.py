import time
from os import system

check = 1
def scp_914(check = 1):
    while 1:
        global key_card_level
        print('1:нежно')
        print('2:1:1')
        print('3:жёстко')
        print('4.Выйти')
        scp914 = int(input(":"))
        if scp914 == 4:
            system('cls')
            break
        if scp914 == 1:
            if key_card_level == 0:
                system('cls')
                print('у вас нет карты')
                print(key_card_level)
            if key_card_level == 1:
                system('cls')
                key_card_level = 2
                print(key_card_level)
                print(key_card_level)

key_card_level = 0

while 1:
    print('         SCP')
    print('Secure. Contain. Protect.')
    print('  Елена Блиновская в SCP ')
    print('1.Играть')
    print('2.Выйти')
    print('3.Как играть')
    play = int(input(':'))
    if play == 2:
        quit()
    elif play == 106:
        system('cls')
        scp_914(key_card_level)
        print(key_card_level)
    elif play ==  105:
        system('cls')
        debug_keys = int(input('key_card_level 1-6=:'))
        key_card_level = debug_keys
    elif play == 3:
        system('cls')
        print('игра хадкорная(при смерти игра закрывается) наслаждайтесь)')
    elif play == 1:
        system('cls')
        while 1:
            print('Пролог: Блиновскую Арестовали и осудили за мошеничество и засадили в тюрьму."Научный фонд"  пригласил на работу вместо тюрьмы. Блиновская согласилась ,и на следущий день она проснулась в фонде SCP, сотрудником D-Class(а). ')
            time.sleep(15)
            continue1 = int(input('Прочитали? Нажмите 1:'))
            system('cls')
            if continue1 == 1:
                while 1:
                    system('cls')
                    print('*вы проснулись в камере*')
                    time.sleep(3)
                    system('cls')
                    print('*бумага на столе лежит вы решили её прочитать*')
                    time.sleep(2)
                    system('cls')
                    print('__________________________')
                    print('|        SCP фонд         |')
                    print('|Secure. Contain. Protect.|')
                    print('|Доброе утро! Вы сотрудн- |')
                    print('|-ик D-Class(а).ВАШ НОМЕР:|')
                    print('|         D-56789         |')
                    print('|Вы будете отправляться на|')
                    print('|смерть. За попытку сбеж- |')
                    print('|ать вы будете ликвидеров-|')
                    print('|аны. Не желаем удачи!!!1!|')
                    print('---------------------------')
                    time.sleep(15)
                    system('cls')
                    print('*вашу камеру открыли*')
                    time.sleep(2)
                    system('cls')
                    print('Охранник - Эй! Дешка для тебя работа есть! Шуруй быстро!')
                    time.sleep(5)
                    system('cls')
                    while 1:
                        print('*Пойти на работу 1 или Нахамить2*')
                        vham = int(input('p :'))
                        if vham == 2:
                            system('cls')
                            print('Блиновская -Я сейчас в рожу плюну!')
                            time.sleep(2)
                            system('cls')
                            print('*Охранник достал автомат*')
                            time.sleep(2)
                            system('cls')
                            print('Охранник-Ну что прощайся с жизнью,бещасть')
                            time.sleep(5)
                            system('cls')
                            print('*Охранник вас расстрелял, вы умерли от потери крови*')
                            print('*Ачивка получена!: "Неудачная борзая фея"*')
                            print('Через 5 секунд выход из игры')
                            time.sleep(5)
                            quit()
                        if vham == 1:
                            system('cls')
                            print('Охранник-Отлично')
                            time.sleep(2)
                            system('cls')
                            print('Охранник-Идём D-56789')
                            time.sleep(2)
                            system('cls')
                            print('*Вы шли*')
                            time.sleep(2)
                            system('cls')
                            print('Блиновская-Дошли?')
                            time.sleep(2)
                            system('cls')
                            print('Охранник-Нет ещё')
                            time.sleep(2)
                            system('cls')
                            print('*Вы дошли*')
                            time.sleep(2)
                            system('cls')
                            print('Охранник-ну вот, дошли')
                            time.sleep(2)
                            system('cls')
                            print('*охранник протягивает вам бумагу*')
                            time.sleep(2)
                            system('cls')
                            print('*вкратце было написано про аномалию SCP-173 класса евклид(мало изученный)*')
                            time.sleep(5)
                            system('cls')
                            print('Блиновская-может не надо?')
                            time.sleep(2)
                            system('cls')
                            print('Охранник-надо Лена надо')
                            time.sleep(2)
                            system('cls')
                            print('*Вас пустили в камеру*')
                            time.sleep(2)
                            system('cls')
                            print('*С вами были ещё 2 человека*')
                            time.sleep(2)
                            system('cls')
                            print('Интерком-Персоналу класса-d, войдите в контейнер содержания SCP-173 для тестирования')
                            time.sleep(2)
                            system('cls')
                            print('*Вы втроём вошли*')
                            time.sleep(2)
                            system('cls')
                            print('*Двери закрылись*')
                            time.sleep(2)
                            system('cls')
                            print('*через 1 минуту*')
                            time.sleep(2)
                            system('cls')
                            print('*двери открылись*')
                            time.sleep(2)
                            system('cls')
                            print('Интерком-Эээ у нас проблема с системой управления двери и эмм')
                            time.sleep(2)
                            system('cls')
                            print('*Вы два раза моргнули*')
                            time.sleep(2)
                            system('cls')
                            print('*SCP-173 свернул голову двоим*')
                            time.sleep(2)
                            system('cls')
                            print('*SCP-173 телепротировался к охраннику.*')
                            time.sleep(2)
                            system('cls')
                            print('*SCP-173 свернул шею охраннику*')
                            time.sleep(2)
                            system('cls')
                            print('*Вы бежали куда дальше от проишествия*')
                            time.sleep(2)
                            system('cls')
                            print('*Зайти в комнату по пути?*')
                            while 1:
                                system('cls')
                                vcom = int(input('p-1  да - 1, пройти мимо - 2:'))
                                if vcom == 1:
                                    system('cls')
                                    print('*Вы вошли в комнату*')
                                    time.sleep(2)
                                    system('cls')
                                    print('*Вы взяли ключ-карту 2 уровня пропуска*')
                                    key_card_level = 2
                                elif vcom == 2:
                                    system('cls')
                                    print('*вы прошли мимо*')
                                print(key_card_level)
                                print('*вы шли*')
                                time.sleep(2)
                                system('cls')
                                print('*вдруг вам показались электрические ворота,а по середине тело учёного*')
                                time.sleep(2)
                                system('cls')
                                print('*вдруг ворота снова ударили током*')
                                time.sleep(2)
                                system('cls')
                                print('Пробегать или подождать?')
                                vvot = int(input('p-2 да-1,подождать-2:'))
                                if vvot == 1:
                                            system('cls')
                                            print('*вы пробежали и вас ударило током*')
                                            time.sleep(2)
                                            system('cls')
                                            print('*Ачивка получена!: "Не оправданый риск"*')
                                            print('Через 5 секунд вы вернётесь выход из игры')
                                            time.sleep(5)
                                            system('cls')
                                            quit()
                                if vvot == 2:
                                        print('*вы подождали и пробежали*')
                                        time.sleep(2)
                                        system('cls')
                                        print('*Ачивка получена!: "Ждун"*')
                                        system('cls')
                                        print('Блиновская пойду я дальше')
                                        time.sleep(2)
                                        print('*Вы выжили*')
                                        print('*вы проходите  мимо и видете 2 двери одна с надписью SCP-914 и ещё одна дверь куда пойти?*')
                                        while 1:
                                            v914 = int(input('1 - да 2 - пройти мимо и пойти в другую дверь'))
                                            if v914 == 1:
                                                if key_card_level < 2:
                                                    print('*У вас нет карты или малый уровень доступа*')
                                                elif key_card_level >= 2:
                                                        scp_914(check = 1)
                                                        print("*после SCP-914 вы зашли в другую дверь*")
                                                        time.sleep(2)
                                                        system('cls')
                                            elif v914 == 2:
                                                print('*вы прошли мимо и зашли в дверь*')
                                                time.sleep(2)
                                                system('cls')
                                                print('*вы зашли*')
                                                print('Если вы читаете это значит что вы достигли конца кода проходит разработка вы можете поделиться своими ощущениями от игры разработчику')
                                                time.sleep(5)
                                                quit()