import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input(str("enter the host name : "))  # Enter the server's hostname or IP address
port = 8080

s.connect((host, port))
print("connected")

filename = input(str("please enter the filename: "))

# Get the current working directory
current_directory = os.getcwd()

# Specify the full path where you want to save the downloaded file
download_path = os.path.join(current_directory, "receiver_folder", filename)

with open(download_path, "wb") as file:
    file_data = s.recv(1024)
    file.write(file_data)

print("file has been downloaded successfully")
