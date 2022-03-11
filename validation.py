from Scanner.Scanner import data
import re

res = worksheet.col_values(1)
#первая колонка таблицы (колонка с абонементами)
res1 = worksheet.col_values(2)
#вторая колонка таблицы (колонка с клиентами)

def unknowing():
    if abonid not in res:
        print('Неизвестный абонемент')
        #функция, которая проверяет есть ли в первой колонке с абонементами ИД абонемента, если нет, выводит ошибку

def faker():
    if (clientid not in res1) or (abonid not in res):
        print('Внимание, поддельный штрих-код')
        #функция, которая проверяет есть ли в первой колонке ИД абонемента ИЛИ во второй ИД клиента, если какого-то одного нет, то ошибка

def limit_check():
    for i in range(1, len(worksheet.col_values(1))):
        #длина первой колонки
        res3 = worksheet.row_values(i)
        res4 = worksheet.row_values(i)
        #список строк
        if abonid in res3:
            if clientid in res4:
                K = str('E' + str(i)) #кол-во занятий
                M = str('F' + str(i)) #пройденные занятия
                #присваиваем переменным значения ячеек, чтобы столбцы оставались одни и те же (константы), а строчки перебирались
                #проверяем есть ли ИД абонемента и ИД клиента в списках
                res5 = worksheet.get('M')
                res6 = worksheet.get('K')
                #заданные ячейки
                if res5 == res6:
                    print('Лимит посещений по абонементу исчерпан')   
                    #если колонка с кол-вом занятий равнаколонке с пройднными занятиями, то абонемент закончился

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
        #функция, которая отдает строки с ИД клиента и абонемента через findall и вызывает другие функции 
      
if __name__ == '__main__':
    valid()
