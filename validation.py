id = str(input())

res = worksheet.col_values(1)
res1 = worksheet.col_values(2)

if len(id) >= 3 and len(id) < 8:
    tire = id.find("-")
    if tire == -1:
        print('Не удалось распознать штрих-код')
    else:
        a = id[:tire]
        b = id[(tire + 1):]
        if len(a) == len(b) == 3:
            if not a == res1:
                if not b == res:
                    print('Внимание, поддельный штрих-код')

else:
    print("Не удалось распознать штрих-код")

if __name__ == '__main__':
    print(id)