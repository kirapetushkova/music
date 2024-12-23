FROM python:3.12-bullseye

WORKDIR /home/parinovapetushkova/music

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python3", "app/app.py"]
