FROM nginx:latest
LABEL maintainer="Seongjae Hwang <lotsofluck4m@gmail.com>"

ENV BASE_DIR /apps/rekindle

RUN mkdir -p $BASE_DIR

WORKDIR $BASE_DIR

COPY . .

CMD echo 'Dockerfile: TBD'
