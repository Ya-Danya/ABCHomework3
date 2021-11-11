from extender import *

# Ввод строк из файла и определение типа элементов кладезя знаний.
def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0   # Индекс, задающий текущую строку в массиве
    Count = 0
    while i < arrayLen:
        key = strArray[i]
        if key == "1": # Признак афоризма
            i += 1
            storageOfKnowledges = Aphorism()
            i = storageOfKnowledges.ReadStrArray(strArray, i)
        elif key == "2": # признак поговорки
            i += 1
            storageOfKnowledges = Proverb()
            i = storageOfKnowledges.ReadStrArray(strArray, i)
        elif key == "3": # признак загадки
            i += 1
            storageOfKnowledges = Riddle()
            i = storageOfKnowledges.ReadStrArray(strArray, i)
        else:
            return Count
        if i == 0:
            return Count
        Count += 1
        container.store.append(storageOfKnowledges)
    return Count
