#QUESTION: CREATE A LIST WITH DICTIONARY AS ELEMENTS AND CREATE A MENU WITH FUNCTIONS:
#ADD TASK, UPDATE TASK, REMOVE TASK, PRINT ALL TASK AND EXIT

task=[]

def create_task(taskid,status):
    t={"taskid":taskid,"status":status}
    task.append(t)
    return f"Task {taskid} is added"

def update_task(taskid,_status):
    for i in task:
        if i["taskid"]==taskid:
            i["status"]==_status
            return f"Task {taskid} is updated to {_status}"
        return f"Task not found"

def remove_task(taskid,_status):
    for i in task:
        if i["taskid"]==taskid:
            task.remove(i)
            return f"Task {taskid} is removed"
        return f"Task not found"
    
def print_task():
    for i in task:
        return f"Task: {i["taskid"]} , status: {i["status"]}"


def start():
    while True:
        print("Choose 1/2/3/4/5")
        print("1- Create task")
        print("2- Update task")
        print("3- Remove task")
        print("4- Print all task")
        print("5- Exit task")

        choice=int(input("Enter a choice")) 
        if choice==1:
            taskid=int(input("Enter the taskid"))
            status=input("Enter the status")
            creat=create_task(taskid,status)
            print(creat)
            
        elif choice==2:
            taskid=int(input("Enter the task taskid"))
            status=input("Enter the status")
            up=update_task(taskid,status)
            print(up)

        elif choice==3:
            taskid=int(input("Enter the task taskid"))
            rem=remove_task(taskid,status)
            print(rem)

        elif choice==4:
            pr=print_task()
            print(pr)

        elif choice==5:
            print("exiting the program")

        else:
            print("Invalid choice, please try again.")


start()