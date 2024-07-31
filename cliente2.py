import socket
import threading

usuario = input('Por favor ingrese su usuario: ')

host = '127.0.0.1'
port = 55555

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, port))

def recibir_mensaje():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')

            if mensaje == '@usuario':
                cliente.send(usuario.encode('utf-8'))
            elif mensaje == '@chau':
                print('El servidor ha cerrado la conexión.')
                cliente.close()
                break
            else:
                print(mensaje)
        except:
            print('Ha ocurrido un error')
            cliente.close()
            break

def escribir_mensaje():
    while True:
        try:
            mensaje = input()
            if mensaje == '@chau':
                cliente.send(mensaje.encode('utf-8'))
                print('Desconectado del chat.')
                cliente.close()
                break
            else:
                cliente.send(f"{usuario} {mensaje}".encode('utf-8'))
        except EOFError:
            print('Se ha desconectado.')
            cliente.close()
            break
        except:
            print('Ha ocurrido un error')
            cliente.close()
            break

# Mostrar mensaje de bienvenida
print("Bienvenido al chat, escriba @chau si desea salir del chat.")

recibir_thread = threading.Thread(target=recibir_mensaje)
recibir_thread.start()

escribir_thread = threading.Thread(target=escribir_mensaje)
escribir_thread.start()
