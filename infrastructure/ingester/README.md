
docker run -p 5555:5555 flask_helloworld
uwsgi --http-socket 127.0.0.1:3031 --wsgi-file hello.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)

