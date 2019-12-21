FROM python:3.7
COPY . /web
WORKDIR /web
RUN pip install -r ./requirements.txt
# RUN pip install pystrich
CMD [ "python", "./run.py"]
