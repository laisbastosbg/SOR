from socket import*

# # # CALCULO DO IMC # # #
def calcIMC(val):
    p, h = val.split()

    if float(p) > 0 and float(h) > 0:
        IMC = float(p) / float(h) ** 2
        print("%.1f" % IMC)
        if IMC < 18.5:
            resultado = "Voce esta abaixo do peso."
        elif 18.5 <= IMC <= 24.9:
            resultado = "Seu peso esta na media."
        elif 25 <= IMC <= 29.9:
            resultado = "Voce esta acima do peso."
        elif 30 <= IMC <= 34.9:
            resultado = "Voce esta com obesidade de grau 1."
        elif 25 <= IMC <= 39.9:
            resultado = "Voce esta com obesidade de grau 2."
        elif 40 <= IMC:
            resultado = "Voce esta com obesidade de grau 3."
    else:
        resultado = "Algo deu errado. Tente novamente."

    return resultado

# # # SEVIDOR # # #
HOST = gethostname()
PORT = 1234

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen(5)

# # # CONEXÃO COM O CLIENTE # # #
while True:
    clientsocket, addr = serversocket.accept()
    print("Conectado com", addr)
    val = clientsocket.recv(1024).decode('ascii')
    clientsocket.send(calcIMC(val).encode('ascii'))
    clientsocket.close()