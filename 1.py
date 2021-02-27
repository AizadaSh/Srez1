# #1
# import random
# guessesTaken = 0
# print("Добро пожаловать на игру: Угадай число! Как Ваше имя?")
# myName = input()
# number = random.randint(1,20)
# print("Ну тогда приступим? "+myName+", я загадал число от одного до 20")
# while guessesTaken < 6:
#     print("Как ты думаешь, какое число загадал?")
#     guess = input()
#     guess = int(guess)
#     guessesTaken = guessesTaken+1
#     if guess < number:
#         print("слишком мало") 

#     if guess > number:
#         print("слишком много")
    
#     if guess == number:
#         break

# if guess == number:
#     guessesTaken = str(guessesTaken)
#     print("Класс! Вы угадали")

# if guess != number:
#     number = str(number)
#     print("Все, вы не выиграли. Игра завершилась")


#2


#3
s = "Adverts"
print(s[2:5])

#4
string="".join("".join(pair) for pair in (zip("Aidana", "Adilet")))
print(string)
