class Order:
    order_counter = 1  # For unique order IDs

    def __init__(self, products,customer_id=None):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.products = products
        self.total = sum(product['price'] * product['quantity'] for product in products)
        self.customer_id = customer_id

    def __repr__(self):
        return f"Order(ID: {self.order_id}, Products: {self.products}, Total: {self.total})"