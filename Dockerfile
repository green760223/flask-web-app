FROM python:3.10-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 4000
COPY . /app
CMD ["python", "app.py"]




