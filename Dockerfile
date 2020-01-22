FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7


#WORKDIR /usr/src/app

COPY ./app /app

#RUN pip install -r requirements.txt
#
#CMD ["uvicorn", "main:app","--reload" ]
