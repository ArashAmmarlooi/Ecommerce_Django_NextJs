# frontend/Dockerfile

FROM node:18.17

WORKDIR /frontend
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . .

RUN npm run build