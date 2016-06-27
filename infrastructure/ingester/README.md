
docker run -p 5555:5555 flask_helloworld

uwsgi --http-socket 127.0.0.1:3031 --wsgi-file hello.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191


