import socket
import json


# # # FUNÇÃO PARA ADICIONAR # # #

def add(dicio, traducao, idioma):
    try:
        dicio[palavra].update({idioma: traducao})
    except KeyError:
        dicio[palavra] = {idioma: traducao}
    with open("Dict.json", "w", encoding="utf-8") as d:
        json.dump(dicio, d)
    serv_socket.sendto("Registrado com sucesso".encode(), cl_addr)


def adicionar(palavra, traducao, idioma):
    try:
        with open("Dict.json", "r") as D:
            dicio = json.load(D)
            try:
                if idioma in dicio[palavra]:
                    serv_socket.sendto("Palavra já registrada".encode(), cl_addr)
                else:
                    add(dicio, traducao, idioma)
            except KeyError:
                add(dicio, traducao, idioma)
    except FileNotFoundError:
        dicio = {palavra: {idioma: traducao}}
        with open("Dict.json", "w", encoding="utf-8") as D:
            json.dump(dicio, D)
        serv_socket.sendto("Registrado com sucesso".encode(), cl_addr)

# # # FUNÇÃO PARA TRADUZIR # # #
def traduzir(palavra, idioma):
    try:
        with open("Dict.json", "r") as D:
            resposta = json.load(D)
            serv_socket.sendto(resposta[palavra][idioma].encode(), cl_addr)
    except:
        serv_socket.sendto("Não encontrado.".encode(), cl_addr)


# # # SERVIDOR # # #
server_addr = (socket.gethostname(), 9999)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_socket.bind(server_addr)

while True:
    msg, cl_addr = serv_socket.recvfrom(60000)
    print("Conectado com", cl_addr)
    msg = msg.decode().lower().split()

    if len(msg) == 2:
        palavra = msg[0]
        idioma = msg[1]
        traduzir(palavra, idioma)
    else:
        palavra = msg[0]
        traducao = msg[1]
        idioma = msg[2]
        adicionar(palavra, traducao, idioma)
