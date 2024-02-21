FROM python:3.6
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev
WORKDIR /home/app
COPY requeriments.txt /home/app/
RUN pip install -r /home/app/requeriments.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build -t sgi . 
# docker run -p 8000:8000 sgi
```