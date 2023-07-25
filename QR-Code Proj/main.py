# necessário ter a biblioteca pyqrcode, pypng e pyio

import pyqrcode as pqr  # criar um QRCode
import io               # criar um arquivo
import png              # criar um PNG
from tkinter import *   # criar um Janelas de iterface

print('Criador de QRCode')
qrtexto = input('Digite o texto que será transformado em QRCode: ')

code =  pqr.create('qrtexto')
code_xbm = code.xbm(scale=5)

jan = Tk()

code_bmp = BitmapImage(data=code_xbm)
code_bmp.config(foreground="black")
code_bmp.config(background="white")

label = Label(image=code_bmp)
label.pack()

jan.mainloop()

# outra forma:
'''
url = pqr.create('Olá, este QR-Code foi gerado com Python')
with open('code.png', 'wb') as fstream:
    url.png(fstream, scale=5)

buffer = io.BytesIO()
url.png(buffer, scale=5)
print(list(buffer.getvalue()))
'''