import random
import Bet

def ochko(balance: int) -> int:
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(koloda)
    print('Поиграем в очко')
    stavka = make_a_bet(balance)
    if stavka == 0:
        return 0
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
    
