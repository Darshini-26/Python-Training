from ps2_db import Database
from ps2_order import Order

class Logic:
    def __init__(self, db_name="orders.db"):
        self.db = Database(db_name)
        self.orders = []
        self._sync_order_counter()

    def _sync_order_counter(self):
        """Synchronize the Order.order_counter with the maximum id in the database."""
        self.db.cursor.execute("SELECT MAX(id) FROM orders")
        max_id = self.db.cursor.fetchone()[0]
        if max_id is not None:
            Order.order_counter = max_id + 1

    def place_order(self, products, customer_id):
        """Places a new order with the specified products and adds it to the order list."""
        order = Order(products, customer_id)
        self.orders.append(order)
        self.add_order(order)
        return order.order_id

    def add_order(self, order):
        """Add a new order to the database."""
        products_str = ";".join([f"{prod['name']}:{prod['price']}:{prod['quantity']}" for prod in order.products])
        self.db.cursor.execute("INSERT INTO orders (id, customer_id, products, total) VALUES (?, ?, ?, ?)",
                            (order.order_id, order.customer_id, products_str, order.total))
        self.db.conn.commit()

    def list_orders(self):
        """Lists all orders currently managed by the OrderManager."""
        return self.get_all_orders()

    def get_all_orders(self):
        """Retrieve all orders from the database."""
        self.db.cursor.execute("SELECT * FROM orders")
        orders = self.db.cursor.fetchall()
        return orders

    def calculate_total_cost(self):
        """Calculates the total cost of all orders."""
        all_orders = self.get_all_orders()
        return sum(order[3] for order in all_orders)

    def cancel_order(self, order_id):
        """Cancels an order with the specified order ID by removing it from the order list."""
        self.delete_order(order_id)
        self.orders = [order for order in self.orders if order.order_id != order_id]

    def delete_order(self, order_id):
        """Delete an order from the database."""
        self.db.cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
        self.db.conn.commit()

    def summarize_orders(self, customer_id):
        """Summarizes orders for a specified customer, including total order count and list of orders."""
        all_orders = self.get_all_orders()
        customer_orders = [order for order in all_orders if order[1] == customer_id]
        summary = {"total_orders": len(customer_orders), "orders": customer_orders}
        return summary

    def close(self):
        """Close the database connection."""
        self.db.close()
