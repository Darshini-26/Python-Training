from logic import Logic
from presentation import Presentation
from task import Task

def fate():
    print(f"Hello")
   
if __name__ == "__main__":
    fate()

   
    ta=Task(3,"ABC",5,"Success","Cbe")
    print(ta)

    lo=Logic()
    la=lo.add(ta)
    if la:
        print("Success")
    else:
        print("Failed")

    va=lo.view_all()
    for i in va:
        print(i)
    
    