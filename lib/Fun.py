import openpyxl
 
def Datos (Archivo):
    worbook = openpyxl.load_workbook(Archivo)
    Hoja = worbook.active
    data = [ ]
    for row in Hoja.iter_rows(values_only=True):
        data.append(row)
    return data

def Red(data,numero):
    for row in data:
        for celda in row:
            if celda == numero:
                print('\033[34m{}\033[0m'.format(celda), end='')
            else:
                print(celda, end=' ')
        print()
        
def imprimir():
    numero = input('Ingresa tu Número: ')
    Archivo = input('Nombre del archivo "Eval.xlsm:" ')
    data = Datos(Archivo)
    Red(data,numero)
    