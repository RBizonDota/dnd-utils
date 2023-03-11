FROM python:3.7.9

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

WORKDIR /code

CMD [ "python", "-m", "dnd_utils" ]