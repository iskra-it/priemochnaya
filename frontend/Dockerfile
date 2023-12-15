FROM node:20-alpine

WORKDIR /build

COPY . /build/
RUN npm run build
COPY /build/dist/ /var/www/frontend