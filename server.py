import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler
s = socketserver.TCPServer
s.server_name = '' #тoва не разбрах за какво ми е, в примерите го няма, но без него не икса да запали
s.server_port = '' #тoва също
httpd = s(("localhost", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()