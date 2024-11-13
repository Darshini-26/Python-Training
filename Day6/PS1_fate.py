#importing necessary modules
from PS1_update import Update
from PS1_product import Product
from PS1_logic import Logic

def fate():

    """Demonstrate various operations on a Product Management System."""

     # Create two product instances and print them
    task_object1=Product(1,"Bottle",300)
    print(task_object1)
    task_object2=Product(2,"Bag",500)
    print(task_object2)

    # Initialize the Logic class for managing products
    lo=Logic()

    # Add the products to the system and print a success or failure message
    la=lo.add_product(task_object1)
    la=lo.add_product(task_object2)
    if la:
        print("Successfully added product")
    else:
        print("Failed")


    # '''Update the information of a product'''
    # updated_product_object = UpdateProduct(1, 5000)
    # b= logic_object.update_product(updated_product_object)
    # if b == True:
    #     print ("Product is updated")
    # else:
    #     print ("Product ID is not found")

    # Update the details of a product and print a success or failure message
    updated_product=Update(1,200)
    a=lo.update(updated_product)
    if a==True:
        print("Product is updated")
    else:
        print("Product is not found")

    # Apply a discount to all products
    ld=lo.discount(10)
    print("Discount applied")
    print(ld)

    # View all products and print their details
    va=lo.view_all()
    print("All products:")
    for i in va:
        print(i)


# Execute the fate function
fate()