# Chat-en-tiempo-real
# Desafío de Chat con Sockets y Threads

Este proyecto es una implementación simple de un sistema de chat utilizando sockets y threads en Python. El sistema consta de un servidor de chat y un cliente de chat, ambos capaces de enviar y recibir mensajes en tiempo real.

## Estructura del Proyecto

- **Servidor de Chat**: Maneja las conexiones de múltiples clientes, transmite mensajes entre ellos y gestiona las desconexiones.
- **Cliente de Chat**: Permite a los usuarios conectarse al servidor, enviar y recibir mensajes, y desconectarse del chat.


## Comportamiento

- **Servidor**:
  - Escucha conexiones en `127.0.0.1:55555`.
  - Permite que múltiples clientes se conecten simultáneamente.
  - Transmite mensajes entre clientes y maneja desconexiones.

- **Cliente**:
  - Solicita el nombre de usuario y se conecta al servidor.
  - Permite enviar y recibir mensajes.
  - Usa `@chau` para desconectarse del chat.

## Notas

- Asegúrate de ejecutar el servidor antes de iniciar los clientes.
- Puedes abrir múltiples instancias del cliente para probar la comunicación entre varios usuarios.

