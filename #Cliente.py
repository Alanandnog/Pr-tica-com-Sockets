#Cliente
import socket

# Configurações do cliente
host = '127.0.0.1'
porta = 7555

# Criação do socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
cliente.connect((host, porta))
print(f"[*] Conectado a {host}:{porta}")

while True:
    # Solicita ao usuário que digite uma mensagem
    mensagem = input("Digite uma mensagem para o servidor (ou 'encerrar' para sair): ")

    # Envia a mensagem para o servidor
    cliente.send(mensagem.encode('utf-8'))

    # Verifica se o usuário deseja encerrar a conexão
    if mensagem.lower() == 'encerrar':
        break

    # Recebe a resposta do servidor
    resposta = cliente.recv(1024).decode('utf-8')
    print(f"Servidor: {resposta}")

# Encerra a conexão
cliente.close()