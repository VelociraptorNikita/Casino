import random
import time

def make_a_bet(balance: int) -> int:
    while True:
        try:
            stavka = int(input('Сколько ставите?\n'))
        except (ValueError, TypeError):
            print('Следите за руками')
            return 0
        if stavka > balance:
            print('У вас нет столько')
        else:
            return stavka

def Avtomat(balance: int) -> int:
    print('При совпадении трёх чисел вы получаете удвоенную ставку')
    print('Поиграем в автоматы')
    stavka = make_a_bet(balance)
    ch1 = random.randint(0, 6)
    ch2 = random.randint(0, 6)
    ch3 = random.randint(0, 6)
    print(f'Первое число: {ch1}')
    time.sleep(2)
    print(f'Второе число: {ch2}')
    time.sleep(2)
    print(f'Третье число: {ch3}')
    time.sleep(1)
    if ch1 == ch2 == ch3:
        k = 1.4 + ch1/10
        print('Поздравляю, вы победили')
        return stavka * k
    else:
        print('В этот раз не повезло')
        return -stavka
          
        
def Ochko(balance: int) -> int:
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(koloda)
    print('Поиграем в очко')
    stavka = make_a_bet(balance)
    countUser = 0
    countKrup = 0
    while True:
        user_input = input('Будете брать карту? д/н\n').lower()
        if user_input in ('д', 'да') and len(koloda) > 0:
            current = koloda.pop()
            print(f'Вам попалась карта дотоинством {current}')
            countUser += current
            print(f'У вас {countUser} очков')
        elif user_input in ('н', 'не', 'нет'):
            print(f'У вас {countUser} очков и вы закончили игру')
            break
        else:
            print('Я не понял вас')
    while countKrup < 17:
        countKrup += koloda.pop()
    print(f'Счёт крупье: {countKrup}')
    if countUser > 21:
        print('Вы проиграли, у вас перебор')
        return -stavka
    elif countKrup > 21:
        print('Вы выиграли, у крупье перебор')
        return stavka
    elif countUser > countKrup:
        print('Вы выиграли')
        return stavka
    else:
        print('Вы проиграли')
        return -stavka
    


def main(balance):
    while True:
        try:
            print(f'Ваш текущий баланс: {balance}')
            if balance <= 0:
                print('Вас выводит охрана')
                input()
                break
            elif balance >= 100000:
                print('Охрана заводит вас в отдалённую комнату, запирает дверь, избивает вас и отнимает все деньги. После чего выкидывает на улицу')
                input()
                break
            print('Если хотите сыграть в очко введите: "Очко"')
            print('Если хотите сыграть в автоматы введите: "Автоматы"')
            print('Если хотите выйти введите: "Выход"')
            user_input = input('Выбор игры: ').lower()
            if user_input == 'очко':
                balance += Ochko(balance)
            elif user_input == 'автоматы':
                balance += Avtomat(balance)
            elif user_input == 'выход':
                print('Всего хорошего')
                break
            else:
                print('Таких услуг мы пока не предоставляем')
        except TypeError:
            print('С вами всё в порядке? Вы не перебрали с алкоголем?')

if __name__ == "__main__":
    main(5000)
