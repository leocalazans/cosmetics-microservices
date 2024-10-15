class ProductService {
  constructor(productRepository) {
    this.productRepository = productRepository;
  }

  async listProducts(limit, skip) {
    return await this.productRepository.findAll(limit, skip);
  }

  async searchProducts(query, limit, skip) {
    return await this.productRepository.findByNameOrDescription(query, limit, skip);
  }

  async addProduct(product) {
    return await this.productRepository.addProduct(product);
  }
  
  async getProductById(id) {
    // Implemente a lógica para buscar o produto pelo ID aqui
    const product = await this.productRepository.findById(id); // Exemplo usando mongoose
    return product;
  }

  async getProductsByCategory(category) {
    return await this.productRepository.findByCategory(category);
  }

  async getAllCategories() {
    return await this.productRepository.findAllCategories();
  }
}

module.exports = ProductService;
