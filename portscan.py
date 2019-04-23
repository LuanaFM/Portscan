import socket

host = input("Informe o endereco que deseja scannear: ") 
ip = socket.gethostbyname(host)                               # Traduz nome para IP

for porta in range (1,65535):
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPV4 e SOCK_STREAM = TCP
    scan.settimeout(0.10)                                     #Tempo para tentativa de conexão
    result = scan.connect_ex((ip,porta))
    if result == 0:                                           #Resultado zero significa conexão bem sucedida. 
        print (" Porta: ",str(porta) ,"<---ABERTA")
        scan.close()
