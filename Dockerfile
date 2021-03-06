FROM alpine:3.11
ADD ["src/requirements.txt", "/requirements.txt"]
RUN apk upgrade --update && \
	apk add --update python3 build-base openldap-dev python3-dev py3-psycopg2 && \ 
	pip3 install -r /requirements.txt && rm /requirements.txt
WORKDIR /quotes
EXPOSE 80
COPY "src" "/quotes"
VOLUME ["/quotes/data"]
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]
