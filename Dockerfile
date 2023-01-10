FROM python:3.10.0

WORKDIR /app

COPY requirements.txt requironments.txt

RUN pip3 install -r requironments.txt

COPY . .

CMD python3 main.py