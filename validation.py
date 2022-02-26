from Scanner.Scanner import data
import re

res = worksheet.col_values(1)
res1 = worksheet.col_values(2)

def unknowing():
    if abonid not in res:
        print('Неизвестный абонемент')

def faker():
    if (clientid not in res1) or (abonid not in res):
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
    result = re.findall(r'^(\d+)-(\d+)', data)
    if result and len(result) == 1:
        clientid = result[0][0]
        abonid = result[0][1]
        unknowing()
        faker()
        limit_check()
    else:
        print('Не удалось распознать штрих-код')
      
if __name__ == '__main__':
    valid()
