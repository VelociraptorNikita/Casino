import random
import One_armed_bandit
import Bet
import Blackjack

def main(balance):
    while True:
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
        try:    
            user_input = input('Выбор игры: ').lower()
        except TypeError:
            print('С вами всё в порядке? Вы не перебрали с алкоголем?')
        if user_input == 'очко':
            balance += Blackjack.ochko(balance)
        elif user_input == 'автоматы':
            balance += One_armed_bandit.avtomat(balance)
        elif user_input == 'выход':
            print('Всего хорошего')
            break
        else:
            print('Таких услуг мы пока не предоставляем')


if __name__ == "__main__":
    main(5000)
