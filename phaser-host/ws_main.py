import logging
import threading
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

def websocket_app(environ, start_response):
    if environ["PATH_INFO"] == '/echo':
        ws = environ["wsgi.websocket"]
        message = ws.receive()
        ws.send(message)

def thread_function(name):
    server = pywsgi.WSGIServer(("", 4309), websocket_app,
        handler_class=WebSocketHandler)
    server.serve_forever()

if __name__ == '__main__':
    logging.info("[PROGRAM START]")

    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    # x.start()
    server = pywsgi.WSGIServer(("", 4309), websocket_app,
        handler_class=WebSocketHandler)
    server.serve_forever()