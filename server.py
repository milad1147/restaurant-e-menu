import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler
s = socketserver.TCPServer
s.server_name = ''  # Without this it does not work
s.server_port = ''
httpd = s(("localhost", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
