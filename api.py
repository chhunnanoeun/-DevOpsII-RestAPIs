from flask import Flask, request, jsonify

app = Flask(__name__)

products = [
    {"id":1, "name": "sneaker", "category":"Luxury Car", "price": 25000, "warehouse": 300},
    {"id":2, "name": "slipper", "category":"Mobile Phones", "price": 4500, "warehouse": 200},
    {"id":3, "name": "high heels", "category":"Household Furniture", "price": 399, "warehouse": 60},
]

@app.route('/products/', methods=["GET"])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=["GET"])
def get_product(id):
    product = next(filter(lambda x: x['id'] == id, products), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

@app.route('/products/', methods=["POST"])
def create_product():
    data = request.get_json()
    product_id = data["id"]
    if any(product for product in products if product['id'] == product_id):
        return jsonify({"error": "Product already exists"}), 400
    products.append(data)
    return jsonify(data), 201

@app.route('/products/<int:id>', methods=["PUT"])
def update_products(id):
    global products
    product = next(filter(lambda x: x['id'] == id, products), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    data = request.get_json()
    product.update(data)
    return jsonify(product), 200


@app.route('/products/<int:id>', methods=["DELETE"])
def delete_product(id):
    product = next(filter(lambda x: x['id'] == id, products), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    products.remove(product)
    return jsonify({"email": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
