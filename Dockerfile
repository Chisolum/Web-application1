FROM python:3.7
COPY . /web
WORKDIR /web
ADD blog_api/src src
RUN pip install -r ./requirements.txt
# RUN pip install pystrich
# CMD [ "python", "./run.py"]
ENTRYPOINT ["python"]
CMD ["./run.py"]
manage.py db migrate
