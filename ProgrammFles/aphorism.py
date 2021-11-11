from storageOfKnowledges import *
from rand import *

# Класс афоризмов.
class Aphorism(StorageOfKnowledges):
    # Конструктор.
    def __init__(self):
        self.author = ""
        self.text = ""
    # Чтение строк и передача их данных в афоризм.
    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 2:
            return 0
        self.text = strArray[i]
        self.author = strArray[i+1]
        return i + 2
    # Метод рандомного ввода.
    def RandomInput(self):
        self.text = StringRnd()
        self.author = StringRnd()
        pass
    # Метод для вывода в консоль.
    def Print(self):
        print("Author: ", self.author, "\nAporism: ", self.text, "\nPercentage of punctuation marks:", self.PercentageOfPunctuation(), "\n")
        pass
    # Метод для вывода в файл.
    def Write(self, ostream):
        ostream.write("Author: {}\nAporism: {}\nPercentage of punctuation marks: {}\n".format(self.author, self.text, self.PercentageOfPunctuation()))
        pass
    # Нахождения отношения знаков препинания к кол-ву символов строки.
    def PercentageOfPunctuation(self):
        percentage = (self.text.count(",")+self.text.count(".")+self.text.count(":")+self.text.count("!")+self.text.count("?")+self.text.count("\"")+self.text.count(";"))/len(self.text)
        return percentage
    