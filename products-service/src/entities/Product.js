class Product {
    constructor(name, description, image, rating = null, price, oldprice = null, category= null) {
      this.name = name;
      this.description = description;
      this.image = image;
      this.rating = rating;
      this.price = price;
      this.oldprice = oldprice;
      this.category = category;
    }
}
module.exports = Product;
  