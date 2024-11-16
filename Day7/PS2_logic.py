'''Create functions to
place an order for products, 
list all orders, and 
calculate the total cost of all orders.
Each order should contain a unique order ID, the list of products ordered, and the order total.
Include functionality to cancel an order, which should remove it from the orders list.
Implement a function to summarize all orders for a given customer.'''

from PS2_order import Order


class OrderManager:
    def __init__(self):
        self.orders = []

    def place_order(self, products):
        """Places a new order with the specified products and adds it to the order list."""
        order = Order(products)
        self.orders.append(order)
        return order.order_id
    
    def list_orders(self):
        """Lists all orders currently managed by the OrderManager."""
        return self.orders

    def calculate_total_cost(self):
        """Lists all orders currently managed by the OrderManager."""
        return sum(order.total for order in self.orders)

    def cancel_order(self, order_id):
        """Cancels an order with the specified order ID by removing it from the order list."""
        self.orders = [order for order in self.orders if order.order_id != order_id]

    def summarize_orders(self, customer_id):
        """Summarizes orders for a specified customer, including total order count and list of orders"""
        customer_orders = [order for order in self.orders if order.customer_id == customer_id]
        summary = {"total_orders": len(customer_orders), "orders": customer_orders}
        return summary
