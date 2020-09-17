def make_a_bet(balance: int) -> int:
    while True:
        try:
            stavka = int(input('Сколько ставите?\n'))
        except (ValueError, TypeError):
            print('Следите за руками')
            return 0
        if 0 < stavka > balance:
            print('Проверьте корректность вашей ставки')
        else:
            return stavka
          
