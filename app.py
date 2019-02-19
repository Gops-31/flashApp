from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_key" 

@app.route('/',)
def func():
   return "hello world"

if __name__ == '__main__':
  HOST = environ.get('SERVER_HOST', 'localhost')
  try:
      PORT = int(environ.get('SERVER_PORT', '5555'))
  except ValueError:
      PORT = 5555
     
  app.run(HOST, port=PORT)
