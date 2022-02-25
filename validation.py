from Scanner.Scanner import data

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
            clientid = data[:tire]
            abonid = data[(tire+1):]
            unknowing()  
    else:
        print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    valid()
