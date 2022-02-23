id = str(input())

if len(id) >= 3 and len(id) < 8:
    tire = id.find("-")
    if tire == -1:
        print('Не удалось распознать штрих-код')
    else:
        a = id[:tire]
        b = id[(tire + 1):]
        if len(a) == len(b) == 3:
            if b not in res:
                print('Неизвестный абонемент')

else:
    print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    print(id)