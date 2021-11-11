from storageOfKnowledges import *
from rand import *

# Класс загадок.
class Riddle(StorageOfKnowledges):
    # Конструктор.
    def __init__(self):
        self.text = ""
        self.answer = ""
    # Чтение строк и передача их данных в афоризм.
    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 2:
            return 0
        self.text = strArray[i]
        self.answer = strArray[i+1]
        return i + 2
    # Метод рандомного ввода.
    def RandomInput(self):
        self.text = StringRnd()
        self.answer = StringRnd()
        pass
    # Метод для вывода в консоль.
    def Print(self):
        print("Riddle: ", self.text, "\nAnswer:", self.answer, "\nPercentage of punctuation marks:", self.PercentageOfPunctuation(), "\n")
        pass
    # Метод для вывода в файл.
    def Write(self, ostream):
        ostream.write("Riddle: {}\nWith answer: {}\nPercentage of punctuation marks: {}\n".format(self.text, self.answer, self.PercentageOfPunctuation()))
        pass
    # Нахождения отношения знаков препинания к кол-ву символов строки.
    def PercentageOfPunctuation(self):
        percentage = (self.text.count(",")+self.text.count(".")+self.text.count(":")+self.text.count("!")+self.text.count("?")+self.text.count("\"")+self.text.count(";"))/len(self.text)
        return percentage
    