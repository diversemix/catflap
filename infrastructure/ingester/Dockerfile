FROM progrium/busybox
RUN opkg-install python-pip 
RUN pip install flask
ADD hello.py /
CMD chmod +x /hello.py
CMD [ "/hello.py" ]
