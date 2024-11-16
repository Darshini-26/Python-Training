from logic import Logic
from presentation import Presentation
from task import Task

def fate():
    print(f"Hello")
   
if __name__ == "__main__":
    #fate()

   
    ta=Task(3,"ABC",5,"Success","Cbe")
    print(ta)
    tt=Task(4,"ABCd",6,"Failure","Cbe")
    lo=Logic()
    la=lo.add(ta)
    la=lo.add(tt)
    if la:
        print("Success")
    else:
        print("Failed")

    lu=lo.update(3,4,"Yes","Chennai")
    if lu==True:
        print("Task is updated")
    else:
        print("Task ID is not found")

    lr=lo.remove(3)
    if lr==True:
        print("Task is removed")
    else:
        print("Task id is not found")

    va=lo.view_all()
    print("All tasks:")
    for i in va:
        print(i)

    vp=lo.view_priority(6)
    print("Based on priority:")
    for i in vp:
        print(i)

    vl=lo.view_location("Cbe")
    print("Based on location:")
    for i in vl:
        print(i)

    vs=lo.view_status("Failure")
    print("Based on status:")
    for i in vs:
        print(i)
    
    