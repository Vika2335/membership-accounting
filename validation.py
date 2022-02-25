id = str(input())

res = worksheet.col_values(1)
res1 = worksheet.col_values(2)

def faker():
    if clientid != res1:
        if abonid != res:
            print('Внимание, поддельный штрих-код')
def valid():
    if len(id) >= 3:
        tire = id.find("-")
        if tire == -1:
            print('Не удалось распознать штрих-код')
        else:
            clientid = id[:tire]
            abonid = id[(tire + 1):]
            faker()
else:
    print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    print(id)
