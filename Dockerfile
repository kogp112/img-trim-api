FROM python:3

ADD img_trim.py /

RUN pip install Pillow matplotlib

CMD [ "python", "./img_trim.py" ]