##Servidor
import socket
import random

# Configurações do servidor
host = '127.0.0.1'
porta = 7555

# Lista de respostas aleatórias
respostas = ["Mensagem recebida com sucesso!",
             "Entendi sua mensagem.",
             "Recebido! Obrigado por compartilhar.",
             "A mensagem chegou ao destino."]

# Criação do socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao endereço e porta especificados
servidor.bind((host, porta))

# Espera por conexões
servidor.listen()

print(f"[*] Aguardando por conexões em {host}:{porta}")

# Aceita a conexão do cliente
cliente, endereco = servidor.accept()
print(f"[*] Conexão estabelecida de {endereco}")

while True:
    # Recebe mensagem do cliente
    mensagem = cliente.recv(1024).decode('utf-8')

    # Imprime a mensagem do cliente
    print(f"Cliente: {mensagem}")

    # Verifica se a mensagem é para encerrar a conexão
    if mensagem.lower() == 'encerrar-server':
        print("O cliente digitou o código de administrador e encerrou o servidor")
        break

    # Escolhe uma resposta aleatória e a envia de volta ao cliente
    resposta_aleatoria = random.choice(respostas)
    cliente.send(resposta_aleatoria.encode('utf-8'))

# Encerra a conexão
cliente.close()
servidor.close()