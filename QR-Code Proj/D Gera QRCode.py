# necessário ter a biblioteca pyqrcode, pypng e pyio

import pyqrcode as pqr  # criar um QRCode
import io               # criar um arquivo
import png              # criar um PNG
from tkinter import *   # criar um Janelas de iterface

# função de criar o QRCode
def exeqrcode():
    qrtexto = qrtext_entry.get()                                # puxa o texto digitado

    code = pqr.create(qrtexto)                                  # cria o QRCode da biblioteca pyqrcode
    code_xbm = code.xbm(scale=5)                                # cria o PNG pela biblioteca pypgn

    code_bmp = BitmapImage(data=code_xbm)                       # cria um BitmapImage
    code_bmp.config(foreground="black", background="white")     # configura a cor do BitmapImage

    code_label.config(image=code_bmp)                           # configura na janela a imagem do QRCode
    code_label.image = code_bmp                                 # exibe a imagem do QRCode

jan = Tk()                                                      # cria uma janela
jan.title('DIEGO Gera QR-Code')                                 # titulo da janela


jan.geometry('300x300')                                         # Dimensão da janela
# jan.resizable(False, False)                                   # janela não redimensiona -> foi tirado pq a imagem pode ser maior 


qrtext_label = Label(jan,text='Digite o texto para ser transformado em QRCode:')   # Texto de orientaçao
qrtext_label.pack()                                                                # Texto que vai ser QRCode


qrtext_entry = Entry(jan)                                                          # Entrada doexto
qrtext_entry.pack() 


generate_button = Button(jan, text='Gerar QR-Code', command=exeqrcode)              # Botao para gerar o QRCode
generate_button.pack()

code_label = Label(jan)                                                             # Rotulo para exibir o QRCode gerado
code_label.pack()

jan.mainloop()                                                                      # mantem a janela aberta       #FIM