from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile(b"<!DOCTYPE html>")
        self.wfile(b"<html lang='en'>")
        self.wfile(b"<head>")
        self.wfile(b"<title>hello title! </title>")
        self.wfile(b"</head>")
        self.wfile(b"<body>")
        self.wfile(b"hello world")
        self.wfile(b"</body>")
        self.wfile(b"</html>")
    
port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address,HTTPServer_RequestHandler)

httpd.serve_forever()