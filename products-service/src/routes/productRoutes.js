const ProductController = require('../controllers/ProductController');

async function productRoutes(fastify, options) {
  const productController = new ProductController(fastify.productService);

  fastify.get('/products', async (req, reply) => {
    return await productController.listProducts(req, reply);
  });

  fastify.get('/products/search/:query', async (req, reply) => {
    return await productController.searchProducts(req, reply);
  });

  fastify.post('/products', productController.addProduct.bind(productController));
  
  const getProductById = async (req, reply) => {
    const productId = req.params.id; // Recupera o ID do produto da URL
    try {
      const product = await productController.productService.getProductById(productId); // Chama o método no service
      if (product) {
        return reply.send(product);
      } else {
        return reply.status(404).send({ message: 'Produto não encontrado' });
      }
    } catch (error) {
      return reply.status(500).send({ message: 'Erro interno do servidor' });
    }
  };

  fastify.get('/products/:id', getProductById); 

  fastify.get('/products/category/:category', async (request, reply) => {
    const { category } = request.params;
    
    try {
      const products = await productService.getProductsByCategory(category);
      if (products.length === 0) {
        reply.code(404).send({ message: 'Nenhum produto encontrado para essa categoria.' });
      } else {
        reply.code(200).send(products);
      }
    } catch (error) {
      reply.code(500).send({ message: 'Erro ao buscar produtos por categoria.' });
    }
  });

  fastify.get('/products/categories', async (req, reply) => {
    return await productController.getCategories(req, reply);
  });
}

module.exports = productRoutes;
