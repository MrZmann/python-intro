import argparse
import socket

parser = argparse.ArgumentParser(
                    prog='Server',
                    description='Multiplies numbers sent to localhost:65432 by the input number, sends the result back to the client')

parser.add_argument("-m", "--multiplier", required=True, type=int, help="Multiplier value")
args = parser.parse_args()
multiplier = args.multiplier

HOST = "localhost"  # Only listening to connections from my same machine
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# TCP connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Tell the OS that I want to listen for connections on HOST from port=PORT
    s.bind((HOST, PORT))

    # Wait for clients to connect
    s.listen()

    # This method returns when I've gotten a connection to a client
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(f'Received data: {data}')
            if not data:
                print('Client closed connection')
                break
            # Ignore non-numeric data
            if not data.isnumeric():
                print('Ignoring non-numeric data')
                continue

            toSend = str(int(data) * multiplier)
            print(f'Sending {toSend} to client')

            conn.sendall(toSend.encode('utf-8'))

