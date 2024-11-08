
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
            print(f"taskid: {task['taskid']} , status: {task['status']}")
    else:
        print("No tasks available.")
 
 
