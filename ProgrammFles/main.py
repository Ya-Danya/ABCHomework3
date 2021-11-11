import sys
import string

from extender import *

# main.
if __name__ == '__main__':
    from time import perf_counter
    startTime = perf_counter()
    #Input string format 1: main.py nameOfInputFile nameOfOutputFile1 nameOfOutputFile2
    #Input string format 2: main.py nameOfInputFile
    #Input string format 3: main.py numberOfRandomElements
    # Проверка правильности ввода из командной строки.
    # Случай, при котором указаны 2 файла вывода и файл ввода.
    randomize = False
    if len(sys.argv) == 4:
        inputFileName  = sys.argv[1]
        outputFileName1 = sys.argv[2]
        outputFileName2 = sys.argv[3]
    elif len(sys.argv) == 2:
        # Определение рандомный ли ввод, или просто нет файла вывода.
        try:
            length = int(sys.argv[1])
            randomize = True
        # Ввод не рандомный, а файлы вывода стандартные.
        except:
            inputFileName  = sys.argv[1]
        outputFileName1 = "output1.txt"
        outputFileName2 = "output2.txt"
    elif len(sys.argv) == 1:
        print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName>]")
        exit()
    print('==> Start')
    container = Container()

    ofile1 = open(outputFileName1, 'w')
    ofile2 = open(outputFileName2, 'w')
    if randomize:
        RndStrArray(container, length)
    else:
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()
        strArray = str.split("\n")
        if len(strArray) == 1:
            print("It is an empty file")
            ofile1.write("It is an empty file")
            ofile2.write("It is an empty file")
            exit()
        else:
            knlgNum = ReadStrArray(container, strArray)
    # Вывод в консоль.
    container.Print()
    # Вывод в файл1.
    container.Write(ofile1)
    ofile1.close()
    container.DeleteElements()
    # Вывод в файл2.
    container.Write(ofile2)
    ofile2.close()

    print('==> Finish')
    endTime = perf_counter()
    print("Time: {:.1f}".format((endTime - startTime)*1000))