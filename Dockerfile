FROM python:3.8
COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt
COPY . .
