FROM python:3.10-buster
EXPOSE 4000
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
