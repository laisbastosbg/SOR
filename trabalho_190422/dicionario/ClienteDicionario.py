import socket
import tkinter
import os

os.system("start /min python ServidorDicionario.py")


# # #  CONEXÃO SERVIDOR TRADUZIR # # #
def conServerTraduzir(idioma, entry_traduzir, traducao):
    traduzir = entry_traduzir.get()
    msg = traduzir + " " + idioma

    if len(traduzir) < 1:
        err_win = tkinter.Tk()
        err_win.title("Erro")
        err_lbl = tkinter.Label(err_win, text="Nenhuma palavra inserida.")
        err_lbl.grid(column=0, row=0)
    else:
        cl_socket.sendto(msg.encode(), server_addr)
        resposta, serv_addr = cl_socket.recvfrom(6000)
        try:
            traducao.delete('1.0', 'end')
        finally:
            traducao.insert("current", resposta.decode())


# # # CONEXÃO SERVIDOR ADICIONAR # # #
def add(original, traducao, idioma):
    msg = original + " " + traducao + " " + idioma
    cl_socket.sendto(msg.encode(), server_addr)
    answr, srvr_addr = cl_socket.recvfrom(60000)
    answr = answr.decode()
    return answr


def conServerAdicionar(original_entry, traducao_entry, idioma, new_win):
    original = original_entry.get()
    traducao = traducao_entry.get()
    if len(original) < 1 or len(traducao) < 1:
        err_win = tkinter.Tk()
        err_win.title("Erro")
        err_lbl = tkinter.Label(err_win, text="Nenhuma palavra inserida.")
        err_lbl.grid(column=0, row=0)
    else:
        answr = add(original, traducao, idioma)
        if answr == "Palavra já registrada":
            err_win = tkinter.Toplevel(new_win)
            err_win.title("Erro")
            err_lbl = tkinter.Label(err_win, text="Essa palavra já foi registrada.")
            err_lbl.grid(column=0, row=0)


# # #  JANELA ADICIONAR # # #
def janelaAdicionar(main_win):
    new_win = tkinter.Tk()
    main_win.destroy()
    new_win.title("Adicionar")
    new_win.geometry("275x155")
    new_win.config(bg="LightBlue4")
    frame_adicionar = tkinter.Frame(new_win)
    frame_adicionar.grid(padx=45, pady=30)
    frame_adicionar.config(bg="LightBlue4")
    lbl_original = tkinter.Label(frame_adicionar, text="Português:")
    lbl_original.grid(column=0, row=0)
    lbl_original.config(bg="LightBlue4")
    entry_original = tkinter.Entry(frame_adicionar, width=20)
    entry_original.grid(column=1, row=0, columnspan=2)
    lbl_traducao = tkinter.Label(frame_adicionar, text="Tradução:")
    lbl_traducao.grid(column=0, row=1)
    lbl_traducao.config(bg="LightBlue4")
    entry_traducao = tkinter.Entry(frame_adicionar, width=20)
    entry_traducao.grid(column=1, row=1, columnspan=2, pady=2)
    btn_adicionar_ingles = tkinter.Button(frame_adicionar, text="Inglês", command=lambda:
                                    (conServerAdicionar(entry_original, entry_traducao, "ingles", new_win)), width=26)
    btn_adicionar_ingles.grid(column=0, row=2, columnspan=2, pady=2)
    btn_adicionar_ingles.config(bg="LightBlue3")
    btn_adicionar_frances = tkinter.Button(frame_adicionar, text="Francês", command=lambda:
                                    (conServerAdicionar(entry_original, entry_traducao, "frances", new_win)), width=26)
    btn_adicionar_frances.grid(column=0, row=3, columnspan=2, pady=2)
    btn_adicionar_frances.config(bg="LightBlue3")
    new_win.protocol("WM_DELETE_WINDOW", lambda: (close(new_win)))

def close(new_win):
    new_win.destroy()
    mainWindow()

# # #  JANELA PRINCIPAL # # #
def mainWindow():
    main_win = tkinter.Tk()
    main_win.title("Dicionario")
    main_win.geometry("200x145")
    main_win.resizable(False, False)
    main_win.config(bg="LightBlue4")
    frame_traduzir = tkinter.Frame(main_win)
    frame_traduzir.config(bg="LightBlue4")
    frame_traduzir.grid(padx=35, pady=20)
    entry_traduzir = tkinter.Entry(frame_traduzir, width=20)
    entry_traduzir.grid(column=0, row=0, columnspan=2)

    btn_traduzir_ingles = tkinter.Button(frame_traduzir, text="Inglês",
                                         command=lambda: (conServerTraduzir("ingles", entry_traduzir, traducao)),
                                         width=7)
    btn_traduzir_ingles.grid(column=0, row=1, pady=2)
    btn_traduzir_ingles.config(bg="LightBlue3")
    btn_traduzir_frances = tkinter.Button(frame_traduzir, text="Francês",
                                          command=lambda: (conServerTraduzir("frances", entry_traduzir, traducao)),
                                          width=7)
    btn_traduzir_frances.grid(column=1, row=1, padx=1)
    btn_traduzir_frances.config(bg="LightBlue3")
    traducao = tkinter.Text(frame_traduzir, pady=4, width=15, bg='white', height=1, relief="sunken", borderwidth=1)
    traducao.grid(column=0, row=2, columnspan=2)
    btn_adicionar = tkinter.Button(frame_traduzir, text="Adicionar",
                                   command=lambda: (janelaAdicionar(main_win)), width=16)
    btn_adicionar.config(bg="LightBlue3")
    btn_adicionar.grid(column=0, columnspan=2, row=3, pady=2)
    main_win.mainloop()


# # #  CLIENTSOCKET # # #
server_addr = (socket.gethostname(), 9999)
cl_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


mainWindow()
