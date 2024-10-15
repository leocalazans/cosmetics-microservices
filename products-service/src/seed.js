const ProductRepository = require('./repositories/ProductRepository');
const Product = require('./entities/Product');

async function seedProducts(db) {
  const productRepository = new ProductRepository(db);

  const existingProducts = await productRepository.findAll();
  if (existingProducts.length > 0) {
    console.info('Produtos já existem no banco de dados.');
    return;
  }

  const categories = ['beleza', 'cuidado pessoal', 'maquiagem', 'cabelo', 'perfume'];

  const products = Array.from({ length: 40 }, (v, i) => {
    const randomCategory = categories[Math.floor(Math.random() * categories.length)];

    return new Product(
      `Produto ${i + 1}`,
      `Descrição do Produto ${i + 1}`,
      `https://picsum.photos/800?random=${i + 1}`, 
      (Math.random() * 5).toFixed(1), 
      (Math.random() * 100).toFixed(2), 
      (Math.random() * 100).toFixed(2),
      randomCategory  
    );
  });


  for (const product of products) {
    await productRepository.addProduct(product);
  }

  console.info('40 produtos de demonstração foram inseridos.');
}

module.exports = seedProducts;
