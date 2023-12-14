from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write('GET'.encode())


def TestHandler(context):
  return context.text("it works!")


class Hono(BaseHTTPRequestHandler):

  def __init__(self):
    pass

  routes = [{
      "method": "GET",
      "path": "/__HONOPY_TEST__",
      "handler": TestHandler
  }]

  def get(self, config):
    pass

  def post(self, config):
    pass

  class Context:
    def __init__(self, request):
      self.req = request
      # params...

    def text(self, httpClass, text, config):
      httpClass.send_reponse(config.status if config.status is not None else 200)
      httpClass.send_header('Content-type', 'text/plain; charset=utf-8')
      for header in config:
        httpClass.send_header(header, config[header])
      httpClass.end_headers()
      httpClass.wfile.write(text.encode())
      
    def body(self, httpClass, text, config):
      httpClass.send_reponse(config.status if config.status is not None else 200)
      httpClass.send_header('Content-type', config.type)
      for header in config:
        httpClass.send_header(header, config[header])
      httpClass.end_headers()
      httpClass.wfile.write(text.encode())

    def json(self, httpClass, json, config):
      httpClass.send_reponse(config.status if config.status is not None else 200)
      httpClass.send_header('Content-type', 'application/json; charset=utf-8')
      for header in config:
        httpClass.send_header(header, config[header])
      httpClass.end_headers()
      httpClass.wfile.write(json.dumps(json).encode())

  def do_GET(self):
    path = ""
    # matching
    # to Handler
    # pass Context
    # return Handler
  def do_POST(self):
    path = ""
    # matching
    # to Handler
    # pass Context
    # return Handler

  def fire(self, config):
    port = config.port if config.port is not None else 8080
    host = config.host if config.host is not None else "localhost"
    server_address = (host, port)
    httpd = HTTPServer(server_address, self)
    httpd.serve_forever()
