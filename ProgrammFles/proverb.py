from storageOfKnowledges import *
from rand import *

# Класс поговорок.
class Proverb(StorageOfKnowledges):
    # Конструктор.
    def __init__(self):
        self.text = ""
        self.country = ""
    # Чтение строк и передача их данных в афоризм.
    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.text = strArray[i]
        self.country = strArray[i+1]
        return i + 2
    # Метод рандомного ввода.
    def RandomInput(self):
        self.text = StringRnd()
        self.country = StringRnd()
        pass
    # Метод для вывода в консоль.
    def Print(self):
        print("Proverb: ", self.text, "\nFrom: ", self.country, "\nPercentage of punctuation marks:", self.PercentageOfPunctuation(), "\n")
        pass
    # Метод для вывода в файл.
    def Write(self, ostream):
        ostream.write("Proverb: {}\nFrom: {}\nPercentage of punctuation marks: {}\n".format(self.text, self.country, self.PercentageOfPunctuation()))
        pass
    # Нахождения отношения знаков препинания к кол-ву символов строки.
    def PercentageOfPunctuation(self):
        percentage = (self.text.count(",")+self.text.count(".")+self.text.count(":")+self.text.count("!")+self.text.count("?")+self.text.count("\"")+self.text.count(";"))/len(self.text)
        return percentage
