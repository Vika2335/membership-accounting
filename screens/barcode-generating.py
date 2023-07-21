from barcode import Code128
from barcode.writer import ImageWriter
from gspread import spreadsheet
import os

clientid = 0
abonid = 0

def Barcoding():
    global clientid, abonid
    res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Список, из которого будет браться ИД клиента
    res1 = [1, 3, 9, 10, 11, 15, 16, 18, 20]  # Список, из которого будет браться ИД абонемента
    resname = ["ЗАС", "ЯСФ", "ГВВ",
               "АУА", "МЕВ", "ЗАС",
               "ДАА", "NULL", "NULL",
               "ЗАС"]  # Список с именами в качестве значений, по которым ведётся поиск для ИД клиента/абонемента
    for i in range(len(resname)-1, 1, -1):
        if resname[i] == "ГВВ":
            clientid = res[i]  # ИД клиента, который берётся из списка ИД клиентов
            abonid = res1[i]  # ИД абонемента, который берётся из списка абонементов
            break
    with open('somefile.jpeg', 'wb') as f:
        Code128(f'{clientid}-{abonid}', writer=ImageWriter()).write(f)

def BarcodeDelete():
    os.remove('somefile.jpeg')

if __name__ == "__main__":
    Barcoding()
    #Здесь будет вызвана функция "Отправить штрих-код"
    #BarcodeDelete() функция удаляет файл после выполнения предыдущих функций
