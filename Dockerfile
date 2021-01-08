FROM python:3.6
ADD data_whiteboard /data_whiteboard
WORKDIR /data_whiteboard
RUN pip install -r requirements.txt
WORKDIR /data_whiteboard/swagger_server
CMD python __main__.py