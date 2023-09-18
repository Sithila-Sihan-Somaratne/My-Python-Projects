from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, "UTF-8"))


httpd = HTTPServer(("localhost", 8000), MyServer)
httpd.serve_forever()
