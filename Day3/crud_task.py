task=[]
 
def add_task(taskid,status):
    task={"taskid": taskid, "status": status}
    task.append(task)
    print(f"Task{taskid} is added")
 
def update_task(taskid,new_status):
        for task in task:
            if task["taskid"] == taskid:
                task["status"] = new_status
                print(f"Task {taskid} is updated to {new_status}")
                return
        print(f"Task {taskid} is not found")
 
def remove_task(taskid):
    for task in task:
        if task["taskid"] == taskid:
            task.remove(task)
            print(f"Task {taskid} is removed")
            return
    print(f"Task {taskid} is not found")
 
def print_all_tasks():        
    if task:
        for task in task:
            print(f"taskId: {task["taskId"]} , status: {task["status"]}")
    else:
        print("No tasks available.")
 
def start():
    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. Print All Tasks")
        print("5. Exit")
       
        choice = input("Enter choice (1-5): ")
        if choice == "1":
            taskid = input("Enter task ID: ")
            status = input("Enter task status: ")
            add_task(taskid, status)
       
        elif choice == "2":
            taskid = input("Enter task ID to update: ")
            new_status = input("Enter new status: ")
            update_task(taskid, new_status)
       
        elif choice == "3":
            taskid = input("Enter task ID to remove: ")
            remove_task(taskid)
       
        elif choice == "4":
            print_all_tasks()
       
        elif choice == "5":
            print("Exiting program.")
            break
       
        else:
            print("Invalid choice, please try again.")
 
start()