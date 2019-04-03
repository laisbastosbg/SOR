from socket import*
from tkinter import*
from os import*

system("start /min python Servidor.py")

# # # CONEXÃO COM O SERVIDOR # # #
def conServer():
    p = entry_peso.get()
    h = entry_alt.get()
    val = p + " " + h

    HOST = gethostname()
    PORT = 1234

    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((HOST, PORT))
    clientsocket.send(val.encode('ascii'))
    return clientsocket.recv(1024).decode('ascii')

# # # NOVA JANELA # # #
def new_window():
    new_window = Tk()
    new_window.title("Seu resultado")
    frame = Frame(new_window)
    frame.pack(padx=8, pady=8)
    lbl_resultado = Label(frame, text=conServer())
    lbl_resultado.pack()
    new_window.mainloop()

# # # JANELA PRINCIPAL # # #
master = Tk()
master.title("Cálculo do IMC")
master.geometry("150x125")
lbl_peso = Label(master, text="Peso:")
lbl_peso.grid(column=0, row=0, padx=10, pady=15)
entry_peso = Entry(width=5)
entry_peso.grid(column=1, row=0)
lbl_alt = Label(master, text="Altura:")
lbl_alt.grid(column=0, row=1)
entry_alt = Entry(width=5)
entry_alt.grid(column=1, row=1)
btn_enviar = Button(master, text="Enviar", command=new_window, width=15)
btn_enviar.grid(columnspan=2, row=2, pady=10, padx=15)
master.mainloop()
