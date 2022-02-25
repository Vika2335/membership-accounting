from Scanner.Scanner import data

res = worksheet.col_values(1)
res1 = worksheet.col_values(2)

def unknowing():
    if abonid not in res:
        print('Неизвестный абонемент')

def faker():
    if clientid != res1:
        if abonid != res:
            print('Внимание, поддельный штрих-код')

def limit_check():
    for i in range(1, len(worksheet.col_values(1))):
        res3 = worksheet.row_values(i)
        res4 = worksheet.row_values(i)
        if abonid in res3:
            if clientid in res4:
                K = str('E' + str(i))
                M = str('F' + str(i))
                res5 = worksheet.get('M')
                res6 = worksheet.get('K')
                if res5 == res6:
                    print('Лимит посещений по абонементу исчерпан')            

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
            limit_check()
    else:
        print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    valid()