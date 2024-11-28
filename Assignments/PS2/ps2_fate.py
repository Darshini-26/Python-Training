from ps2_logic import Logic

# Initialize the OrderManager
order_manager = Logic()

# Sample products for orders
products1 = [
    {"name": "Product A", "price": 10, "quantity": 2},
    {"name": "Product B", "price": 5, "quantity": 5}
]

products2 = [
    {"name": "Product C", "price": 20, "quantity": 1},
    {"name": "Product D", "price": 15, "quantity": 3}
]

products3 = [
    {"name": "Product E", "price": 50, "quantity": 1}
]

# Test place_order function
print("Placing Orders")
order_id1 = order_manager.place_order(products1, 1)  # Order 1 for Customer 1
order_id2 = order_manager.place_order(products2, 2)  # Order 2 for Customer 2
order_id3 = order_manager.place_order(products3, 1)  # Order 3 for Customer 1

print(f"Order IDs: {order_id1}, {order_id2}, {order_id3}")

# Test list_orders function
print("\nListing All Orders:")
all_orders = order_manager.list_orders()
for order in all_orders:
    print(order)

# Test calculate_total_cost function
print("\nCalculating Total Cost of All Orders:")
total_cost = order_manager.calculate_total_cost()
print(f"Total Cost of All Orders: {total_cost}")

# Test cancel_order function
print("\nCancelling Order ID 2")
order_manager.cancel_order(order_id2)

print("Updated List of Orders After Cancellation:")
updated_orders = order_manager.list_orders()
for order in updated_orders:
    print(order)

# Test summarize_orders function for Customer 1
print("\nSummarizing Orders for Customer ID 1:")
summary_customer_1 = order_manager.summarize_orders(customer_id=1)
print(f"Total Orders for Customer 1: {summary_customer_1['total_orders']}")
print("Orders:")
for order in summary_customer_1['orders']:
    print(order)

# Test summarize_orders function for Customer 2
print("\nSummarizing Orders for Customer ID 2:")
summary_customer_2 = order_manager.summarize_orders(customer_id=2)
print(f"Total Orders for Customer 2: {summary_customer_2['total_orders']}")
print("Orders:")
for order in summary_customer_2['orders']:
    print(order)

# Close the database connection
order_manager.close()
