# 1 Напишите функцию, которая будет принимать номер кредитной карты и показывать только
# последние 4 цифры. Остальные цифры должны заменяться звездочками.

card = (input("Input number of card:\n"))


def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]


if __name__ == '__main__':
    print(card_hide(card))
