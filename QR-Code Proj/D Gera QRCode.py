# necessário ter a biblioteca pyqrcode, pypng e pyio

import pyqrcode as pqr  # criar um QRCode
import io               # criar um arquivo
import png              # criar um PNG
from tkinter import *   # criar um Janelas de interface
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# função de criar o QRCode

# Variável global para armazenar o último QR gerado
last_qr_img = None
last_qr_code = None

def exeqrcode():
    global last_qr_img, last_qr_code
    qrtexto = qrtext_entry.get()                                # puxa o texto digitado
    if not qrtexto:
        messagebox.showwarning("Atenção", "Digite um texto para gerar o QRCode.")
        return
    code = pqr.create(qrtexto)                                  # cria o QRCode da biblioteca pyqrcode
    code_xbm = code.xbm(scale=5)                                # cria o PNG pela biblioteca pypng
    code_bmp = BitmapImage(data=code_xbm)                       # cria um BitmapImage
    code_bmp.config(foreground="black", background="white")     # configura a cor do BitmapImage
    code_label.config(image=code_bmp)                           # configura na janela a imagem do QRCode
    code_label.image = code_bmp                                 # exibe a imagem do QRCode
    # Salva o último QR gerado como imagem PIL para salvar depois
    buffer = io.BytesIO()
    code.png(buffer, scale=8)
    buffer.seek(0)
    last_qr_img = Image.open(buffer).convert("RGB")
    last_qr_code = code

jan = Tk()                                                      # cria uma janela
jan.title('DIEGO Gerador de QR-Code')                                 # titulo da janela

jan.geometry('320x350')                                         # Dimensão da janela
# jan.resizable(False, False)                                   # janela não redimensiona -> foi tirado pq a imagem pode ser maior 

qrtext_label = Label(jan,text='Digite o texto para ser transformado em QRCode:')   # Texto de orientaçao
qrtext_label.pack(pady=(10, 0))                                                                # Texto que vai ser QRCode

qrtext_entry = Entry(jan)
qrtext_entry.pack(pady=(5, 10))


# Novo frame para centralizar os botões
frame_botoes = Frame(jan)
frame_botoes.pack(pady=(0, 10))

generate_button = Button(frame_botoes, text='Gerar QR-Code', command=exeqrcode, width=15, height=2)
generate_button.grid(row=0, column=0, padx=10, pady=5)

# Ícone de disquete (salvar) em base64 (pequeno, preto)
icon_save = (
    'R0lGODlhEAAQAPQAAP///wAAAMLCwkJCQmZmZjY2NpKSkoqKip6enqCgoJmZmf///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAABAAIf8LTkVUU0NBUEUyLjADAQAAACwAAAAAEAAQAAAFLCAljmRpnmiqrmzrvnAsz3Rt33iu73AQA7'
)
icon_save_img = PhotoImage(data=icon_save)

def salvar_qrcode():
    global last_qr_img
    if last_qr_img is None:
        messagebox.showinfo("Salvar QRCode", "Primeiro gere um QRCode.")
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png"), ("Todos os arquivos", "*.*")],
        title="Salvar QRCode como..."
    )
    if file_path:
        try:
            last_qr_img.save(file_path, format="PNG")
            messagebox.showinfo("Sucesso", f"QRCode salvo em:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Erro ao salvar", str(e))

save_button = Button(frame_botoes, text='Salvar', command=salvar_qrcode, width=15, height=2)
save_button.grid(row=0, column=1, padx=10, pady=5)

code_label = Label(jan)
code_label.pack(pady=(20, 0))

jan.mainloop()                                                                      # mantem a janela aberta       #FIM
