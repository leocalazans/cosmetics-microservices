class ProductController {
  constructor(productService) {
    this.productService = productService;
  }

  async listProducts(req, reply) {
    const { limit = 40, skip = 0 } = req.query; 
    const products = await this.productService.listProducts(parseInt(limit), parseInt(skip));
    return reply.send(products);
  }

  async searchProducts(req, reply) {
    const { query } = req.params;
    const { limit = 4, skip = 0 } = req.query;
    const products = await this.productService.searchProducts(query, parseInt(limit), parseInt(skip));
    return reply.send(products);
  }

  async addProduct(req, reply) {
    const product = req.body;
    await this.productService.addProduct(product);
    return reply.code(201).send({ message: 'Product added successfully' });
  }

  async getProductById(req, reply) {
    const { id } = req.params; 
    try {
      const product = await this.productService.getProductById(id); 
      if (!product) {
        return reply.status(404).send({ message: 'Produto não encontrado' }); 
      }
      return reply.send(product); 
    } catch (error) {
      return reply.status(500).send({ message: 'Erro ao buscar o produto', error }); 
    }
  }

  async getCategories(req, reply) {
    try {
      const categories = await this.productService.getAllCategories();
      return reply.send({ categories });
    } catch (error) {
      return reply.status(500).send({ error: 'Erro ao buscar categorias' });
    }
  }
}

module.exports = ProductController;
