import socket

class ServidorWeb:
    def __init__(self, HOST, PORTA):
        self.HOST = HOST
        self.PORTA = PORTA
        self.__socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def iniciarServidor(self):
        self.__socketServer.bind((self.HOST, self.PORTA))
        self.__socketServer.listen(5)
         
        while True:
            try:
                conexao_cliente, endereco_cliente = self.__socketServer.accept()
                requisicao = conexao_cliente.recv(1024).decode()
                requisicao = str(requisicao).split(' ')
                if requisicao[0] == 'GET':
                    print(requisicao[1])
                    data = self.__get(requisicao[1])
                    conexao_cliente.sendall(data.encode())
                    
                conexao_cliente.close()
                gc.collect()
            except KeyboardInterrupt:
                conexao_cliente.close()
                self.__socketServer.close()
                break
            
    def __get(self, requisicao):
        
        try:
            if requisicao == '/':
                arquivo = open('./files/index.html').read()
            else:
                arquivo = open('./files' + requisicao).read()
        except:
            return 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        
        response_header = 'HTTP/1.1 200 OK\r\n'
        
        if '.html' in requisicao:
            response_header += 'Content-Type: text/html\r\n'
        elif '.css' in requisicao:
            response_header += 'Content-Type: text/css\r\n'
        elif '.png' in requisicao:
            response_header += 'Content-Type: image/png\r\n'
        elif '.ico' in requisicao:
            response_header += 'Content-Type: image/x-icon\r\n'
        else:
            response_header += 'Content-Type: none\r\n'
        
        
        return response_header + 'Content-Length: '  +  str(len(arquivo)) + '\r\n\r\n' + arquivo