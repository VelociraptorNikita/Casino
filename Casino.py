import random
from games import Bet

def load(dir) -> list:
    from os import listdir as ls
    py_files = [m[:-3] for m in ls(dir) if m[-3:]=='.py' and m[:-3] != 'Bet']
    return [getattr(__import__(dir+'.'+m), m) for m in py_files]

object_to_function = {'balance': 0, 'bet': 0}
list_games = load('games')
dict_games = {}
for module in list_games:
  dict_games[module] = module.info()


def main(input_data: dict):
    while input_data['balance'] > 0:
        print(f'Ваш текущий баланс: {input_data["balance"]}')
        if input_data['balance'] >= 100000:
            print('Охрана заводит вас в отдалённую комнату, запирает дверь, избивает вас и отнимает все деньги. После чего выкидывает на улицу')
            input()
            break
        print('Список игр: ')
        for game in dict_games.values():
            print(game)
        print('Если хотите выйти введите: "Выход"')
        try:
            user_input = input('Выбор игры: ').title().strip()
        except TypeError:
            print('С вами всё в порядке? Вы не перебрали с алкоголем?')
        for module, info in dict_games.items():
            if info == user_input:
                input_data['bet'] = Bet.make_a_bet(input_data['balance'])
                input_data['balance'] += module.game(input_data)
                break
        if user_input == 'выход':
            print('Всего хорошего')
            break
    else:
        print('Вас выводит охрана')
        input()

if __name__ == "__main__":
    object_to_function['balance'] = 5000
    main(object_to_function)
