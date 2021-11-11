import random

# Метод для рандома типа элемента кладезя знаний.
def Rnd1To3():
    number = random.randint(1, 3)
    return number
# Создание строки рандомной длинны.
def StringRnd():
    simbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", ",", "!", "?", ":", ";"]
    ret = ""
    for number in range(random.randint(1,100)):
        ret += simbols[random.randint(0, len(simbols)-1)]
    return ret

