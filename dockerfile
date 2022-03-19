FROM python:3

ADD App.py /

RUN pip3 install speedtest-cli

CMD [ "python3", "./App.py" ]