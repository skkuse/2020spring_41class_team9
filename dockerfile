FROM        python:3.8-alpine
ADD         src /
RUN         python -m pip install --upgrade pip
RUN         pip install -r requirements.txt
RUN         pip install gunicorn
EXPOSE      8086
ENTRYPOINT  ["gunicorn" "--bind=0.0.0.0:8086"]