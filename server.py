from pynput.keyboard import Key, Controller
import socket

h = input("Host: ")
p = int(input("Port: "))
keyboard = Controller()
while(True):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((h, p))
		s.listen()
		conn, addr = s.accept()
	with conn:
		while True:
			data = conn.recv(1024)
			if not data:
				break
			detected_key = data.decode("UTF-8")
			detected_key = detected_key.replace("'", '')
			detected_key = str(detected_key)
			print(detected_key)
			if(len(str(detected_key)) > 1):
				keyboard.press(eval(str(detected_key)))
				keyboard.release(eval(str(detected_key)))
				break
			keyboard.press(detected_key)
			keyboard.release(detected_key)

			conn.sendall(data)