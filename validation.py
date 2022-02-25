id = str(input())

res = worksheet.col_values(1)

def unknowing():
    if abonid not in res:
        print('Неизвестный абонемент')
def valid():
    if len(id) >= 3:
        tire = id.find("-")
        if tire == -1:
            print('Не удалось распознать штрих-код')
        else:
            clientid = id[:tire]
            abonid = id[(tire+1):]
            unknowing()  
    else:
        print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    valid()
