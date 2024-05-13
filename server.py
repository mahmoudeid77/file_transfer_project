import socket

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =socket.gethostbyname(socket.gethostname())
s.bind((host, 8080))
s.listen(5)
print("listening....")
print(host)
print("waiting for any incoming connections...")
conn , addr = s.accept()
print(addr, "has connected.")

filename =input(str("please enter the filename: "))
file =open(filename, "rb")
file_data =file.read(1024)
conn.send(file_data)
print("file has been send successfully")
