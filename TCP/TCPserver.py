from socket import *
def run_server():
    serverPort = 4200
    host = '127.0.0.1'
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((host, serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")

    while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.upper()
        print(capitalizedSentence.decode())
        connectionSocket.send(capitalizedSentence)
        connectionSocket.close()

if __name__ == '__main__':
  run_server()

