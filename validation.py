from Scanner.Scanner import data

res = worksheet.col_values(1)
res1 = worksheet.col_values(2)

def unknowing():
    if abonid not in res:
        print('Неизвестный абонемент')

def faker():
    if (clientid not in res1) or (abonid not in res):
        print('Внимание, поддельный штрих-код')

def valid():
    if len(data) >= 3:
        tire = data.find("-")
        if tire == -1:
            print('Не удалось распознать штрих-код')
        else:
            clientid = data[:tire]
            abonid = data[(tire+1):]
            unknowing()
            faker()
    else:
        print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    valid()
