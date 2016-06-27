FROM progrium/busybox
RUN opkg-install python-pip 
RUN pip install flask flask-sqlalchemy tweepy
ADD ../../ingest-service /

CMD [ "/app.py" ]
