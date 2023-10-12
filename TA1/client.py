import socket
from threading import Thread
# Import tkinter as tk


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

# Create GUI class that inherits Tk

    # Create initializer method
    
        # Call __init__ method of parent using super
        
        # Set title using title() method on self
        
        # Make window resizable to false using resizable() method on self
        
        # Use configure() method to set width, height and bg of the window on self
        
        
        

# Create app object using GUI class

# Call mainloop method from app object

# Comment rest of the code
nickname = input("Choose your nickname: ")

client.connect((ip_address, port))
print("Connected with the server...")

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break
        

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()