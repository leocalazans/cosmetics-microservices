const fastify = require('fastify')({ logger: true });
const swagger = require('@fastify/swagger');
const fastifySwaggerUi = require('@fastify/swagger-ui');
const mongodb = require('@fastify/mongodb');
const productRoutes = require('./routes/productRoutes');
const ProductRepository = require('./repositories/ProductRepository');
const ProductService = require('./services/ProductService');
const seedProducts = require('./seed');  // Adicionar o seed
const cors = require('@fastify/cors');
const uri = "mongodb+srv://mrlewry:UGDcNuV365xysR7q@cluster0.egkpc.mongodb.net/cosmeticos?retryWrites=true&w=majority&appName=Cluster0";

// Registre o plugin do MongoDB
fastify.register(mongodb, {
  forceClose: true,
  url: uri
});

fastify.register(cors, {
  origin: (origin, cb) => {
    const whitelist = ['http://localhost:5173'];
    if (whitelist.indexOf(origin) !== -1 || !origin) {
      cb(null, true);
    } else {
      cb(new Error('Not allowed by CORS'));
    }
  },
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  exposedHeaders: ['X-Total-Count'],
  credentials: true,
});
module.exports = fastify;

fastify.register(swagger, {
  routePrefix: '/docs',  
  swagger: {
    info: {
      title: 'API de Cosméticos',
      description: 'Documentação da API para gerenciamento de cosméticos',
      version: '1.0.0',
    },
    host: 'localhost:3000',
    schemes: ['http'],
    consumes: ['application/json'],
    produces: ['application/json'],
  },
  exposeRoute: true
});

fastify.register(fastifySwaggerUi, {
  routePrefix: '/docs',  
  uiConfig: {
    docExpansion: 'full',
    deepLinking: false
  },
  exposeRoute: true
});

fastify.after(() => {
  const db = fastify.mongo.db;
  
  if (!db) {
    fastify.log.error(fastify.mongo);
    fastify.log.error('Banco de dados MongoDB não está acessível.');
    process.exit(1);
  }

  fastify.decorate('productService', new ProductService(new ProductRepository(db)));
});

fastify.register(productRoutes);


const start = async () => {
  try {
    await fastify.listen({ port: 3000 });
    fastify.log.info(`Server running at http://localhost:3000`);
    await seedProducts(fastify.mongo.db);
    fastify.swagger(); 
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();

