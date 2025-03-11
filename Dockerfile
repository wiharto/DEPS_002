FROM python:3.9.10-slim-bullseye
# Update os and install necessary packages to enable pyodbc installation in Linux
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc unixodbc-dev \
  && apt-get install -y wget \
  && apt-get clean

RUN pip install poetry
RUN poetry config virtualenvs.create false

RUN mkdir deps_002
COPY ["pyproject.toml", "create_ccle_db.py", "main.py", "deps_002/"]
RUN wget https://ndownloader.figshare.com/files/34989940
RUN mv 34989940 deps_002/ccle_mutations.csv

WORKDIR deps_002
RUN poetry install

EXPOSE 8000:8000
