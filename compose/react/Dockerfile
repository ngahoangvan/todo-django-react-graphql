FROM node:alpine
WORKDIR /app
COPY frontend/package.json .
COPY compose/react/entrypoint.sh .
RUN npm install
COPY frontend/ .
ENTRYPOINT [ "/bin/sh" ]
