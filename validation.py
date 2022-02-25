res = worksheet.col_values(1)

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

if __name__ == '__main__':
    limit_check()