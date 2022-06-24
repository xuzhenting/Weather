FROM python:3.6.9
WORKDIR /app
ADD . /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python3 1-1.py
CMD python3 1-2.py
