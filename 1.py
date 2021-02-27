#1
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

# print(dict(enumerate(["92","91","49", "87", 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33])))

d = {}
for i in range(0, len(lst)):
    d[i]=lst[i]
print(d) 

#2
import random
guessesTaken = 0
print("Добро пожаловать на игру: Угадай число! Как Ваше имя?")
myName = input()
number = random.randint(1,20)
print("Ну тогда приступим? "+myName+", я загадал число от одного до 20")
while guessesTaken < 6:
    print("Как ты думаешь, какое число загадал?")
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken+1
    if guess < number:
        print("слишком мало") 

    if guess > number:
        print("слишком много")
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Класс! Вы угадали")

if guess != number:
    number = str(number)
    print("Все, вы не выиграли. Игра завершилась")


#3
s = "Adverts"
print(s[2:5])

#4
string="".join("".join(pair) for pair in (zip("Aidana", "Adilet")))
print(string)
