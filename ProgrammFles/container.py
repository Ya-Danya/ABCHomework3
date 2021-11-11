# Класс контейнера содержащий кладезь знаний.
class Container:
    # Конструктор.
    def __init__(self):
        self.store = []
    # Метод вывода в консоль.
    def Print(self):
        print("Container is store", len(self.store), "shapes:")
        for storageOfKnowledges in self.store:
            storageOfKnowledges.Print()
        
        pass
    # Метод вывода в файл.
    def Write(self, ostream):
        ostream.write("Storage of knowledges contains {} elements:\n".format(len(self.store)))
        for storageOfKnowledges in self.store:
            storageOfKnowledges.Write(ostream)
            ostream.write("\n")
        pass
    # Метод удаления элементов, процент знаков препинания в тексте которых ниже среднего.
    def DeleteElements(self):
        summ = 0.0
        for storageOfKnowledges in self.store:
            summ += storageOfKnowledges.PercentageOfPunctuation()
        middlePoint = summ / len(self.store)
        i = 0;
        for storageOfKnowledges in self.store:
            if (storageOfKnowledges.PercentageOfPunctuation() < middlePoint):
                self.store.pop(i)
                i = i + 1
        pass
