
# Импорт библиотек
import random
import time

# Счет игроков
score_player = 0
score_bot = 0

# Начальное сообщение
all_carts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Сыграем в 21? \n Если хотите играть нажмите Enter")
input()

# Цикл
while True:
    if score_player == 21:
        print("Больше карт брать не нужно, вы набрали 21 очко")
        print("Вы автоматически победили соперника, так как у вас 21.")
        input("Нажмите Enter, чтобы закрыть окно.");
        break
    if score_player > 21:
        print("Вы проиграли, так как набрали больше 21 очка")
        print("Попытайте свою попытку в другой раз.")
        input("Нажмите Enter, чтобы закрыть окно.");
        break
    yes_or_no = input(
        "Будете ли вы брать карту? \n Введите yes, если хотите брать карту или введите no, если не берете карту.\n")

    if yes_or_no == 'yes':

        score_carts = random.choice(all_carts)
        print("Вы взяли карту, вам выпало:", score_carts)
        score_player += score_carts
        print("Сейчас у вас ", score_player)
    if yes_or_no == 'no':
        print("У вас ", score_player, "очков.")
        print("Ход соперника")
        time.sleep(3)

        while True:
            if score_bot < 20:
                print("Соперник берет карту")
                score_carts = random.choice(all_carts)
                print("Сопернику выпало", score_carts, "очков.")
                score_bot += score_carts
                print("У соперника ", score_bot, "очков.")
                time.sleep(3)

            if score_bot > 21:
                print("Ваш соперник проиграл.\n Соперник набрал", score_bot, "очков, вы набрали ", score_player)
                input("Нажмите Enter, чтобы закрыть");
                exit(0)
            if score_bot > score_player:
                print("Соперник победил.\n Соперник набрал", score_bot, "очков, а вы набрали ", score_player,
                      "\n Не растраивайтесь. Попробуйте ещё раз.")
                input("Нажмите Enter, чтобы закрыть");
                exit(0)
            if score_bot == score_player:
                print("Вы набрали равное количество очков и у вас ничья")
                input("Нажмите Enter, чтобы закрыть");
                exit(0)