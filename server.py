import http.server
import socketserver
import configparser
import urllib

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import tensorflow.keras as keras
import numpy as np

config = configparser.ConfigParser()
config.read('model_v4/model.conf')

model = keras.models.load_model(config.get('model', 'model'))
print(f"Loaded Model: {model}")
tokenizer = tokenizer_from_json(open(config.get('model', 'tokens'), 'r').read())
print(f"Loaded Tokenizer: {tokenizer}")

class Server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/api/request/'):
            data = self.path.replace('/api/request/', '')
            data = urllib.parse.unquote(data)
            message = data
            size = 36

            print(message)
            for _ in range(size):
                sequence = tokenizer.texts_to_sequences([message])[0]
                sequence = pad_sequences([sequence], maxlen=int(config.get('model', 'max_length')) - 1, padding='pre')
                prediction = np.argmax(model.predict(sequence), axis=1)
                index = prediction[0]
                message += ' ' + tokenizer.index_word[index]
            
            message = message[len(data):]
            message = message.replace(".", ". ").replace("\n\n", "\n").replace("\r\n", "\\r\\n").replace("  ", " ")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))
            return
        
        
        self.send_response(200)
        if self.path == '/':
            self.path = '/index.html'
        
        if self.path.split('.')[-1] == 'html':
            self.send_header('Content-type', 'text/html')
        elif self.path.split('.')[-1] == 'css':
            self.send_header('Content-type', 'text/css')
        elif self.path.split('.')[-1] == 'js':
            self.send_header('Content-type', 'text/javascript')
        elif self.path.split('.')[-1] == 'ico':
            self.send_header('Content-type', 'image/vnd.microsoft.icon')
        self.end_headers()
        
        try:
            with open(f"client{self.path}", "r", encoding="utf-8") as file:
                self.wfile.write(bytes(file.read(), 'utf-8'))
        except:
            self.send_response(404)
        
        return

handler = Server
PORT = 4000
server = socketserver.TCPServer(("", PORT), handler)

print(f"Serving at http://localhost:{PORT}")
server.serve_forever()