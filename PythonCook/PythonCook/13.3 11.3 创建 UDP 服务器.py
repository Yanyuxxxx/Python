from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandle(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)

        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandle)
    serv.serve_forever()

