import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(f'El servidor está en línea {host}:{port}')

clientes = []
usuarios = []

def transmision(mensaje, _cliente):
    for cliente in clientes:
        if cliente != _cliente:
            try:
                cliente.send(mensaje)
            except:
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)

def manejo_mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            if mensaje:
                transmision(mensaje, cliente)
            else:
                raise ConnectionResetError
        except (ConnectionResetError, ConnectionAbortedError):
            index = clientes.index(cliente)
            usuario = usuarios[index]
            transmision(f'Chat: {usuario} se desconectó'.encode('utf-8'), cliente)
            print(f'{usuario} se ha desconectado')
            clientes.remove(cliente)
            usuarios.remove(usuario)
            cliente.close()
            break

def recibir_conecciones():
    while True:
        cliente, direccion = server.accept()
        cliente.send('@usuario'.encode('utf-8'))
        usuario = cliente.recv(1024).decode('utf-8')

        clientes.append(cliente)
        usuarios.append(usuario)

        print(f'{usuario} está conectado con {str(direccion)}')

        mensaje = f'Chat: {usuario} se unió al chat'.encode('utf-8')
        transmision(mensaje, cliente)
        cliente.send('Conectado al servidor'.encode('utf-8'))

        thread = threading.Thread(target=manejo_mensajes, args=(cliente,))
        thread.start()

recibir_conecciones()
