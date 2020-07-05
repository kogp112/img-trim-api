FROM python:3

ADD image_crop.py /
RUN pip install Pillow
COPY ./test.jpg /
CMD [ "python", "./image_crop.py", "test.jpg", "4" ]