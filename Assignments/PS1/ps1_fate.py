from ps1_update import Update
from ps1_product import Product
from ps1_logic import Logic

def fate():
    """Demonstrate various operations on a Product Management System."""

    # Create two product instances and print them
    task_object1 = Product(4, "Bottle", 300)
    # print(task_object1)
    task_object2 = Product(5, "Bag", 500)
    # print(task_object2)

    # Initialize the Logic class for managing products
    lo = Logic()

    # Add the products to the system and print a success or failure message
    la1 = lo.add_product(task_object1)
    la2 = lo.add_product(task_object2)
    if la1 and la2:
        print("Successfully added products")
    else:
        print("Failed to add products")

     # View all products and print their details
    va = lo.view_all_products()
    print("All products:")
    for product in va:
        print(product)

    # Update the details of a product and print a success or failure message
    updated_product = Update(2, 200)
    a = lo.update_product(updated_product)
    if a:
        print("Product is updated")
    else:
        print("Product is not found")

    # Apply a discount to all products
    ld = lo.apply_discount(10)
    if ld:
        print("Discount applied:")
        for product in lo.view_all_products():
            print(product)
    else:
        print("Failed to apply discount")


    # Close the database connection
    lo.close()

# Execute the fate function
fate()
