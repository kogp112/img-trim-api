FROM python:3

ADD img_trim.py /
RUN pip install Pillow matplotlib
COPY ./test.jpg /
CMD [ "python", "./img_trim.py" ]