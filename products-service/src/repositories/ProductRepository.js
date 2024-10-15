const { ObjectId } = require('mongodb');

class ProductRepository {
  constructor(db) {
    this.collection = db.collection('products');
  }

  async findAll(limit = 40, skip = 0) {
    return await this.collection.find().skip(skip).limit(limit).toArray();
  }

  async findByNameOrDescription(query, limit = 4, skip = 0) {
    return await this.collection.find({
      $or: [{ name: query }, { description: { $regex: query, $options: 'i' } }]
    }).skip(skip).limit(limit).toArray();
  }

  async addProduct(product) {
    return await this.collection.insertOne(product);
  }

  async findById(id) {
    const objectId = new ObjectId(id);
    const product = await this.collection.findOne({ _id: objectId });
    if (!product) {
      throw new Error('Product not found');
    }
    return product;
  }
  async findByCategory(category) {
    try {
      const products = await this.collection.find({ category }).toArray();
      return products;
    } catch (error) {
      throw new Error("Erro ao buscar produtos por categoria");
    }
  }
  async findAllCategories() {
    return await this.collection.distinct('category');
  }
}

module.exports = ProductRepository;
