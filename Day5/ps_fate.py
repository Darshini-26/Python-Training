from PS1_task import product
from ps_logic import Logic

def fate():
    task_object1=product(1,"Bottle",300)
    print(task_object1)

    task_object2=product(2,"Bag",500)
    print(task_object2)

    lo=Logic()
    la=lo.add_product(task_object1)
    la=lo.add_product(task_object2)
    if la:
        print("Successfully added product")
    else:
        print("Failed")

    lu=lo.update(1,"pen",200)
    if lu==True:
        print("Product is updated")
    else:
        print("Product is not found")


    ld=lo.discount(10)
    print("Discount applied")

    va=lo.view_all()
    print("All products:")
    for i in va:
        print(i)






fate()


