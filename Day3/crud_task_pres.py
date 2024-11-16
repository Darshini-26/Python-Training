import crud_task_logic

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
            crud_task_logic.add_task(taskid, status)
       
        elif choice == "2":
            taskid = input("Enter task ID to update: ")
            new_status = input("Enter new status: ")
            crud_task_logic.update_task(taskid, new_status)
       
        elif choice == "3":
            taskid = input("Enter task ID to remove: ")
            crud_task_logic.remove_task(taskid)
       
        elif choice == "4":
            crud_task_logic.print_all_tasks()
       
        elif choice == "5":
            print("Exiting program.")
            break
       
        else:
            print("Invalid choice, please try again.")
 
start()