FROM python

WORKDIR /home/ubuntu

COPY ./app.py /home/ubuntu

RUN pip install flask

EXPOSE 8080

CMD python /home/ubuntu/app.py

# Build the image