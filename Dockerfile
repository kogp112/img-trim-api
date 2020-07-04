FROM python:3

ADD img_trim.py /
RUN pip install Pillow
COPY ./test.jpg /
CMD [ "python", "./img_crop.py" ]