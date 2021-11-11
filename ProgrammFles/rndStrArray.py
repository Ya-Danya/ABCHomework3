from extender import *
from rand import *

# Рандом типа элемента кладезя знаний.
def RndStrArray(container, length):
    for i in range(length):
        key = Rnd1To3()
        if key == 1: # Признак афоризма.
            storageOfKnowledges = Aphorism()
            storageOfKnowledges.RandomInput()
        elif key == 2: # признак поговорки.
            storageOfKnowledges = Proverb()
            storageOfKnowledges.RandomInput()
        else: # Оставшиеся элементы определяем как загадки.
            storageOfKnowledges = Riddle()
            storageOfKnowledges.RandomInput()
        container.store.append(storageOfKnowledges)
