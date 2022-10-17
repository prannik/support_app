# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /support_app

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install psycopg2 dependencies
#RUN apt-get update && apt-get install postgresql-dev gcc python3-dev musl-dev
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy whole src
COPY . .

# filtering and setting access rights on start scripts
COPY ./scripts/entrypoint.sh .
RUN sed -i 's/\r$//g' /support_app/scripts/entrypoint.sh
RUN chmod +x /support_app/scripts/entrypoint.sh

COPY ./scripts/web_start.sh .
RUN sed -i 's/\r$//g' /support_app/scripts/web_start.sh
RUN chmod +x /support_app/scripts/web_start.sh

COPY ./scripts/celery_worker_start.sh .
RUN sed -i 's/\r$//g' /support_app/scripts/celery_worker_start.sh
RUN chmod +x /support_app/scripts/celery_worker_start.sh

# run entrypoint.sh
ENTRYPOINT ["/support_app/scripts/entrypoint.sh"]
