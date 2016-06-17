FROM progrium/busybox
RUN opkg-install python-pip 
RUN pip install flask
ADD ../../ingest-service /

CMD [ "/app.py" ]
