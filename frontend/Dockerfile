FROM node:20-alpine as builder

WORKDIR /build

COPY package*.json ./
RUN npm install

COPY . ./
RUN npm run build

# WORKDIR /build/dist

# COPY . /var/www/frontend/