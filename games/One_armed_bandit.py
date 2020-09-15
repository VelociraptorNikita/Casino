import Bet
import random
import time

def avtomat(balance: int) -> int:
    print('При совпадении трёх чисел вы получаете удвоенную ставку')
    print('Поиграем в автоматы')
    stavka = make_a_bet(balance)
    if stavka == 0:
        return 0
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
