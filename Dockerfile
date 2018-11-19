FROM alpine:3.6
ADD ["fachschaftszitat/requirements.txt", "/requirements.txt"]
RUN apk upgrade --update && \
	apk add --update python3 && \ 
	pip3 install -r /requirements.txt && rm /requirements.txt
WORKDIR /fs_zitat
EXPOSE 80
VOLUME ["/fs_zitat/data"]
ENTRYPOINT ["python3", "manage.py"]
ADD ["fachschaftszitat", "/fs_zitat"]
CMD ["runserver", "0.0.0.0:80"]
