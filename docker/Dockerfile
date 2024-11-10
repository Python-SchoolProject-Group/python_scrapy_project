FROM python:3.10.0
LABEL authors="张洛"
ADD . /code
WORKDIR /code
COPY ../scrapyd.conf /etc/scrapyd/
EXPOSE 6800
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD scrapyd