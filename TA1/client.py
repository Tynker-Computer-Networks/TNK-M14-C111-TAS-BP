import socket
from threading import Thread
# Import tkinter as tk


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

# Create GUI class

    # Create initializer method
    
        # Create an instance variable named window using TK()
        
        # Set title of the window using title() method
        
        # Make window resizable to false using resizable() method
        
        # Use configure() method to set width and height of the window
        
        # Call mainloop() method on window to tell that this component to be run
        

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