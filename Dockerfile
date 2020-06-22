FROM python:3.8.3-slim-buster
RUN mkdir /app
ADD main.py /app
ADD requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=main.py
EXPOSE 5000
ENV PORT=5000
CMD flask run