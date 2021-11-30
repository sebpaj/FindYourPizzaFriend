const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require('@apollo/gateway');

require('dotenv').config();

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'pizza', url: process.env.PIZZA_URL ? process.env.PIZZA_URL : 'http://localhost:8000' },
  ],
});

const server = new ApolloServer({
  gateway,
});

server.listen().then(({ url }) => {
  console.log(`🚀 Gateway ready at ${url}`);
}).catch(err => { console.error(err) });

