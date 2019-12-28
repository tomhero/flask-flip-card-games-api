FROM nginx:1.17.6-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY certs/server.cert /etc/nginx/certs/server.cert
COPY certs/server.key /etc/nginx/certs/server.key