FROM alpine:3.8

RUN apk add --no-cache python py-pip

RUN mkdir -p /app

RUN pip install bottle

COPY py/*.py /app

CMD python /app/rest_server.py