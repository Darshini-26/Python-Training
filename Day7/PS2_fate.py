from PS2_logic import OrderManager

# Initialize the OrderManager
order_manager = OrderManager()

# Define some sample products
products1 = [
    {"name": "Chair ", "price": 500, "quantity": 2},
    {"name": "Table", "price": 1000, "quantity": 5}
]

products2 = [
    {"name": "Shirt", "price": 1000, "quantity": 1},
    {"name": "Denim", "price": 2000, "quantity": 3}
]

# Place Orders
print("Placing Orders")
order_id1 = order_manager.place_order(products1)
print(f"Order ID {order_id1} placed")
order_id2 = order_manager.place_order(products2)
print(f"Order ID {order_id2} placed")

# List all Orders
print("\nListing All Orders:")
orders = order_manager.list_orders()
for order in orders:
    print(order)

# Calculate Total Cost of All Orders
print("\nCalculating Total Cost of All Orders")
total_cost = order_manager.calculate_total_cost()
print(f"Total cost of all orders: {total_cost}")

# Cancel an Order
print(f"\nCanceling Order ID {order_id2}")
order_manager.cancel_order(order_id2)

# List all Orders after cancellation
print("\nListing All Orders After Cancellation:")
orders = order_manager.list_orders()
for order in orders:
    print(order)

