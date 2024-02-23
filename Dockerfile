FROM python:3.6
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gnupg \
    g++ \
    unixodbc-dev


# Add Microsoft's repo for the latest version of MSODBC
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install MSODBCSQL
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17


WORKDIR /home/app
COPY requeriments.txt /home/app/
RUN pip install -r /home/app/requeriments.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build -t sgi . 
# docker run -p 8000:8000 sgi
