import socket

def run(host='127.0.0.1', port=4200):
    with socket.socket() as s:
        s.connect((host, port))
        for i in range(10):
            data = input('>>')
            s.sendall(data.encode())
            res = s.recv(1024)
            print(res)
            print(f'={res.decode()}')


if __name__ == '__main__':
    run()



