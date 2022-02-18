from barcode import Code128
from barcode.writer import ImageWriter

def Barcoding():
    with open('somefile.jpeg', 'wb') as f:
        clienid = 0
        abonid = 0
        Code128(f'{clienid}-{abonid}', writer=ImageWriter).write(f)

Barcoding()