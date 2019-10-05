FROM python:alpine

LABEL maintainer="linweiyuan <root@linweiyuan.com>"

ENV FOLDER shadowsocks-flask

COPY . ${FOLDER}

WORKDIR ${FOLDER}

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk add --no-cache python3-dev build-base gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del python3-dev build-base gcc

EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]
