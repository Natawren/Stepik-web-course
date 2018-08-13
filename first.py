
import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, channel, details):
        self.channel = channel
        self.details = details
        threading.Thread.__init__(self)

    def run(self):
        print
        'Received connection:', self.details[0]
        self.channel.recv(1024)
        self.channel.close()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.72.1', 2222))
server.listen(10)

while True:
    channel, details = server.accept()
    ClientThread(channel, details).start()