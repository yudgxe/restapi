FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=main
CMD flask run --host 0.0.0.0

