FROM node:latest

RUN mkdir federation
COPY package.json ./package.json
COPY supergraph.graphql ./supergraph.graphql
COPY index.js ./index.js
RUN npm i

RUN apt-get update && apt-get install -y iputils-ping curl telnet

CMD node index.js