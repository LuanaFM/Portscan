import socket

host = input("Informe o endereco que deseja scannear: ")
ip = socket.gethostbyname(host)

for porta in range (1,65535):
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan.settimeout(0.10)
    result = scan.connect_ex((ip,porta))
    if result == 0:
        print (" Porta: ",str(porta) ,"<---ABERTA")
        scan.close()
